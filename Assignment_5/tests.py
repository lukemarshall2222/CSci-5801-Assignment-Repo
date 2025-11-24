"""
This module contains tests for the rls_source.py sourcecode file.
"""

import pytest
from rls_source import Artifact, button_press, system

class TestArtifact:
    """tests for Artifact class"""

    def test_battery_false(self):
        """test launch pad light with battery_charged = False makes launch_pad.green == False"""
        # battery_charged = False, circuit_closed = True
        launch_pad = Artifact('launchpad', True, (False and True))
        assert launch_pad.red == True
        assert launch_pad.green == False

    def test_circuit_false(self):
        """test launch pad light with  the circuit_closed = False makes launch_pad.green == False"""
        # battery_charged = True, circuit_closed = False
        launch_pad = Artifact('launchpad', True, (True and False))
        assert launch_pad.red == True
        assert launch_pad.green == False

    def test_circuit_true(self):
        """test launch pad light with  both battery and cuituit True makes launch_pad.green == True"""
        launch_pad = Artifact('launchpad', True, (True and True))
        assert launch_pad.red == True
        assert launch_pad.green == True
    
    def test_ready_false(self):
        """test control unit lights with ready_to_launch = False makes control_unit.red == False"""
        # ready_to_launch = False, launch = True
        control_unit = Artifact('control unit', False, True)
        assert control_unit.red == False
        assert control_unit.green == True
    
    def test_launch_false(self):
        """test control unit lights with launch = False makes control_unit.green == False"""
        # ready_to_launch = True, launch = False
        control_unit = Artifact('control unit', True, False)
        assert control_unit.red == True
        assert control_unit.green == False
    
    def test_ready_launch_true(self):
        """test control unit lights with both ready_to_launch = True and launch = True"""
        # ready_to_launch = True, launch = True
        control_unit = Artifact('control unit', True, True)
        assert control_unit.red == True
        assert control_unit.green == True


class TestButtonPress:
    """tests for button_press() function"""

    def test_button_simple_true(self, monkeypatch, capsys):
        """correct input on first try, result is true"""
        monkeypatch.setattr('builtins.input', lambda _: 't')

        result = button_press('t', True, 'Success', 'Failure')

        assert result == True
        captured = capsys.readouterr()
        assert 'Success' in captured.out

    def test_button_simple_false(self, monkeypatch, capsys):
        """correct input on first try, result is false"""
        monkeypatch.setattr('builtins.input', lambda _: 't')

        result = button_press('t', False, 'Success', 'Failure')

        assert result == False
        captured = capsys.readouterr()
        assert 'Failure' in captured.out

    def test_button_complex_true(self, monkeypatch, capsys):
        """test if button behaves correctly in face of multiple inccorect input followed by correct resulting in true"""
        inputs = iter(['x', 'y', 't'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        result = button_press('t', True, 'Success', 'Failure')

        assert result == True
        captured = capsys.readouterr()
        assert 'Success' in captured.out

    def test_button_complex_false(self, monkeypatch, capsys):
        """Test if button behaves correctly in face of multiple incorrect input followed by correct resulting in false"""
        inputs = iter(['a', 'b', 't'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        result = button_press('t', False, 'Success', 'Failure')

        assert result == False
        captured = capsys.readouterr()
        assert 'Failure' in captured.out


class TestSystem:
    """test system() function"""

    def test_system_all_success(self, monkeypatch, capsys):
        """total launch sequence, all steps should complete normally"""
        inputs = iter(['t', 'e', 'r', 'l'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        launch_pad = Artifact('launchpad', red=True, green=True)
        control_unit = Artifact('control unit', red=True, green=True)

        system(launch_pad, control_unit)

        captured = capsys.readouterr()
        assert 'Circuit is functional' in captured.out
        assert 'Communication is enabled' in captured.out
        assert 'We are ready to launch' in captured.out
        assert 'Rocket is launching' in captured.out

    def test_system_test_fail(self, monkeypatch, capsys):
        """should fail at test button"""
        monkeypatch.setattr('builtins.input', lambda _: 't')

        # signifies batteries are not charged or the circuit is not closed, causes test to fail
        launch_pad = Artifact('launchpad', red=True, green=False)
        control_unit = Artifact('control unit', red=True, green=True)

        system(launch_pad, control_unit)

        captured = capsys.readouterr()
        assert 'Error with circuit' in captured.out
        # success response not reached
        assert 'Communication is enabled' not in captured.out

    def test_system_enable_fail(self, monkeypatch, capsys):
        """should fail at enable button"""
        inputs = iter(['t', 'e'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        # signifies the communication enabling should fail because it is not enabled at a higher level
        launch_pad = Artifact(red=False, green=True) 
        control_unit = Artifact(red=True, green=True)

        system(launch_pad, control_unit)

        captured = capsys.readouterr()
        assert 'Circuit is functional' in captured.out
        assert 'Error with communication' in captured.out
        assert 'We are ready to launch' not in captured.out  # success response not reached

    def test_system_ready_fail(self, monkeypatch, capsys):
        """should fail at ready button"""
        inputs = iter(['t', 'e', 'r'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        launch_pad = Artifact('launchpad', red=True, green=True)
        # signifies the ready communication should fail because it is not enabled at a higher level
        control_unit = Artifact('control unit', red=False, green=True)

        system(launch_pad, control_unit)

        captured = capsys.readouterr()
        assert 'Circuit is functional' in captured.out
        assert 'Communication is enabled' in captured.out
        assert 'We are not ready to launch' in captured.out
        assert 'Rocket is launching' not in captured.out  # success response not reached

    def test_system_fail_launch_fail(self, monkeypatch, capsys):
        """should fail at launch"""
        inputs = iter(['t', 'e', 'r', 'l'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        launch_pad = Artifact('launchpad', red=True, green=True)
        # signifies the launch communication should fail because it is not enabled at a higher level
        control_unit = Artifact('control unit', red=True, green=False)

        system(launch_pad, control_unit)

        captured = capsys.readouterr()
        assert 'Circuit is functional' in captured.out
        assert 'Communication is enabled' in captured.out
        assert 'We are ready to launch' in captured.out
        assert 'Rocket is not ready to launch' in captured.out

    def test_system_random_input_success(self, monkeypatch, capsys):
        """random input (noise) interleaved into the launch sequence should not imact the launch if all signals given in correct order
        -- possible place for improvement, could keep track of noise and if it exceeds some bound the launch is scrapped"""
        inputs = iter(['x', 't', 'y', 'e', 'z', 'r', 'a', 'l'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        launch_pad = Artifact('launchpad', red=True, green=True)
        control_unit = Artifact('control unit', red=True, green=True)

        system(launch_pad, control_unit)

        captured = capsys.readouterr()
        assert 'Rocket is launching' in captured.out




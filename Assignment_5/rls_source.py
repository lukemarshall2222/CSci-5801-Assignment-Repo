import argparse

class Artifact:
    def __init__(self, name, red=False, green=False):
        self.red: bool = red
        self.green: bool = green
        self.name = name

    def update(self, name, cond = True):
        if name == 'red':
            self.red = cond
        elif name == 'green':
            self.green = cond
        print(f'{self.name} has red light {self.red} and green light {self.green}')

class Environment:
    def __init__(self, communication_enabled, battery_charged, circuit_closed, ready_to_launch, launch):
        self.communication_enabled = communication_enabled
        self.battery_charged = battery_charged
        self.circuit_closed = circuit_closed
        self.ready_to_launch = ready_to_launch
        self.launch = launch
    
    def test_communication(self):
        return self.communication_enabled
    
    def test_circuit(self):
        return self.battery_charged and self.circuit_closed
    
    def test_ready(self):
        return self.ready_to_launch
    
    def launched(self):
        return(self.launch)

def button_press(button_char, condition, pass_message, fail_message) -> bool:
    # Buttons can be pressed in any order, but if pressed out of order nothing happens
    user_input: str = " "
    while user_input[0] != button_char:
        user_input = input(f"Enter t for test, e for enable, r for ready, and l for launch to test the button: ")
    
    if condition:
        print(pass_message)
        return True
    else:
        print(fail_message)
        return False

def system(launch_pad: Artifact, control_unit: Artifact, environment: Environment):
    # This would be housed in the launch pad which is the "server" role in this situation
    # Sort of a state machine, houses the pipe/filter operation
    test: bool = button_press('t', environment.test_circuit(), 'Circuit is functional', 'Error with circuit')
    launch_pad.update('red', test)
    if not test:
        return
    
    enable: bool = button_press('e', environment.test_communication(), 'Communication is enabled', 'Error with communication')
    launch_pad.update('green', enable)
    if not enable:
        return
    
    ready: bool = button_press('r', environment.test_ready(), 'We are ready to launch', 'We are not ready to launch')
    control_unit.update('red', ready)
    if not ready:
        return
    
    launch: bool = button_press('l', environment.launched(), 'Rocket is launching', 'Rocket is not ready to launch')
    control_unit.update('green', launch)
    if not launch:
        return

def main():
    launch_pad: Artifact = Artifact('launchpad')
    control_unit: Artifact = Artifact('control unit')
    environment: Environment = Environment(args.communication_enabled, args.battery_charged, args.circuit_closed, args.ready_to_launch, args.launch)
    system(launch_pad, control_unit, environment)
      
if __name__ == "__main__":
    # Uer sets up arguments that they want to set up as false
    parser = argparse.ArgumentParser(prog='rls_source')
    parser.add_argument('--battery_charged', action='store_false', help="Is the battery charged")
    parser.add_argument('--circuit_closed', action='store_false', help="Is the circuit closed?")
    parser.add_argument('--communication_enabled', action='store_false', help="Can control unit and launch pad interact?")
    parser.add_argument('--ready_to_launch', action='store_false', help="Does the launch pad know we are ready to launch?")
    parser.add_argument('--launch', action='store_false', help="Can we actually launch the rocket?")
    args = parser.parse_args()
    main()


import argparse

class Artifact:
    def __init__(self, red=True, green=True):
        self.red: bool = red
        self.green: bool = green

def button_press(button_char, condition, pass_message, fail_message) -> bool:
    # User input that tells the user to press a button
    user_input: str = " "
    while user_input[0] != button_char:
        user_input = input(f"Press 't' for test, 'e' for enable, 'r' for ready, and 'l' for launch: ")
    
    if condition:
        print(pass_message)
        return True
    else:
        print(fail_message)
        return False

def system(launch_pad: Artifact, control_unit: Artifact):
    test: bool = button_press('t', launch_pad.green, 'Circuit is functional', 'Error with circuit')
    if not test:
        return
    
    enable: bool = button_press('e', launch_pad.red, 'Communication is enabled', 'Error with communication')
    if not enable:
        return
    
    ready: bool = button_press('r', control_unit.red, 'We are ready to launch', 'We are not ready to launch')
    if not ready:
        return
    
    launch: bool = button_press('l', control_unit.green, 'Rocket is launching', 'Rocket is not ready to launch')
    if not launch:
        return

def main():
    launch_pad: Artifact = Artifact(args.communication_enabled, (args.battery_charged and args.circuit_closed))
    control_unit: Artifact = Artifact(args.ready_to_launch, args.launch)
    system(launch_pad, control_unit)
      
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


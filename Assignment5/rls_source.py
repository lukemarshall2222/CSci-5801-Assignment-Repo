import argparse

class Artifact:
    def __init__(self, red=True, green=True):
        self.red = red
        self.green = green

def button_press(button_char, button, condition, pass_message, fail_message):
    user_input = " "
    while user_input[0] != button_char:
        user_input = input(f"Enter '{button_char}' to press the {button} button: ")
    
    if condition:
        print(pass_message)
        return True
    else:
        print(fail_message)
        return False

def main():
    launch_pad = Artifact(args.communication_enabled, (args.battery_charged and args.circuit_closed))
    control_unit = Artifact(args.ready_to_launch, args.launch)
    
    test = button_press('t', 'test', launch_pad.green, 'Circuit is functional', 'Error with circuit')
    if not test:
        return
    
    enable = button_press('e', 'enable', launch_pad.red, 'Communication is enabled', 'Error with communication')
    if not enable:
        return
    
    ready = button_press('r', 'ready', control_unit.red, 'We are ready to launch', 'We are not ready to launch')
    if not ready:
        return
    
    launch = button_press('l', 'launch', control_unit.green, 'Rocket is launching', 'Rocket is not ready to launch')
    if not launch:
        return
        
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


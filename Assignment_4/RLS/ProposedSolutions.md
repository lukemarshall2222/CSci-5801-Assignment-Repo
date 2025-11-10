## Rocket Launch System
### Proposed Solutions
- For the Rocket Launch system, we will use a standard radio controller with a custom verfification process to ensure the requirements for safety and signals that should be passed betweeen the launch pad and controller are met.
- The control unit will start off in a disabled mode and cannot be switched to enabled except from the launch pad. The launch pad internally checks the battery connection and sends an enable signal to the control unit when the respective buttons are pressed. The control unit is in disarmed mode until the arming button is pressed, and sends a signal to the launch pad when launch is pressed. The launch pad is able to receive signals from the control unit like the launch command, and act on those commands like responding and launching the rocket. 

### Alternate Solutions
- We considered using a wired connection between the control unit and the launch pad, but this creates the task of organizing and setting up the wire and another expense.

- We also considered placing the lights on another module, a sort of inidcator board that everyone can see, separate from tither the control unit or the launch pad. We decided this was against the requirements and allows for another point of failure. 

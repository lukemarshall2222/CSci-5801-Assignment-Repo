# Typical Usage Scenario

## User Stories

- As a tester, I want to know if the circuit is fully connected so that the current can run.
- As a tester, I want to know if the launchpad can communicate with the control unit because I want to use them in tandem.
- As a tester, I want to know if the rocket is enabled so that I am ready to launch the rocket.
- As a tester, I want to launch the rocket so that I know if it's possible to launch the rocket at least once.

## Acceptance Criteria
- Redundancy in the launch controls
- Appropraite sequential progression based on result of previous step
    - abort launch if step failed
    - move forward if step succeeded
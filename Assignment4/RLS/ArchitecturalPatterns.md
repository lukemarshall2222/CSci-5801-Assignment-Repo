# RLS Proposed Decision

## Context

The Rocket Engineers want a safe way to test wheather or not their equipement for launching the rocket works. The current system is very unsafe, and we want to improve it.

## Decision

To address the criticality of the igniter system functioning properly, we recommend using a pipe and filter type arcitecture to control the launch sequence. This architecture pattern was selected because of its sequential nature. As different user interactions take place with the system, this architecture ensures operations only move forward at the appropriate timing (ie LAUNCH cannot be pressed prior to TEST). This architecture is also simple to diagnose and debug and fits with the low complexity nature of the system. For example, if an error condition is met, we simply branch off to some common failure state because an error should probably restart the sequence anyway for safety. 

Additionally, we selected a client/server architecture for the Control Unit/Launchpad Unit system. The Control Unit would be the client, with minimal logic happening here. This ensures that the logic really takes place on the launch pad. This centrality makes sure the most critical element, the igniter control system, also houses the most information about system status. The control unit then becomes an easy interface telling the user where the launch sequence is at. Since there should only be one control unit, the "server" should only be doing minimal processing. Interactions can then use ordinary network type protocols like TCP to ensure delivery of information and ensure both systems have the same status (ie the READY light is actually turned on when the launchpad is in the ready state). 

## Status
Proposed

## Consequences

This will affect the safety of the Rocket Engineers as they test their rockets.

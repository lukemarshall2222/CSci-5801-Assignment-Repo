# RLS Proposed Decision

## Context

The rocket engineers want to ensure safety even in the face of partial failures. The system requirements communicate this need through a series of steps that must occur to test the launch system, enable the control unit, and use the control unit to launch the rocket. These steps are implemented using some method of communication.

## Decision

The method of communication in the system will be basic radio signals. The sequence of signals between the control unit and launch pad can be easily implemented using simple radio signals that are linked to actions such as enabling, turning on lights, and sending response signals. Radio is also inexpensive and can be used over long ranges, enabling a safe distance between rocket and engineer before takeoff. 

## Status
Proposed

## Consequences

The engineers will be able to get farther away from the launch site, increasing safety, and the launch sequence will be able to be facilitated using the signals, meeting the requirements; while also keeping costs low. 

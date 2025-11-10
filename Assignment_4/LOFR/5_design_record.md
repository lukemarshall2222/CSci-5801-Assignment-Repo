# Logfile Analysis Framework Solution doc

## Context

The system engineers who work on safety critical systems need good ways to go through their data. At the moment, testing is expensive, and the manufacturers want cheaper testing scenarios. There is also the problem of the complexity of analysis, and how error prone the analysis can be.

## Decision

We will build a consistent logfile format such that we can make queries and look through the data efficiently.

- For the logging system, we will use a buffered memory solution default with selectable direct-write to disk as an option. This option is ideal for its high access speed, limiting overhead introduced from constant IO operations.
- Logging will be default configured to default to compressed logs in interactive mode and uncompressed in batch mode. The program must be usable on laptops and workstations, so the program must be able to work with limited storage volumes and memory sizes. In batch mode, however, the assumption is a server-type system testing many systems at once, so speed is much preferred. Memory is assumed to be more plentiful and storage more accessible. 

## Status

Proposed

## Consequences

Data Analysis will become cheaper and easier. The engineers will also have to learn our new format, which could take some time.

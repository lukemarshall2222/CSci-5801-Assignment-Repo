### Proposed Solution

- For the log storage, we will use a buffered memory solution default with selectable direct-write to disk as an option. 
    - This option is ideal for its high access speed, limiting overhead introduced from constant IO operations.
    - Logging will be default configured to compressed logs in interactive mode and uncompressed in batch mode. 
    - The program must be usable on laptops and workstations, so the program must be able to work with limited storage volumes and memory sizes. 
    - In batch mode, however, the assumption is a server-type system testing many systems at once, so speed is much preferred. 
        - Memory is assumed to be more plentiful and storage more accessible beccause of this setup. 
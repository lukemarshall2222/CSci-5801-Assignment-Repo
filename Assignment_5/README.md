# User Manual
Change the current directory in your terminal to the one containing the project file.

## Required Dependencies
- Python 3.10 or higher
- If you want to run the tests: Python libraries `pytest` and `pytestcov`. 
    - To install: `pip install pytest pytest-cov` 

## System Execution

- Enter the command awith argument `python rls_source.py` (possibly `python3 rls_source.py`) 
    - Add the following flags if you want to set something to false.
#### Flags
- `--battery_charged`: Make it so that the battery isn't charged
- `--circuit_closed`: Make it so that the circuit isn't closed
- `--communication_enabled`: Communication is not enabled?
- `--ready_to_launch`: The rocket will not be ready to launch
- `--launch`: The rocket will not launch
    args = parser.parse_args()
    main()

## Running Tests

- Change the executable permisions on the bash script `test.sh` so that it may be executed i.e. `chmod +x run_tests.sh`.
- Run the `test.sh` bash script, i.e. `./test.sh`. It will first ask for a name, give it yours or any other.
    - The script will then complete the tests in the `tests.py` file.   
- After the tests are complete, the script will log the output and the name given to the `test_log.txt` log file. 

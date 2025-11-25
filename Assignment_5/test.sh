#!/bin/bash

# run_tests.sh - Run pytest with coverage and log results

# Ask for user's name
read -p "Enter your name: " username

# Run pytest and capture output
timestamp=$(date "+%Y-%m-%d %H:%M:%S")
test_output=$(pytest tests.py -v --cov=rls_source --cov-report=term-missing --cov-branch 2>&1)
# Write to test_log.txt (append if exists)
{
    echo "Tests completed by $username"
    echo "Tests completed at $timestamp"
    echo "$test_output"
    echo ""
    echo "Tests necessary to demonstrate that the acceptance criteria in our user stories have been satisfied:
            Redundancy in the launch controls is demonstrated by the button press behavior being determined by not only the user input 
            but also the initial configuraed state of the launch pad and control unit. These are demonstraited in the TestButtonPress
            and TestSystem tests.

            Appropriate sequential progression based on result of previous step is determined in context of the correct behavior at some 
            point in a sequence. This is demonstraited in the TestSystem tests."
    echo "----------------------------------------"
    echo ""
} >> test_log.txt

# Display results to terminal
echo "$test_output"
echo ""
echo "Results appended to test_log.txt"
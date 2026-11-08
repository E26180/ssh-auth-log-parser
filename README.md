# Project 2 – SSH Authentication Log Parser

## Overview
A Python mini-project that analyses SSH authentication logs to identify failed login attempts and their source IP addresses.

## Features
- Count failed SSH password attempts
- Extract source IPv4 addresses using regular expressions
- Count attempts per IP address
- Rank IP addresses by attempt count
- Accept a log file path as a command-line argument
- Handle missing or unreadable log files

## Technologies
- Python 3
- re
- pathlib
- collections.Counter
- sys

## Usage
python3 parser.py sample_auth.log

## Example Output
Total failed attempts: 5

Failed attempts by IP:
192.0.2.10: 3 attempts
198.51.100.23: 2 attempts

## Error Handling
- Missing argument: displays a usage message
- Invalid file path: displays a file-reading error

## Security Notes
Uses synthetic SSH logs for testing. Never publish private authentication logs containing sensitive information.

The current regex targets common IPv4 SSH log entries and does not perform full IP address validation.

## Learning Outcomes
- Python file handling
- Regular expressions
- Command-line arguments
- Error handling
- SSH log analysis
- Basic security monitoring

## Limitations
This project is a basic SSH log analysis utility, not an advanced intrusion detection system.

The parser currently detects failed SSH password attempts and extracts IPv4 addresses from common log formats. It does not detect all attack types or support every SSH log format.

## Validation
Tested using synthetic SSH logs and two anonymised entries derived from a real Ubuntu VM journal.

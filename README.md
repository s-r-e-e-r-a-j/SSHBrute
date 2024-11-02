# SSHBrute

SSHBrute is a command-line tool for performing brute-force attacks on SSH servers using specified username and password wordlists. This tool is intended for ethical hacking and penetration testing in controlled environments where you have explicit permission to test.

## Disclaimer

**WARNING**: This tool should only be used on systems that you own or have explicit permission to test. Unauthorized access to computer systems is illegal and unethical.

## Features

- Brute-forces SSH login attempts using combinations of usernames and passwords from wordlists.
- Supports separate wordlists for usernames and passwords.
- Displays attempts and successful logins in the command line.

## Requirements

- Python 3.x
- `paramiko` library

You can install the required library using pip:

```bash
pip install paramiko

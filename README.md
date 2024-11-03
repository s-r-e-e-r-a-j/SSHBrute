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

`paramiko` is pre-installed in kalilinux so don't need to install it on kalilinux 

```bash
pip install paramiko
```
You can install requirements (optional if you are using kali linux):-

`In kali linux all requirements are pre-installed so don't need this on kali linux`

```bash
pip3 install -r requirements.txt
```

## Installation

1. Clone the repository or download the script

```bash
git clone https://github.com/s-r-e-e-r-a-j/SSHBRUTE-TOOL.git
```
```bash
cd SSHBRUTE-TOOL
```
```bash
cd SSHBrute
```
2. Ensure you have the required dependencies installed (as mentioned above)



## Usage

Run the tool from the command line with the following syntax:

```bash
python3 ssh_bruteforce.py <target_ip> <username_wordlist> <password_wordlist>
```

## Example

```bash
python3 ssh_bruteforce.py 192.168.1.100 usernames.txt passwords.txt
```

`target_ip`: The IP address of the SSH server you want to 
test.

`username_wordlist`: Path to the text file containing usernames (one per line).

`password_wordlist`: Path to the text file containing passwords (one per line)


## Output

The tool will display each username/password combination it attempts and indicate if a login was successful.

```bash
Trying username: admin, password: 123456
Success! Username: admin, Password: 123456
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

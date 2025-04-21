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

## Installation

1. Clone the repository or download the script

```bash
git clone https://github.com/s-r-e-e-r-a-j/SSHBrute.git
```
2. Navigate to the SSHBrute directory
```bash
cd SSHBrute
```
3. Install required libraries 

```bash
pip3 install -r requirements.txt
```
4. Navigate to the SSHBrute directory
   
```bash
cd SSHBrute
```



## Usage

Run the tool from the command line with the following syntax:

```bash
python3 sshbrute.py <target_ip> <target_port> <username_wordlist> <password_wordlist>
```

## Example

```bash
python3 sshbrute.py 192.168.1.100 22 usernames.txt passwords.txt
```

`target_ip`: The IP address of the SSH server you want to 
test.

`target_port`: The port number of the SSH server (default is usually 22)


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

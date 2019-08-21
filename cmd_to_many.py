# issue a command to multiple devices
# devices are listed in a text file named "hosts.txt"
# output written to text file named "output.txt"

from __future__ import print_function, unicode_literals
from netmiko import ConnectHandler
from datetime import datetime
import getpass

# login function
def login():

    with open("hosts.txt", "r") as f:
        ipaddr = f.read().splitlines()
    f.close()

    #uname = getpass.getuser() #uncomment to read username from Windows...commented out for GNS3 testing
    uname = input('username:')
    passwd = getpass.getpass(prompt='password: ', stream=None)

    return ipaddr,uname,passwd

# function to input and issue command
def cmd():

    file = open('output.txt', 'w')

    hostfile,uname,passwd = login()\
    
    command = input("Enter Global Config Command:")

    for ipaddr in hostfile:
        device = {
            "device_type": "cisco_ios",
            "ip": ipaddr.strip(),
            "username": uname.strip(),
            "password": passwd.strip(),
        }

        try:
            net_connect = ConnectHandler(**device)

        except Exception:
            print("** Failed to connect.", end="", flush=True)
            continue

        output = net_connect.send_command(command)

        print("\n")
        print("#" * 80)
        print(output)
        print("#" * 80) 
        print("\n")

        file.write(output)

    file.close()

# main starts script run timer
def main():

    start_time = datetime.now()

    cmd()

    end_time = datetime.now()

    print("Script Run Time: {}".format(end_time - start_time))
    print("\n")

main()
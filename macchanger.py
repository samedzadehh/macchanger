import subprocess
import re
import random
import os

if os.geteuid() == 0:
    pass
else:
    print("     You are not root(\n     Please try again  ")
    exit()
print("\033[1m\033[31mMAC CHANGER\033[31m")



interface=input("Interface: ")
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)
    
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        return None

current_mac = get_current_mac(interface)
if current_mac:
    print("        Current MAC  " + current_mac)
else:
    print("MAC not found")
    

def macchange(mac):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])


print("How to change mac address?\n1.Random\n2.Given")
choice=input("choice: ")
if choice=="1":
    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    mac=str("00")
    d=10
    while d!=0:
        b=random.choice(characters)
        mac+=b
        d-=1
    c=2
    e=5
    while e!=0:
        mac=mac[:c]+":"+mac[c:]
        c+=3
        e-=1
    macchange(mac)
elif choice=="2":
    mac=input("New Mac: ")
    macchange(mac)
else:
    print("Choice not found")
    

print("MAC adress successfully changed")
print("Old mac ",current_mac)
print("New mac",mac)
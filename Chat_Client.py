import socket
import time

oUserDict = {}

userInf = open("userInf.txt","r")
username = userInf.read()
userInf.close()

onlineUsers = open("users.txt","r")

for line in onlineUsers:
    (key,value) = line.split()
    oUserDict[key] = value  #oUserDict = {"Ata":"192.168.0.26"}

onlineUsers.close()

print("Online Users:"+"\n")
for key,value in oUserDict.items():
    if key != username:
       print(key + " -> " + value)

print("\n")

tryAgain = True
port = 5001

while(tryAgain):
     try:
        nickPick = input("Choose a user to chat : ")
        if nickPick != username:
           ip = oUserDict[nickPick]
           tryAgain = False
        else:
           print("Please don't choose yourself.")
     except KeyError:
         print("There is no online user with name : " + nickPick + ".")

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((ip, port))
    except socket.timeout:
        print("Connection Timeout")
        time.sleep(2)
        exit()

    except ConnectionRefusedError:
        print(nickPick + " is offline.")
        time.sleep(2)
        exit()

    message = input(username + " >> ")

    #Ata >> asıdljfasf

    try:
        s.send(bytes(username + " >> " + message, "utf-8"))
        s.close()
    except ConnectionResetError:
        print("Couldn't deliver the message.Trying again.")
        time.sleep(1)









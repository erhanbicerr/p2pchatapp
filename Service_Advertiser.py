import socket
import json
import time

username = input("Username : ")

userInf = open("userInf.txt","w")
userInf.write(username)
userInf.close()

IP = socket.gethostbyname(socket.gethostname())
broadcastIP = "" #Sonu 255li IP
PORT = 5000
print(IP)
dotcount = 0
#192.168.0.26
#IP sonuna 255 ekliyoruz burada (Tabi yeni bir değişkene atıyoruz bunu)

for i in range(len(IP)):
    if IP[i] == ".":
        dotcount += 1
    if dotcount < 3:
        broadcastIP += IP[i]
    elif dotcount == 3:
        broadcastIP += IP[i] + "255"
        break

print(broadcastIP)

ex = {"username": username, "ip_address": IP}

jsonEx = json.dumps(ex)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr = (broadcastIP,PORT)

while 1:
    s.sendto(bytes(jsonEx,"utf-8"), addr)
    for i in range(60):
       print(str(i))
       time.sleep(1)




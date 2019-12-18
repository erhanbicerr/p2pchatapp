import socket
import json

IP = socket.gethostbyname(socket.gethostname())
PORT = 5000
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((IP, PORT))
userDict = {}
while 1:
     jsonMsg,ip_port = s.recvfrom(2048)
     jsonDict = json.loads(jsonMsg.decode("utf-8")) #jsonDict = {"username": username, "ip_address": IP}
     userDict[jsonDict["username"]] = ip_port[0] #(192.168.0.29,5000) #userDict = {"Erdem":192.168.0.29,"Atahan":192.168.0.25}
     onlineUsers = open("users.txt", "w+")
     for key,value in userDict.items():
         onlineUsers.write(key+" "+value+"\n") #Erdem 192.168.0.29
         #Atahan 192.168.0.25
     onlineUsers.close()


     print(str(userDict))




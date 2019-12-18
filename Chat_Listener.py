import socket
import time

userInf = open("userInf.txt","r")
username = userInf.read()
userInf.close()

port = 5001
ip = socket.gethostbyname(socket.gethostname())

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((ip,port))
s.listen(5)

chatLog = open("chatlog.txt","w")
chatLog.write("")
chatLog.close()

s.settimeout(5) #Süre random
firstAccept = False

while True:

    while True:
      try:
          clientSocket, addr = s.accept()

          if firstAccept == False:
              firstAccept = True

          incoming_msg = clientSocket.recv(1024)
          break

      except socket.timeout:
          print("TCP Connection Request Timeout.")
          if(firstAccept == False):
             print("Waiting for a new TCP Connection Request.")
             continue
          else:
             time.sleep(2)
             exit()

      except ConnectionResetError:
          print("Chat_Client is closed.")
          time.sleep(2)
          exit()


    localtime = time.asctime(time.localtime(time.time()))

    with open("chatlog.txt","a") as chatLog:
         chatLog.write(incoming_msg.decode("utf-8") + " -> " + localtime + "\n")

    print(incoming_msg.decode("utf-8"))




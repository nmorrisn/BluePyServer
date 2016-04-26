import socket
import subprocess
from Modules.buildobject import basicobject
''

hostMACAddress = '00:19:86:00:21:E5' #address of Pi
port = 1 #default port
backlog = 1
size = 1024

s = None
while s is None: #continuously try to open socket until it succeeds
    try:
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    except OSError as msg:
        s = None
        print(msg)
        continue
    try:
        s.bind((hostMACAddress,port))
        s.listen(backlog)
    except OSError as msg:
        s.close()
        print(msg)
        s = None
        continue

try:
    print("Waiting for connection on RFCOMM channel %d" % port)
    
    client, address = s.accept()


    print("Accepted connection from ", address)
    print("Beginning testing...")
    while 1:
        data = client.recv(size)
        doObject = basicobject()
        print(data)
        if data == b'disconnect':
            data = doObject.disconnect(s,client)
        if data == b'glucose':
            data = doObject.getGluc()
        if data == b'getbp':
            data = doObject.getBP()
        client.send(data)
        
except:
    print("Closing socket")
    client.close()
    s.close()

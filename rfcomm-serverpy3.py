import socket
import subprocess
import RPi.GPIO as GPIO
''

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17,False)

hostMACAddress = '00:19:86:00:21:E5'
port = 1
backlog = 1
size = 1024

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)

try:
    print("Waiting for connection on RFCOMM channel %d" % port)
    
    client, address = s.accept()

    print("Accepted connection from ", address)
    print("Beginning testing...")
    while 1:
        data = client.recv(size)
        if data == b'1':
            GPIO.output(17,True)
            data = b'Light is on!'
            print("Light is on!")
        if data == b'2':
            GPIO.output(17,False)
            data = b'Light is off!'
            print("Light is off!")
        if data == b'3':
            data = b'Connection terminated by user'
            print("Connection terminated by user")
            client.send(data)
            client.close()
            s.close()
        client.send(data)
        
except:
    print("Closing socket")
    GPIO.output(17,False)
    client.close()
    s.close()

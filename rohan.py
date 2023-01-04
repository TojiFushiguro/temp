# Client.py

import socket
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.output(8,GPIO.LOW)
s = socket.socket()
port = 8787
s.connect(('192.168.21.232', port))
print (s.recv(1024).decode())
while True:
    if s.recv(1024).decode()=='1':
        print('intruder detected')
        GPIO.output(8,GPIO.HIGH)
        sleep(10)
    else:
        GPIO.output(8,GPIO.LOW)
        print('intruder not detected')
        s.close()

# Server.py
# pip install RPi.GPIO

import socket
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN)
s = socket.socket()
print ("Socket successfully created")
port = 8787
s.bind(('', port))
print ("socket binded to %s" %(port))

s.listen(5)
print ("socket is listening")
while True:
c, addr = s.accept()
print ('Got connection from', addr )
c.send('Thank you for connecting'.encode())
while True:
if GPIO.input(7):
c.send("1".encode())
print("INtruder DEtected")
else:
c.send("0".encode())
print("No INtruder")
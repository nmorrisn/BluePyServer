import socket
import subprocess
import RPi.GPIO as GPIO

from Modules.glucObject import glucObject

class basicobject:

    def GPIO_on(self):
        GPIO.output(17,True)
        data = b'Light is on!'
        print("Light is on!")
        return data

    def GPIO_off(self):
        GPIO.output(17,False)
        data = b'Light is off!'
        print("Light is off!")
        return data

    def disconnect(self,s,client):
        data = b'Connection terminated by user'
        print("Connection terminated by user")
        client.send(data)
        client.close()
        s.close()
        return data

    def getGluc(self):
        getGlucObj = glucObject()
        #data = b'Getting values from Glucometer'
        print("Getting values from Glucometer")
        #client.send(data)
        glucResults = getGlucObj.getResults()
        print(glucResults)
        return glucResults
        
        
    

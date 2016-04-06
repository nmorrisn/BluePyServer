import socket
import subprocess
import RPi.GPIO as GPIO

from Modules.glucObject import glucObject

class basicobject:

    def disconnect(self,s,client):
        data = b'Connection terminated by user'
        print("Connection terminated by user")
        client.send(data)
        client.close()
        s.close()
        return data

    def getGluc(self):
        getGlucObj = glucObject()
        print("Getting values from Glucometer")
        glucResults = getGlucObj.getResults()
        print("Glucometer results: %d",glucResults)
        return glucResults
        
        
    

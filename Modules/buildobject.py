import socket
import subprocess

from Modules.glucObject import glucObject
from Modules.bpObject import bpObject

class basicobject:

    def disconnect(self,s,client):
        print("Connection terminated by user")
        client.close()
        s.close()
        return data

    def getGluc(self):
        getGlucObj = glucObject()
        print("Getting values from Glucometer")
        glucResults = getGlucObj.getResults()
        print("Glucometer results: ",glucResults)
        return glucResults

    def getBP(self):
        getBPObj = bpObject()
        print("Getting values from Blood Pressure Monitor")
        bpResults = getBPObj.getResults()
        print("Blood Pressure results: ",bpResults)
        return bpResults
        
        
    

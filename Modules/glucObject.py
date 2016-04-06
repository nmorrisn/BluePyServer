import subprocess
import os.path

from Modules.getJSONObject import getJSONObject

class glucObject:

    def getResults(self):
        pathtoResults = '/home/pi/Desktop'
        nameofFile = 'glucResults.txt'

        completeName = os.path.join(pathtoResults, nameofFile)
        f = open(completeName, "r")
        glucResults = f.readline()
        f.close()
        glucResults = str.encode(glucResults)
        return glucResults
        
        

import subprocess
import os.path

class glucObject:

    def getResults(self):
        pathtoResults = '/home/pi/eHealth_raspberrypi_v2.4'
        nameofFile = 'glu.txt'

        completeName = os.path.join(pathtoResults, nameofFile)
        f = open(completeName, "r")
        glucResults = f.readline()
        f.close()
        glucResults = str.encode(glucResults)
        return glucResults
        
        

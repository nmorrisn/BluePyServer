import subprocess
import os.path

class glucObject:

    def getResults(self):
        pathtoResults = '/home/pi/bluepyenv/BluePyServer'
        pathtoexe = '/home/pi/bluepyenv/eHealth_raspberrypi_v2.4'
        filename = "glucode"
        completepathtoexe = os.path.join(pathtoexe,filename)
        nameofFile = 'glu.txt'
        proc = subprocess.call('sudo /home/pi/bluepyenv/eHealth_raspberrypi_v2.4/glucode',shell=True)
        completeName = os.path.join(pathtoResults, nameofFile)
        f = open(completeName, "r")
        glucResults = f.readline()
        f.close()
        glucResults = str.encode(glucResults)
        return glucResults
        
        

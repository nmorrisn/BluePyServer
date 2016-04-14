import subprocess
import os.path
import array


class bpObject:

    def getResults(self):
        pathtoResults = '/home/pi/bluepyenv/BluePyServer'
        pathtoexe = '/home/pi/bluepyenv/eHealth_raspberrypi_v2.4'
        filename = "bpcode"
        nameofFile = 'bp.txt'
        proc = subprocess.call('sudo /home/pi/bluepyenv/eHealth_raspberrypi_v2.4/bpcode',shell=True)
        completeName = os.path.join(pathtoResults, nameofFile)
        f = open(completeName, "r")
        bpResults = f.readline()
        f.close()
        bpResults = str.encode(bpResults)
        return bpResults

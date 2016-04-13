import subprocess
import os.path
import array


class bpObject:

    def getResults(self):
        pathtoResults = '/home/pi/eHealth_raspberrypi_v2.4'
        nameofFile = 'bp.txt'
        completeName = os.path.join(pathtoResults, nameofFile)
        f = open(completeName, "r")
        bpResults = f.readline()
        f.close()
        bpResults = str.encode(bpResults)
        return bpResults

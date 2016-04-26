import subprocess
import os.path

class glucObject:

    def getResults(self):
        pathtoResults = '/home/pi/bluepyenv/BluePyServer'
        nameofFile = 'glu.txt'
        completeName = os.path.join(pathtoResults, nameofFile)
        
        try:
            proc = subprocess.call('sudo /home/pi/bluepyenv/eHealth_raspberrypi_v2.4/glucode',shell=True)
        except OSError as msg:
            print ("OSError({0}): {1}".format(msg.errno, msg.strerror))
        except:
            print ("Unexpected error:", sys.exc_info()[0])
            raise
        
        try:
            f = open(completeName, "r")
            glucResults = f.readline()
        except IOError as e:
            print ("I/O error({0}): {1}".format(e.errno, e.strerror))
        except:
            print ("Unexpected error:", sys.exc_info()[0])
            raise
        else:
            f.close()
        
        glucResults = str.encode(glucResults)
        return glucResults
        
        

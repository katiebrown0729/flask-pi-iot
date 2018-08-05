# Mock Pi file

import requests
import time
import datetime
import random
import math

class DataPoster():

    def __init__(self):
        self._validServers = []
        self._invalidServers = []
        self._serverList = ['http://megan-pi-iot.cfapps.io/test',
                     'http://katie-pi-iot.cfapps.io/test',
                    'http://david-pi-iot.cfapps.io/test',
                    'http://jpf-flask-pi-iot.cfapps.io/test',
                    'http://shane-flask-pi-iot.cfapps.io/test']

    def getserial(self):
        # Extract serial from cpuinfo file
        cpuserial = "0000000000000000"
        try:
            f = open('/proc/cpuinfo', 'r')
            for line in f:
                if line[0:6] == 'Serial':
                    cpuserial = line[10:26]
            f.close()
        except:
            cpuserial = "KATIE000000000"

        return cpuserial

    def get_ServerList(self):
        return self._serverList

    def get_valid_servers(self, sl):
        for server in sl:
            r = requests.get(server)
            if r.status_code != 200:
                self._invalidServers.append(server)
                # print('Added {} to INVALID server list' .format(server))
            else:
                self._validServers.append(server)
                # print('Added {} to VALID server list'.format(server))
        return(self._validServers)

    def accel_read(self):
        x = random.randrange(0, 10, 1)
        y = random.randrange(0, 10, 1)
        z = random.randrange(0, 10, 1)
        return (x, y, z)

    def post_to_valid_servers(self, aData: object) -> object:
        self.get_valid_servers(self.get_ServerList())
        n = 0
        for server in self._validServers:
            print("Sending to server {}".format(server))
            r = requests.post(server, data = aData)
            if r.status_code != 200:
                print("server: {} returned error code: {}".format(server, r.status_code))
            else:
                n = n + 1
        return n

    def get_aData(self):
        x, y, z = self.accel_read()
        print('X={0}, Y={1}, Z={2}'.format(x, y, z))
        ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        myserial = self.getserial()
        aData = {'serial-no': myserial, 'timestamp': ts, 'x': x, 'y': y, 'z': z}
        return (aData)


if __name__ == '__main__':
    dP = DataPoster()

    oldtime = time.time()

    while True:
        dP.post_to_valid_servers(dP.get_aData())
        newtime = math.floor(time.time())

        if 10 >= newtime - oldtime:
            print("Refreshing server list...")
            dP.get_valid_servers(dP.get_ServerList())
            oldtime = time.time()





        #todo make check for valid servers periodically
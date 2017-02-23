#!/usr/bin/env python
from utils import dbWrite, eventConnector, eventWriter,eventDeconnect
import requests
from models import *

connection, channel = eventConnector()

data = [
    {
        "measurement": "httpLogs",
        "tags": {
            "url": "localhost",
            "monitor": "name",
            "user"   : "test"
        },
        "fields": {
		    "status" : "ok",
        }
    }
]

def checkHTTP(url, name, user):

    data[0]["tags"]["url"]     = url
    data[0]["tags"]["monitor"] = name
    data[0]["tags"]["user"]    = user
    try:
        r = requests.get('http://'+url)
        if r.status_code == requests.codes.ok:
            # log in influxdb
            dbWrite(data=data)
    except requests.ConnectionError, e:
        # log in influxdb
        data[0]["fields"]["status"] = "ko"
        dbWrite(data=data)
        eventWriter(channel, data)

if __name__ == '__main__':

    monitor = Monitors.objects()

    for mon in monitor:
        mon.user = 'test'
        if mon.url and mon.name and mon.user :
            checkHTTP(mon.url, mon.name, mon.user)
        else:
            print "missing fields"
    eventDeconnect(connection)

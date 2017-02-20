#!/usr/bin/env python
import pika
import logger
import requests
from models import *

# connect to rappitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='alerts')

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
            logger.write(data=data)
    except requests.ConnectionError, e:
        # log in influxdb
        data[0]["fields"]["status"] = "ko"
        logger.write(data=data)
        channel.basic_publish(exchange='',
                              routing_key='alerts',
                              body='test alert')
        print(" [x] Sent 'Alert message'")

monitor = Monitors.objects()

for mon in monitor:
    mon.user = 'test'
    if mon.url and mon.name and mon.user :
        checkHTTP(mon.url, mon.name, mon.user)
    else:
        print "missing fields"

connection.close()

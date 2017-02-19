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
            "region": "tunisia"
            "user"   : "test"
        },
        "fields": {
		    "status" : "ok",
        }
    }
]

def checkHTTP(url):
    try:
        r = requests.get(url)
    except requests.ConnectionError, e:
        raise e
    if r.status_code == requests.codes.ok:
        # log in influxdb
        logger.write(data=data)
    else:
        # log in influxdb
        data[0]["fields"]["status"] = "ko"
        logger.write(data=data)
        channel.basic_publish(exchange='',
                              routing_key='alerts',
                              body='test alert')
        print(" [x] Sent 'Alert message'")


monitor = Monitors.objects()

for mon in monitor:
    if mon.url:
        checkHTTP(mon.url)
    else:
        print "no url"

connection.close()

#!/usr/bin/env python
import pika
import requests
from models import *

# connect to rappitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='httpWorker')


def get_status_code(url):
    try:
        r = requests.get(url)
    except requests.ConnectionError, e:
        raise e
    if r.status_code == requests.codes.ok:
        return 'OK'
    else:
        channel.basic_publish(exchange='',
                              routing_key='httpWorker',
                              body='test alert')
        print(" [x] Sent 'Alert message'")
        return 'KO'


monitor = Monitors.objects()

for mon in monitor:
    if mon.url:
        print get_status_code(mon.url)
    else:
        print "no url"

connection.close()

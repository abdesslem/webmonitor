#!/usr/bin/env python
import pika
import json
import logging

file_handler = logging.FileHandler('alerts.log')

def callback(ch, method, properties, body):
    data = json.loads(body)
    print data[0]['measurement']
    print data[0]['fields']
    print "user"       + data[0]['tags']['user']
    print "monitor"    + data[0]['tags']['monitor']

def alertListner():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='alerts')


    channel.basic_consume(callback,
                          queue='alerts',
                          no_ack=True)

    logging.debug(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

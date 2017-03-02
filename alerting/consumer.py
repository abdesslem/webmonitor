#!/usr/bin/env python
import pika
import json

def callback(ch, method, properties, body):
    print("Method: {}".format(method))
    print("Properties: {}".format(properties))
    data = json.loads(body)
    print data
    #print("measurement: {}".format(data['measurement']))
    #print("fields: {}".format(data['fields']))
    #print('tags: {}'.format(data['tags']))

def alertListner():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='alerts')


    channel.basic_consume(callback,
                          queue='alerts',
                          no_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

import pika
import json

def eventConnector():
    # connect to rappitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters(
	host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='alerts')
    return connection, channel

def eventWriter(channel, data):
    message = json.dumps(data)
    channel.basic_publish(exchange='',
                          routing_key='alerts',
                          body=message)
    print(" [x] Sent 'Alert message'")

def eventDeconnect(connection):
    connection.close()

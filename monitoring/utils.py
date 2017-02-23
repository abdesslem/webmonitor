from influxdb import InfluxDBClient
import pika
import json

def dbWrite(host='localhost', port=8086 , data=[]):
    user = 'root'
    password = 'root'
    dbname = 'monitors'
    dbuser = 'admin'
    dbuser_password = 'admin_password'
    client = InfluxDBClient(host, port, user, password, dbname)
    client.create_database(dbname)
    client.write_points(data)

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

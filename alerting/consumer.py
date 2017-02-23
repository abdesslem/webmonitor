#!/usr/bin/env python
import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


if __name__ == '__main__':

    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='alerts')


    channel.basic_consume(callback,
                          queue='alerts',
                          no_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


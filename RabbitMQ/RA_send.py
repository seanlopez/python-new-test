import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue="myQ")

channel.basic_publish(exchange='',
                      routing_key='myQ',
                      body="Hello world")


connection.close()

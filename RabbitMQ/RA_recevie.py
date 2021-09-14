import pika


connection= pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare(queue="myQ")

def callback(ch, method, properties, body):
    print("----- Received message is (%s) -----"%body)
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback,
                      queue="myQ",
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

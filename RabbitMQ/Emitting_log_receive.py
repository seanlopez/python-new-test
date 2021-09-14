import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

result = channel.queue_declare(exclusive=True)

queue_name = result.method.queue

channel.queue_bind(exchange="direct_logs",
                   queue=queue_name,
                   routing_key='error')

def callback(ch, method, properties, body):
    print("----- Received message is (%s) -----"%body.decode())


channel.basic_consume(callback,
                      queue = queue_name,
                      no_ack = True)   #

channel.start_consuming()

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="direct_logs",
                         exchange_type="direct")

channel.basic_publish(exchange="direct_logs",
                      routing_key="error",
                      body="this is error log")

connection.close()

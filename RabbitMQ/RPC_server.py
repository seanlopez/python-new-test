import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')   #创建一个Q，使用这个Q去接受client发来的请求

def judge_ou(n):
    if n % 2 == 0:
        return True
    else:
        return False

def on_request(ch, method, props, body):
    num = int(body)
    print("the receive num is %s"%num)

    rece = judge_ou(num)

    ch.basic_publish(exchange="",
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(rece))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')    #建立一个可以回执的consume

print(" [x] Awaiting RPC requests")
channel.start_consuming()

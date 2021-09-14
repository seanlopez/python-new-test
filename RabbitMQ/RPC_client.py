import pika
import uuid


class judge_ou_client:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, #接收到了消息，交给on_response这个callback函数执行
                                   no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self,n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,    #之前定义好的callback q
                                       correlation_id=self.corr_id),     #发出去的时候加上corr_id
                                   body=str(n))
        while self.response is None:        #当回复为空，则循环继续
            self.connection.process_data_events()     #设置继续等待
        return self.response

RPC_start = judge_ou_client()

print("sent 31 to server")
response = RPC_start.call(31)
if response.decode() == False:
    print("this is a ji num")
else:
    print("this is a ou num")


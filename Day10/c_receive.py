#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

"""
消息队列接收端
"""

import pika

# 建立 socket 对象
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# 建立管道对象
channel = connection.channel()

# 声明一个 queue, 由于服务端和接收端并不知道哪边先启动，所以在两边都声明一个 queue
channel.queue_declare(queue='hello', durable=True)

def callback(ch, method, properties, body):
    print("-->", ch, method, properties)
    print("[X] received: %s" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag) # 队列处理结束，返回应答

channel.basic_consume(callback,
                      queue='hello',
                      #no_ack=True  # 默认不需要， 为 接收端是否需要应答，这里为不需要应答
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')

# 接收消息队列
channel.start_consuming()
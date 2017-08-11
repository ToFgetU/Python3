#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange="logs", type="fanout")

result = channel.queue_declare(exclusive=True) # 不指定queue,随机生成queue
queue_name = result.method.queue

# 绑定queue
channel.queue_bind(exchange='logs',
                   queue=queue_name)

print("[*] Waiting for logs.")

def callback(ch, method, properties, body):
    print("[x] Received : %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
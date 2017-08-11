#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import pika
import time

# 建立socket
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# 创建管道
channel = connection.channel()

#申明queue
# queue = channel.queue_declare(queue='task_queue1')

def callback(ch, method, properties, body):
    print(ch, method, properties, body)
    print("[x] Received %r" % body)
    time.sleep(10)
    print("[x] Done")
    print("method.delivery_tag", method.delivery_tag)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback,
                      queue='task_queue1')

print("[*] Waiting for messages.")
channel.start_consuming()

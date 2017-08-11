#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import pika
import time

# 建立socket
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# 创建管道
channel = connection.channel()

# 申明queue, durable=True 队列持久化
queue = channel.queue_declare(queue='task_queue1', durable=True)

message = "Hello World! %s" % time.time()
channel.basic_publish(exchange='',
                      routing_key='task_queue1',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2 # 消息持久化
                      ))
print("[x] Sent %r" % message) # %r 给字符串加了单引号
connection.close()

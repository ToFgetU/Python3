#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import pika

# 建立socket
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# 建立管道
channel = connection.channel()

# 声明queue
queue = channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World')

print("[x] Send 'Hello World'")
connection.close()
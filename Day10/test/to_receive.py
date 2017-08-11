#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

queue = channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(ch, method, properties)
    print("[x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello')

print("[*] Waiting for messages.")

#开始监听服务端
channel.start_consuming()
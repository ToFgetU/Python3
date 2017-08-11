#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

# 设置为广播模式
channel.exchange_declare(exchange='logs',
                         type='fanout')

message = "Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print("[x] Sent %r" % message)
connection.close()
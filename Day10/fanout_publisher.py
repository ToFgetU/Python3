#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"

change = channel.basic_publish(exchange='logs',
                               routing_key='', # 广播不需要设置消息队列，默认全部发送
                               body=message)

print(" [x] Sent %r" % message)
connection.close()
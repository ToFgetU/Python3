#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu
"""
消息队列发送端
"""
import pika

# 建立 socket 对象
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# 建立管道对象
channel = connection.channel()

# 声明一个queue   durable=True 为队列持久化
channel.queue_declare(queue='hello', durable=True)

channel.basic_publish(exchange='',
                      routing_key='hello',  # 消息队列（queue）的名称
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2, # 消息持久化
                      ))  # 发送的消息内容

print("[X] Sent 'Hello World!'")
# 关闭连接
connection.close()




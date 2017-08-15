#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import pika

class client(object):
    '''客户端类'''
    def __init__(self, ip):
        # 创建socket实例
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=ip))
        # 创建管道
        self.channel = self.connection.channel()
        # 定义随机queue
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response,
                                   no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method ,properites, body):
        print(ch, method, properites, body)

    def call(self):
        pass

    def start(self):
        print()
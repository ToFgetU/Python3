#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import pika

class server(object):
    def __init__(self, ip, queue_name):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=ip))
        self.channel = self.connection.channel()
        self.channel.queue.declare(queue=self.queue_name)

    def handler(self, cmd):
        pass

    def on_request(self, ch, method, properites, body):
        cmd = body
        print(cmd)

    def start(self):
        self.channel.basic_consume(self.on_request, queue=self.queue_name)
        print('等待数据'.center(60, '='))
        self.channel.start_consuming()
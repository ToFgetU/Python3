#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import pika

class server(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='rpc_queue')

    def handler(self, cmd):
        pass

    def on_request(self, ch, method, properites, body):
        cmd = body.decode()
        print(cmd)
        cmd_list = cmd.split('"')
        _cmd = cmd_list[1].strip()
        print("-cmd:", _cmd)
        hosts = cmd_list[2].split()
        print(hosts)

    def start(self):
        self.channel.basic_consume(self.on_request, queue='rpc_queue')
        print('等待数据'.center(60, '='))
        self.channel.start_consuming()


if __name__ == '__main__':
    s = server()
    s.start()
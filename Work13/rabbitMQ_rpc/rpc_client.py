#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import pika
import random
import paramiko

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

class Hander(object):
    """
    用户执行类
    """
    info = {}
    def run(self, cmd):
        print("cmd:", cmd)
        cmd_list = cmd.split('"')
        print(cmd_list)
        _cmd = cmd_list[1]
        _host = cmd_list[2].split()
        print(_host)



    def check_task(self, cmd):
        print("I am check_task")

    def start(self):
        print("程序开始运行".center(50, "="))
        while True:
            task_id = random.randint(10000, 100000)
            while task_id in Hander.info:
                task_id = random.randint(10000, 100000)

            cmd = input(">>> ").strip()
            Hander.info[task_id] = cmd
            cmd_list = cmd.split(' ', 1)
            if hasattr(self, '%s' % cmd_list[0]):
                func = getattr(self, '%s' % cmd_list[0])
                func(cmd)
            else:
                print("""\033[32;1m输入的命令行有误, 命令格式如下：
        run \"df -Th\" --host 10.10.10.10
        check_task [check_id] （如：check_task 11111）\033[0m """)

if __name__ == '__main__':
    s = Hander()
    s.start()
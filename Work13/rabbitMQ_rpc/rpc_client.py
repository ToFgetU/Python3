#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import uuid
import time
import pika
import random
import paramiko
import threading

class Client(object):
    '''客户端类'''
    def __init__(self):
        # 创建socket实例
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        # 创建管道
        self.channel = self.connection.channel()
        # 定义随机queue
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response,
                                   no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method ,props, body):
        # print(ch, method, props, body)
        if self.callback_id == props.correlation_id:
            self.response = body
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def get_response(self, callback_queue, callback_id, task_id):
        self.callback_id = callback_id
        self.channel.basic_consume(self.on_response,
                                   queue=callback_queue)
        self.response = None
        while self.response is None:
            self.connection.process_data_events()
            # print(11)
        Hander.info[task_id] = self.response
        # return self.response

    def call(self, cmd):
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                  routing_key='rpc_queue',
                                  properties=pika.BasicProperties(reply_to=self.callback_queue,
                                                                  correlation_id=self.corr_id),
                                  body=str(cmd))
        return self.callback_queue, self.corr_id


class Hander(object):
    """
    用户执行类
    """
    info = {}
    def run(self, cmd):
        task_id = random.randint(10000, 100000)
        while task_id in Hander.info:
            task_id = random.randint(10000, 100000)
        # print("cmd:", cmd)
        cmd_list = cmd.split('"')
        # print(cmd_list)
        self.client = Client()
        response = self.client.call(cmd)
        Hander.info[task_id] = None
        print('task_id: ', task_id)
        self.client.get_response(response[0], response[1], task_id)


    def check_task(self, cmd):
        # print('cmd', cmd)
        cmd_list = cmd.split()
        # print(cmd_list)
        # print(Hander.info)
        task_id = int(cmd_list[1].strip())
        if task_id in Hander.info:
            result = Hander.info[task_id]
            if result is None:
                print("程序还在执行中 . . .")
            else:
                for key, vaule in eval(result).items():
                    print(key.center(40, '='))
                    print(vaule)
                del Hander.info[task_id]
        else:
            print("查找的 TASK_ID 不存在,或者已经查询过该ID，系统自动进行了清理")


    def start(self):
        print("程序开始运行".center(50, "="))
        p_list = []
        while True:
            cmd = input(">>> ").strip()
            if not cmd:
                continue
            cmd_list = cmd.split(' ', 1)
            if hasattr(self, '%s' % cmd_list[0]):
                func = getattr(self, '%s' % cmd_list[0])
                t1 = threading.Thread(target=func, args=(cmd,))
                t1.start()
                p_list.append(t1)
                time.sleep(0.5)
            else:
                print("""\033[32;1m输入的命令行有误, 命令格式如下：
        run \"df -Th\" --host 10.10.10.10
        check_task [check_id] （如：check_task 11111）\033[0m """)
        for r in p_list:
            r.join()

if __name__ == '__main__':
    s = Hander()
    s.start()
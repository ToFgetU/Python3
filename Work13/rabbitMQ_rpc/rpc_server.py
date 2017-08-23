#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import pika
import paramiko

class server(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='rpc_queue')

    def handler(self, cmd):
        cmd_list = cmd.split('"')
        _cmd = cmd_list[1].strip()
        print("-cmd:", _cmd)
        hosts = cmd_list[2].split()
        print(hosts)
        response = {}
        for host in hosts:
            ssh = SSHClients('root', '123456', host)
            ssh.conn()
            response[host] = ssh.exec(_cmd)
            return str(response)

    def on_request(self, ch, method, props, body):
        cmd = body.decode()
        print(cmd)
        response = self.handler(cmd)
        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(correlation_id=props.correlation_id),
                         body=response)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start(self):
        self.channel.basic_consume(self.on_request, queue='rpc_queue')
        print('等待数据'.center(60, '='))
        self.channel.start_consuming()

class SSHClients(object):
    def __init__(self, username, password, hostname, port=22):
        self.username = username
        self.password = password
        self.hostname = hostname
        self.port = port

    def conn(self):
        '''连接服务器'''
        # 创建SSH对象
        self.ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        self.ssh.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.password)

    def exec(self, cmd):
        # 执行命令
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        # 获取执行结果
        res, err = stdout.read(), stderr.read()
        result = (res if res else err).decode()
        return result

    def to_close(self):
        self.ssh.close()

if __name__ == '__main__':
    s = server()
    s.start()
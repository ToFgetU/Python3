#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import paramiko
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
        return self.ssh.connect(hostname=self.hostname, port=self.port, username=self.username, password=self.password)

    def exec(self, cmd):
        # 执行命令
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        # 获取执行结果
        res, err = stdout.read(), stderr.read()
        result = (res if res else err).decode()
        return result

    def close(self):
        self.ssh.close()

    def sftp_conn(self):
        # 创建SFTP对象
        transport = paramiko.Transport((self.hostname, self.port))
        transport.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient()
        return sftp

    def change(self, cmd):
        sftp.put('test.txt', '/tmp/test.txt')
        sftp.get('/etc/passwd', 'passwd.txt')

        transport.close()

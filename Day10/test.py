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

    def sftp_conn(self):
        # 创建SFTP对象
        self.transport = paramiko.Transport((self.hostname, self.port))
        self.transport.connect(username=self.username, password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def change(self, cmd):
        if len(cmd) < 3:
            return 'Invalid cmd'
        if cmd[0] == 'put':
            try:

                self.sftp.put(cmd[1], cmd[2])
                return '上传成功'
            except FileNotFoundError as e:
                return e
        else:
            try:
                self.sftp.get(cmd[1], cmd[2])
                return '下载成功'
            except FileNotFoundError as e:
                return e

    def sftp_close(self):
        self.transport.close()



if __name__ == '__main__':
    p = SSHClients('weblogic', 'weblogic', '10.28.31.183')
    p.conn()
    policy = input('请输入要下载的保单号: ').strip()
    cmd = 'get /home/data_mount/ilis/ehome_print/%s.pdf' % policy
    p.change(cmd)
    p.sftp_close()
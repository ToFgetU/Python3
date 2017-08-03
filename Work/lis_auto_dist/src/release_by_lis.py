#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import paramiko
from conf import settings

def ssh_conn(hostname):
    try:
        ssh = paramiko.SSHClient()

        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接服务器
        # ssh.connect(hostname='192.168.128.133', port=22, username='root', password='123456')
        private_key = paramiko.RSAKey.from_private_key_file('/home/weblogic/.ssh/id_rsa')
        ssh.connect(hostname=hostname, port=22, username='weblogic', pkey=private_key)
        return ssh
    except Exception as e:
        settings.logger.error("%s SSH CONNECTION ERROR：%s".center(60, '=') % (hostname, e))

def exec(ssh, cmd):
    try:
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(cmd)

        # 获取执行结果
        res, err = stdout.read(), stderr.read()
        result = (res if res else err).decode()
        settings.logger.debug("%s 文件创建成功<%s>：%s" % (hostname, cmd, result))
        print(result)
    except Exception as e:
        settings.logger.error("%s ERROR：%s" % (hostname, e))

def sftp_conn(hostname):
    """SFTP connection"""
    try:
        private_key = paramiko.RSAKey.from_private_key_file('/home/weblogic/.ssh/id_rsa')
        transport = paramiko.Transport((hostname, 22))
        transport.connect(username='weblogic', pkey=private_key)
        settings.logger.debug("%s 服务器连接成功".center(60, '=') % hostname)
        return transport
    except Exception as e:
        settings.logger.error("%s 服务器连接失败：%s".center(60, '=') % (hostname, e))

def upload(transport, path, to_path):
    """to upload the file """
    try:
        # print('开始上传文件,连接sftp')
        sftp = paramiko.SFTPClient.from_transport(transport)
        # print("sftp连接成功")
        # 将path 上传至服务器 to_path
        sftp.put(path, to_path)
        print("%s --> %s" % (path, to_path))
        settings.logger.debug("%s --> %s" % (path, to_path))
    except Exception as e:
        settings.logger.error("%s 文件上传失败：%s" % (path, e))
        print("%s 文件上传失败：%s" % (path, e))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()

# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
# ssh.connect(hostname='192.168.128.133', port=22, username='root', password='123456')
private_key = paramiko.RSAKey.from_private_key_file('id_rsa.txt')
ssh.connect(hostname='192.168.128.131', port=22, username='root', pkey=private_key)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')

# 获取执行结果
res, err = stdout.read(), stderr.read()
result = (res if res else err).decode()
print(result)

# 关闭连接
ssh.close()

# 创建SFTP对象
transport = paramiko.Transport(('192.168.128.131', 22))
transport.connect(username='root', pkey=private_key)
sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put('test.txt', '/tmp/test.txt')
sftp.get('/etc/passwd', 'passwd.txt')

transport.close()

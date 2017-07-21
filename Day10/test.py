#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import paramiko
import cx_Oracle

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

def oracle_conn(policy):
    dns_tns = '(DESCRIPTION=(ADDRESS_LIST=(FAILOVER=on)(LOAD_BALANCE=on)(ADDRESS=(PROTOCOL=TCP)(HOST=*.*.*.*)(PORT=1521))(ADDRESS=(PROTOCOL=TCP)(HOST=*.*.*.*)(PORT=1521)))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=LISDBPRD)))'
    # 连接数据库
    conn = cx_Oracle.connect('user', 'passwd', dns_tns)
    print('oracle version:', conn.version)
    # 获取游标
    cursor = conn.cursor()
    cursor.execute("select prtno from lccont where contno=%s" % policy)
    # 获取执行结果
    result = cursor.fetchone()
    print('result:', result)
    cursor.close()
    conn.close()
    return result[0]

def get_pdf(policy, dest):
    p = SSHClients('weblogic', '7bdc2df9', '10.28.31.183')
    p.sftp_conn()
    if len(policy) == 12:
        cmd = 'get /home/data_mount/ilis/ehome_print/%s.pdf %s' % (policy, dest)
        cmd = cmd.split()
        tmp = p.change(cmd)
    elif len(policy) == 15:
        cmd = 'get /home/data_mount/ilis/ehome/%ssinatay.pdf %s' % (policy, dest)
        cmd = cmd.split()
        tmp = p.change(cmd)
    else:
        p.sftp_close()
        exit('获取的pdf有误')
    print(tmp)
    p.sftp_close()


if __name__ == '__main__':
    policy = input('请输入要下载的单号: ').strip()
    change = input('是否需要签章(Y/N): ').strip().upper()
    dest = 'D:/%s.pdf' % policy
    if len(policy) == 12:
        if change == 'Y':
            policy = oracle_conn(policy)
            dest = 'D:/%s.pdf' % policy
            get_pdf(policy, dest)
        else:
            get_pdf(policy, dest)
    elif len(policy) == 15:
            get_pdf(policy, dest)
    else:
        exit('输入的单号有误')

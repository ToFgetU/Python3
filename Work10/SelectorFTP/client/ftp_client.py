#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu
"""
简单的客户端
使用方法：put filename
测试并发：准备好一个几M文件，一个几十M文件，先put大的，再put小的，就能看到效果
"""
import os, sys, datetime
import socket
import optparse


def auth(client, opstions, args):
    '''用户验证'''
    if opstions.username is None or opstions.password is None:
        parse.print_help()
        return False
    else:
        cmd = 'auth|%s|%s' % (opstions.username, opstions.password)
        cmd = cmd.strip()
        client.send(cmd.encode('utf8'))
        response = client.recv(1024).strip().decode()
        return response


def make_conn(opstions, args):
    '''连接服务器'''
    if opstions.server is None or opstions.port is None:
        parse.print_help()
        return False
    else:
        # print(self.opstions, self.args)
        client = socket.socket()
        client.connect((opstions.server, int(opstions.port)))
        return client

def start():
    '''开始程序'''
    parse = optparse.OptionParser()
    parse.add_option("-s", "--server", dest="server", help="ftp server ip addr")
    parse.add_option("-P", "--Port", type='int', dest="port", help="ftp server port")
    parse.add_option("-u", "--username", dest="username", help="ftp server user")
    parse.add_option("-p", "--password", dest="password", help="ftp server password")
    opstions, args = parse.parse_args()
    client = make_conn(opstions, args)
    conn = int(auth(client, opstions, args))

    if conn:
        print('登入成功')
        c_input = input('[%s]>>>' % opstions.username).strip()
        action = c_input.split(maxsplit=1)[0]
        filename = c_input.split(maxsplit=1)[1]
        if action == 'put':
            if os.path.dirname(filename):
                filesize = os.stat(filename).st_size
                cmd = '%s|%s|%s|%s' % (action, filename, opstions.username, filesize)
            else:
                exit('输入的文件不存在')
        else:
            cmd = '%s|%s|%s' % (action, filename, opstions.username)
        if cmd.startswith('put'):
            client.send(cmd.encode('utf8'))
            # 服务端确认可以接收数据
            client.recv(1)
            buffer_size = 4096
            sent_size = 0
            with open(filename, 'rb') as fp:
                while fp.tell() < filesize:
                    buffer = fp.read(buffer_size)
                    client.send(buffer)
                    sent_size += len(buffer)
                    print("已发送%d%%，%d字节" % (int(sent_size / filesize * 100), sent_size))
            print('发送完毕')
            client.close()
        elif cmd.startswith('get'):
            # print(cmd)
            client.send(cmd.encode('utf8'))
            response = client.recv(1024).decode()
            if response == '0':
                exit('下载的文件不存在')
            else:
                received_size = 0
                while True:
                    filename = response.split('|')[0]
                    filesize = int(response.split('|')[1])
                    if os.path.dirname(filename):
                        received_size = os.stat(os.path.abspath(filename)).tz_size
                    s_cmd = '%s|%s' % (filename, received_size)
                    client.send(s_cmd.encode('utf8'))
                    with open(filename, 'ab') as fp:
                        # print(fp)
                        if filesize - received_size > 4096:
                            data = client.recv(4096)
                            fp.write(data)
                            fp.flush()
                            received_size += len(data)
                            print("已接收%d%%，%d字节" % (int(received_size / filesize * 100), received_size))
                        else:
                            data = client.recv(filesize - received_size)
                            fp.write(data)
                            fp.flush()
                            received_size += len(data)
                            print("已接收%d%%，%d字节" % (int(received_size / filesize * 100), received_size))
                            break

        else:
            exit("输入错误")

    else:
        exit('登入失败')


if __name__ == '__main__':
    start()
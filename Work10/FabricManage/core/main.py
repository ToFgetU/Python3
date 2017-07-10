#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import threading, os
from conf import settings
from core.ftpserver import SSHClients

class Handler(object):
    '''服务端的调用类'''
    HOST_LIST = []
    HP_LIST = []
    # RESULT_DICT = {}

    def callback_func(self, msg):
        '''回调函数'''
        self.semaphore.acquire()
        print(msg)
        self.semaphore.release()

    # @staticmethod
    def _cmd(self, host, ssh, _cmd, callback):
        '''命令行,利用回调函数显示结果'''
        result = ssh.exec(_cmd)#self.s.exec(_cmd)
        print(host.center(60, '='))
        callback(result)
        # print(result)
        # Handler.RESULT_DICT[host] = result
        # for k, v in Handler.RESULT_DICT.items():
        #     print(k.center(60, '='))
        #     print(v)
        #     Handler.RESULT_DICT = {}
        ssh.to_close()

    def _put(self, host, ssh, _cmd, callback):
        '''上传文件'''
        result = ssh.change(_cmd)
        print(host.center(60, '='))
        callback(result)
        ssh.sftp_close()

    def _get(self, host, ssh, _cmd, callback):
        '''下载文件'''
        result = ssh.change(_cmd)
        print(host.center(60, '='))
        callback(result)
        ssh.sftp_close()

    def show(self):
        '''主机列表显示'''
        print('------ HOST LIST -----')
        for k, v in settings.hosts_dict.items():
            print('[%s]' % k)
            for m, n in v:
                Handler.HOST_LIST.append(m)
                Handler.HP_LIST.append((m, n))
                print(m)

        # 主机去重
        Handler.HOST_LIST = list(set(Handler.HOST_LIST))

    def start(self):
        '''主程序，启动方法'''
        # host_list = settings.hosts_dict
        while True:
            self.show()
            # print(Handler.HP_LIST)
            choice = input('\n>>> 请选择要执行的主机或主机组: ').strip()
            self.hosts = []
            if choice in Handler.HOST_LIST:
                for i in Handler.HP_LIST:
                    if choice == i[0]:
                        self.hosts.append(i)
                        break
            elif choice in settings.hosts_dict:
                for i in settings.hosts_dict[choice]:
                    self.hosts.append(i)
            elif choice == 'exit':
                exit("退出程序")
            else:
                exit('输入的主机或主机组不存在')

            print("服务器连接成功".center(70, '+'))
            print("""
                ****************************************************
                * 命令行格式:                                      *
                *     df -Th                                       *
                *     ifconfig                                     *
                *     put filename dest                            *
                *       ex: put F:/hello.txt /tmp/hello.txt        *
                *     get filename dest                            *
                *       ex: get /tmp/hello.txt helloworld.txt      *
                ****************************************************""")
            while True:
                self.semaphore = threading.BoundedSemaphore(10)
                cmd = input("\n>>> 请操作: ").strip()
                # print(cmd)
                cmd_list = cmd.split()
                # print(cmd_list)
                if cmd_list[0] == 'exit':
                    break
                res_list = []
                for h in self.hosts:
                    username = settings.user_dict[h[0]]['username']
                    password = settings.user_dict[h[0]]['password']
                    s = SSHClients(username, password, h[0], h[1])
                    if cmd_list[0] == 'put' or cmd_list[0] == 'get':
                        s.sftp_conn()
                    else:
                        s.conn()
                    if hasattr(self, '_%s' % cmd_list[0]):
                        func = getattr(self, '_%s' % cmd_list[0])
                        t = threading.Thread(target=func, args=(h[0], s, cmd_list, self.callback_func))
                        t.start()
                        res_list.append(t)
                    else:
                        t = threading.Thread(target=self._cmd, args=(h[0], s, cmd, self.callback_func))
                        t.start()
                        res_list.append(t)
                for j in res_list:
                    j.join()



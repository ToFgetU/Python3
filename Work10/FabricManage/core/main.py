#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import threading
from conf import settings
from core.ftpserver import SSHClients

class Handler(object):
    HOST_LIST = []
    HP_LIST = []
    def _cmd(self, cmd):
        result = self.s.exec(cmd)
        print(result)
        self.s.close()

    def _conn(self):
        pass

    def show(self):
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
        # host_list = settings.hosts_dict
        self.show()
        print(Handler.HP_LIST)
        choice = input('>>> 请选择要执行的主机或主机组: ').strip()
        self.hosts = []
        if choice in Handler.HOST_LIST:
            for i in Handler.HP_LIST:
                if choice == i[0]:
                    self.hosts.append(i)
                    break
        elif choice in settings.hosts_dict:
            for i in settings.hosts_dict[choice]:
                self.hosts.append(i)
        else:
            exit('输入的主机或主机组不存在')

        print("服务器连接成功".center(60, '+'))
        print("""
            ***********************************
            * 命令行格式:                     *
            *     df                          *
            ***********************************""")
        cmd = input(">>> 请操作: ").strip()
        for h in self.hosts:
            username = settings.user_dict[h[0]]['username']
            password = settings.user_dict[h[0]]['password']
            self.s = SSHClients(username, password, h[0], h[1])
            self.s.conn()
            if hasattr(self, '_%s' % cmd[0]):
                func = getattr(self, '_%s' % cmd[0])
                t = threading.Thread(target=func, args=(cmd,))
                t.start()
            else:
                t = threading.Thread(target=self._cmd, args=(cmd,))
                t.start()




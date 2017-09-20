#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socket
import hashlib
import pickle
import os
from optparse import OptionParser

class ftp_client(object):
    def __init__(self):
        self.parser = OptionParser()
        self.parser.add_option("-P","--PORT",dest="PORT",help="the server PORT")
        self.parser.add_option("-i","--host",dest="host",help="the server IP")
        self.parser.add_option("-u", "--username", dest="username", help="the username")
        self.parser.add_option("-p", "--passwd", dest="passwd", help="the passwd")
        options, args = self.parser.parse_args()
        #print(options),print(type(options))
        if options.host and options.PORT:
            self.conn(options)
        else:
            print('缺少主机ip和端口号')
    def auth_user(self,options):
        if options.username and options.passwd:
            options = self.encry(options)
            self.s.send(pickle.dumps(options))
            self.mysocket()
        elif options.username is None and options.passwd is None:
            x = 0
            while  x < 3:
                username = input('请输入用户名>>>').strip()
                passwd = input('请输入密码>>>').strip()
                if username and passwd:
                    options.username = username
                    options.passwd = passwd
                    #self.pass_userinfo(username, passwd)
                    break
                x += 1
            options = self.encry(options)
            self.s.send(pickle.dumps(options))
            self.mysocket()
        else:
            print('请输入用户名或者密码...')
    def encry(self,options):
        '''对用户传输的密码进行加密'''
        md5_passwd = hashlib.md5()
        md5_passwd.update(options.passwd.encode())
        options.passwd = md5_passwd.hexdigest()
        return options
    def conn(self,options):
        self.s = socket.socket()
        self.s.connect((options.host, int(options.PORT)))
        self.auth_user(options)
        # while True:
        #     choice = input('>>>')
        #     if len(choice)==0:continue
        #     self.s.send(choice.encode())
        #     print(self.s.recv(1024).decode())
    def mysocket(self):
        '''与服务器交互数据'''
        file_list = pickle.loads(self.s.recv(1024))
        for i in file_list:
            print(i)
        while True:

            socket_data = input('>>>')
            #print('准备发送数据')
            if len(socket_data) == 0:continue
            socket_data_list = socket_data.split()
            if hasattr(self,'_%s'% socket_data_list[0]):
                self.s.send(pickle.dumps(socket_data_list))
                func = getattr(self,'_%s'% socket_data_list[0])
                func(socket_data_list)
                #self.s.send(socket_data_list)
    def _get(self,*args,**kwargs):
        file_size = int(self.s.recv(1024).decode())
        self.xb = 0
        self.zb = 0
        self.s.send('sucess'.encode())
        file_len = 0
        hs_get = hashlib.md5()
        with open('tmp/%s'% args[0][1],'wb') as f:
            print('[',end='')
            while file_len < file_size:
                if (file_size - file_len)>1024:
                    file_len2 = self.s.recv(1024)
                else:
                    file_len2 = self.s.recv(file_size - file_len)

                self._scr(file_len,file_size)
                f.write(file_len2)
                hs_get.update(file_len2)
                #self._scr(len(file_len2),file_size)
                file_len += len(file_len2)
        hs_client = hs_get.hexdigest()
        hs_server = self.s.recv(1024).decode()
        if hs_client == hs_server:
            print('] 100%')
            print('传输完成，文件内容一致')
    def _put(self,*args,**kwargs):
        self.xb = 0
        self.zb = 0
        self.s.recv(1024)
        hs_put = hashlib.md5()
        putfile_size = os.path.getsize('%s/%s' % ('tmp', args[0][1]))
        self.s.send(str(putfile_size).encode())
        put_file_size = self.s.recv(1024).decode()
        if put_file_size == 'big':
            print('您上传的文件过大，服务器没有足够的空间')
        else:
            putfile_len = 0
            with open('%s/%s' % ('tmp', args[0][1]), 'rb') as f:
                print('[',end='')
                for i in f:
                    self.s.send(i)
                    self._scr(putfile_len, putfile_size)
                    hs_put.update(i)
                    putfile_len += len(i)
            print('] 100%')
            self.s.send(hs_put.hexdigest().encode())
        # with open('%s/%s'% (args[0],args[1][1]),'r',encoding='gbk') as f:
        #   for i in f:
        #       print(i)
    def _ls(self,*ages,**kwargs):
        file_list = pickle.loads(self.s.recv(1024))
        for i in file_list:
            print(i)
    def _cd(self,*ages,**kwargs):
        pass


    def _scr(self,s,totle):
        '''上传下载的时候显示文件进度条'''
        #print(self.x)
        #print(s)
        if (self.xb+totle/30) < 1024:
            if self.zb < 1:
                print('##############################',end='')
                self.zb += 1
        elif (self.xb+totle/30) >= 1024:
            if self.xb < s:
                print('#',end='')
                #y+='#'
                self.xb += (totle/30)


if __name__ == '__main__':
    f = ftp_client()
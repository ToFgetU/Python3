#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from conf import settings
import pickle
import hashlib
import configparser
import os
import pickle

import  socket
import selectors
HOST, PORT = settings.HOST, settings.PORT
def run():
    m = myTCPserver()
    # m.handle(conn)
    def accept(sock, mask):
        conn, addr = sock.accept()
        conn.setblocking(False)
        sel.register(conn, selectors.EVENT_READ, m.handle2)

    sock = socket.socket()
    sock.setblocking(False)
    sock.bind((HOST, PORT))
    sock.listen(10)
    sel = selectors.DefaultSelector()
    sel.register(sock, selectors.EVENT_READ, accept)
    print('服务器开始运行...')
    # server = socketserver.ThreadingTCPServer((HOST, PORT), c)
    # server.serve_forever()
    while True:
        events = sel.select()
        for key, mask in events:
            func2 = key.data
            func2(key.fileobj, mask)



DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class myTCPserver():
    def handle2(self,conn,mask):
        data = pickle.loads(conn.recv(1024))
        if data:
            self.username = data.username
            self.passwd = data.passwd
            #print(data)
            if self.auth_user(self.username,self.passwd):
                print('登录成功...')
                #self.path = '%s/home/%s' % (DIR, self.username)
                self.file_path_home = '%s/home/%s' % (DIR, self.username)
                '''获取并打印用户主目录大小'''
                self.get_s = 0
                self._get_size('%s/home/%s' % (DIR, self.username))
                print(self.get_s)
                self.get_user_size = int(self.get_user_size) * 1024 * 1024


                self.file_path = '%s/home/%s' % (DIR, self.username)
                self.file_list = self.check(self.username)
                conn.send(pickle.dumps(self.file_list))
                while True:

                    data_file = conn.recv(1024)
                    print('开始传送数据')
                    socket_data_list = (pickle.loads(data_file))
                    socket_data_list = (pickle.loads(data_file))
                    print(socket_data_list)

                    if hasattr(self,'_%s'%socket_data_list[0]):
                        func = getattr(self,'_%s'%socket_data_list[0])
                        func(self.file_path,socket_data_list)
            else:
                print('用户名或者密码有误')
            #print('%s已经断开'% self.client_address)
            #break
        #if len(data) == 0:continue
        #print('{}worte:'.format(self.client_address))
        #self.request.send(data.upper().encode())
        #print('%s已经断开！！！'% self.client_address[0])
    def auth_user(self,username,passwd):
        '''此方法目的是为了验证用户的合法性'''
        cf = configparser.ConfigParser()
        cf.read(settings.USERS)
        if username in cf.sections():
            self.get_user_size = cf[username]['size']
            md5_passwd = hashlib.md5()
            md5_passwd.update(cf[username]['Password'].encode())
            if passwd == md5_passwd.hexdigest():
                return True
            else:
                return False
        else:
            return False
    def check(self,username):
        return os.listdir('%s/home/%s'%(DIR,username))
    def _get(self,*args,**kwargs):
        '''客户端下载文件方法'''
        #self.file_path = '%s/home/%s'%(DIR,self.username)
        #print('111111111111111111111111111111111111111111111111111111111%s'% args[1][1])
        file_size = os.path.getsize('%s/%s'%(self.file_path,args[1][1]))
        #print(file_size)
        self.request.send(str(file_size).encode())
        self.request.recv(1024)
        hs = hashlib.md5()
        with open('%s/%s'%(self.file_path,args[1][1]),'rb') as f:
            for i in f:
                self.request.send(i)
                hs.update(i)
        self.request.send(hs.hexdigest().encode())
        #with open('%s/%s'% (args[0],args[1][1]),'r',encoding='gbk') as f:
         #   for i in f:
         #       print(i)
    def _put(self,*args,**kwargs):
        '''给服务器上传文件方法'''
        self.request.send('sucess'.encode())
        file_size = int(self.request.recv(1024).decode())
        if self.get_s + file_size > self.get_user_size:
            self.request.send('big'.encode())
        #home_size = self._get_size(self, '%s/home/%s' % (DIR, self.username))
        #print('111111111111111111111111111111111111111111111111111111111111 %s' % home_size)
        else:
            self.request.send('sucess'.encode())

            file_size_put = 0
            hs_put = hashlib.md5()
            with open('%s/%s'% (args[0],args[1][1]),'wb')as f:
                while file_size_put < file_size:
                    if file_size - file_size_put < 1024:
                        file_file = self.request.recv(file_size - file_size_put)
                    else:
                        file_file=self.request.recv(1024)
                    f.write(file_file)
                    hs_put.update(file_file)
                    file_size_put += len(file_file)
            hs_server = hs_put.hexdigest()
            hs_client = self.request.recv(1024).decode()
            if hs_server == hs_client:
                print('传输完成，文件内容一致')

        #with open('%s/%s'% (args[0][0],args[1][1]))
    def _ls(self,*args,**kwargs):
        file_list = os.listdir(self.file_path)
        self.request.send(pickle.dumps(file_list))

    def _cd(self,*args,**kwargs):
        if args[1][1] == '..':
            if self.file_path == self.file_path_home:
                self.file_path = self.file_path_home
            else:
                self.file_path = os.path.dirname(self.file_path)

        else:
            self.file_path = self.file_path + '/%s' % args[1][1]


    def _get_size(self,size_file_path):
        '''这个方法获取主目录文件的大小'''
        for i2 in os.listdir(size_file_path):
            if os.path.isfile('%s/%s'% (size_file_path,i2)):
                self.get_s += os.path.getsize('%s/%s'% (size_file_path,i2))
            if os.path.isdir('%s/%s'% (size_file_path,i2)):
                self._get_size('%s/%s' % (size_file_path,i2))

    #get_file_size(size_file_path)
    #   return self.get_s







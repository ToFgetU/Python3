#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from core import server
from optparse import OptionParser
from core import server
from core.server import myTCPserver
from  conf import settings



# 创建socket对象


# 创建selector对象



#def read(conn,mask):



class MyParser(object):
    def __init__(self):
        self.parser=OptionParser()
        # self.parser.add_option("-P","--PORT",dest="PORT",help="the server PORT")
        # self.parser.add_option("-h","--host",dest="host",help="the server IP")
        # self.parser.add_option("-u", "--username", dest="username", help="the username")
        #self.parser.add_option("-p", "--passwd", dest="passwd", help="the passwd")
        self.options,self.args = self.parser.parse_args()
        self.auth_user_passwd(self.options,self.args)
    def auth_user_passwd(self, option, args):
        if hasattr(self,args[0]):
            func = getattr(self,args[0])
            func()
    def start(self):
        server.run()

    #建立请求方法



    # def myTCPserver(self,conn,mask):
    #     pass


'''
import selectors
import socket


def read(conn,mask):
    data = conn.recv(1024)
    if data:
        conn.send(data.upper())
    else:
        sel.unregister(conn)
        conn.close()
def accept(sock,mask):
    conn, addr = sock.accept()
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)

s = socket.socket()
s.bind(('127.0.0.1',9999))
s.setblocking(False)
s.listen(10)

sel = selectors.DefaultSelector()
sel.register(s,selectors.EVENT_READ,accept)
print('selector start')
while True:
    events = sel.select()
    for key,value in events:
        func = key.data
        func(key.fileobj,value)



'''










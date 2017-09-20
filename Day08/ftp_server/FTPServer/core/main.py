#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import socket
import selectors
import time



def read(conn,mask):
    try:
        size = int(conn.recv(1024).decode())
        print(size)
        with open('file.txt', 'wb') as f:
            len_file = 0
            time.sleep(1)
            while size > len_file:
                if (size - len_file) > 1024:
                    data = conn.recv(1024)
                    print("-->", data)
                else:
                    data = conn.recv(size - len_file)
                print(data.decode())
                f.write(data)
                len_file += len(data)

        conn.send('ok'.encode())
    except Exception as e:
        print(e)
        print('%s断开'% mask)
        sel.unregister(conn)
        conn.close()

def accept(server,mask):
    conn,addr = server.accept()
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)

server = socket.socket()
server.bind(('127.0.0.1',8888))
server.setblocking(False)
server.listen(10)

sel = selectors.DefaultSelector()
sel.register(server, selectors.EVENT_READ, accept)
def run():
    print('ftp services...')
    while True:
        events = sel.select()
        for key,mask in events:
            func = key.data
            func(key.fileobj,mask)
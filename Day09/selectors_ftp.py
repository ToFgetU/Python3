#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import selectors
import socket
import time
import threading

sel = selectors.DefaultSelector()


def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr, '--mask', mask)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)
    time.sleep(10)


def read(conn, mask):
    data = conn.recv(1024)  # Should be ready
    print('开始', conn)

    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
        time.sleep(2)
        print('结束', conn)
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()


sock = socket.socket()
sock.bind(('localhost', 9999))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    # res_list = []
    for key, mask in events:
        print('触发事件', key.fileobj)
        callback = key.data
        callback(key.fileobj, mask)
    #     t = threading.Thread(target=callback, args=(key.fileobj, mask))
    #     t.start()
    #     res_list.append(t)
    # for j in res_list:
    #     j.join()
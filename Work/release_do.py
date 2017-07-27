#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

# import cx_Oracle
#
# TNS_DICT = { '生产': '(DESCRIPTION=(ADDRESS_LIST=(FAILOVER=on)(LOAD_BALANCE=on)(ADDRESS=(PROTOCOL=TCP)(HOST=10.16.1.103)(PORT=1521))(ADDRESS=(PROTOCOL=TCP)(HOST=10.16.1.104)(PORT=1521)))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=LISDBPRD)))',
#              '准生产':  '(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=10.20.3.90)(PORT=1521)))(CONNECT_DATA=(lisdb90)))'}
#
# def oracle_conn(user, password, tns):
#     conn = cx_Oracle.connect(user, password, tns)
#     return conn
#
# def DML_DB(conn, sql):
#     # 获取游标
#     cursor = conn.cursor()
#     result = cursor.execute(sql)
#     print(result)
#     cursor.close()
#     db.commit()
#
# def DDL_DB(conn, sql):
#     # 获取游标
#     cursor = conn.cursor()
#     result = cursor.execute(sql)
#     print(result)
#     cursor.close()
#     db.commit()

from subprocess import Popen, PIPE

def run_sql_script(connstr, filename):
    sqlplus = Popen(['sqlplus', '-S', connstr], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    sql = '@ %s' % filename
    print(sql)
    sql = sql.encode()
    sqlplus.stdin.write(sql)
    return sqlplus.communicate()

connstr = 'dev/dev@orcl'
output, error = run_sql_script(connstr, r'E:\test.sql')
# output = output.decode()
# error = error.decode()
print(output)
print('error', error)

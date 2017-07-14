#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import os
import os.path
import datetime

env = input("请输入环境: ").strip()
pathdir = input("请输入脚本路径: ").strip()

if env == '1':
	user_code = 'liscode'
	user_base = 'lisbase'
	user_data = 'lisdata'
	pwd_code = 'liscode432u1'
	pwd_base = 'lisbase643u1'
	pwd_data = 'lisdata531u1'
	db_name = 'stgdb'
elif env == '2':
	user_code = 'songj[liscode]'
	user_base = 'songj[lisbase]'
	user_data = 'songj[lisdata]'
	pwd_code = 'zxcvbnm,.123'
	pwd_base = 'zxcvbnm,.123'
	pwd_data = 'zxcvbnm,.123'
	db_name = 'lis'

now = datetime.datetime.now()
#struts_base
sqltxt = 'sqlautorun'+('%d' %now.year)+('%d' %now.month).zfill(2)+('%d' %now.day).zfill(2)+\
       ('%d' %now.hour).zfill(2)+('%d' %now.minute).zfill(2)+('%d' %now.second).zfill(2)+\
       ('%d' %now.microsecond)+'strutsbase.sql'

#"/usr/local/var/homebrew/locks"
file_object=open(sqltxt,'w')
file_object.write('')
file_object.close()
for parent,dirnames,filenames in os.walk(rootdir+'\\struts_base'):
	#for dirname in dirnames:
	#	print("parent folder is:"+parent)
	for filename in filenames:
		#rint("parent folder is:"+parent)
		#print("filename with full path:"+os.path.join(parent,filename))

		file_path=os.path.join(parent,filename)

		file_object=open(sqltxt,'a+')
		file_object.write('@ '+file_path+'\n')
		file_object.close()

#调用sqlplus执行脚本计划
sql_list=open(sqltxt,'rU').readlines()
i=0
j='Y'
while (i<len(sql_list) and j=='Y'):
	sqltent = """
    set head off
    spool sql.log
    %s
    spool off
    """ % sql_list[i]
	cmd = 'sqlplus %s/%s@%s << EOF %s EOF' % (user_code, pwd_code, db_name, sqltent)
	result = os.popen(cmd)
	for line in result:
		print('result:', line)
	i=i+1
	j=super(input('是否继续？（Y/N）').strip())


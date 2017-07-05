## 程序介绍

#### 作者:ToFgetU
#### 版本:示例版本 v0.1
#### 程序功能介绍:
    实现简易的SELECT FTP服务端与客户端。
    功能全部用python的基础知识和面向对象知识实现,用到了json\os\sys\socketoptparse\selectors\函数\模块知识，通过用optparse 对格式进行格式化要求，通过configgparser对 帐号文件进行读取
##### 主要功能如下：
######	1. FTP客户端
	1) 上传命令 （put）
		功能：上传一个文件到用户家目录
	2) 下载命令	（get）
		功能：在用户家目录下载一个文件
	3) FTP启动参数
		-s: ip address
		-P: Port
		-u: username
		-p: password

######	2. FTP服务端
	实现FTP客户端的功能交互，多用户并发上传下载文件


#### 程序结构:

	FTP #主目录
	├──	client #FTP客户端
	│　　	└── ftp_client.py     # FTP客户端功能实现模块
	│
	└── server #FTP服务端
		├── bin # 执行文件 目录  	
		│　　├── __init__.py  
		│　　└── f_start.py # 执行程序  
		├── conf #配置文件目录  
		│　　├── __init__.py
		│　　└── settings.py  #数据路径配置文件  
		├── core #主要逻辑程序  
		│　　├── __init__.py  
		│　　├── ftp_server.py  #FTP服务端实现模块 
		│　　└── main.py  #FTP服务端主程序  
		└── home  #用户家目录
		　　　└── alex #账户目录

#### 测试案例(环境为 python3.6 的环境)：
	测试用户：alex
	用户密码：123
	
	启动FTP服务端：
		[root@dev-mysql bin]# python3 ftp_start.py start

	启动FTP客户端：
		#### 用户test
		[root@dev-mysql SelectFTP]# python3 client/ftp_client.py -s 10.11.22.117 -P10021 -u test -p test
		recv data:  b'{"status_code": 200, "status_msg": "Success"}'
		开始交互
		[test] >>> put /home/work/Work10/SelectFTP/server/home/alex/test.avi
		t1 b'1'
		t2 b'1'
		recv data:  b'{"status_code": 200, "status_msg": "Success"}'
		文件上传成功
		[test] >>> get test.avi
		recv data:  b'{"status_code": 200, "status_msg": "Success", "filename": "test.avi", "size": 13949898}'
		recv data:  b'{"status_code": 200, "status_msg": "Success"}'
		文件下载成功
		
		#### 用户alex
		[root@dev-mysql client]# python3 ftp_client.py -s 10.11.22.117 -P10021 -u alex -p 123
		recv data:  b'{"status_code": 200, "status_msg": "Success"}'
		开始交互
		[alex] >>> put /home/work/Work10/SelectFTP/server/home/alex/test.avi
		t1 b'1'
		t2 b'1'
		recv data:  b'{"status_code": 200, "status_msg": "Success"}'
		文件上传成功
		[alex] >>> get test.avi
		recv data:  b'{"status_code": 200, "status_msg": "Success", "filename": "test.avi", "size": 13949898}'
		recv data:  b'{"status_code": 200, "status_msg": "Success"}'
		文件下载成功
		[alex] >>> 

#####注意：用户设置或添加需要直接修改server/conf/settings.py
		 	
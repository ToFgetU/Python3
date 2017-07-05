## 程序介绍

#### 作者:ToFgetU
#### 版本:示例版本 v0.1
#### 程序功能介绍:
    实现简易的FTP客户端与服务端。
    功能全部用python的基础知识和面向对象知识实现,用到了json\os\sys\socket\socketserver\optparse\configparser\函数\模块知识，通过用optparse 对格式进行格式化要求，通过configgparser对 帐号文件进行读取
##### 主要功能如下：
######	1. FTP客户端
	1) 上传命令 （put）
		功能：上传一个文件到用户家目录
	2) 下载命令	（get）
		功能：在用户家目录下载一个文件，支持断点续传
		参数： --md5 对下载文件进行校验一致性
	3) 查看命令	（ls）
		功能：查看当前家目录下所有文件
	4) 查看当前路径	（pwd）
		功能：查看当前位置所在的路径
	5) 切换目录	（cd）
		功能：切换目录
		其他用法：（~，..）
			cd ~：返回用户根目录
			cd ..：返回上级目录
	6) FTP客户端启动参数
		-s: ip address
		-P: Port
		-u: username
		-p: password

######	2. FTP服务端
	实现FTP客户端的功能交互
	服务器启动参数： start


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
		│　　├── account.cfg  #FTP账户配置 
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
		[root@dev-mysql client]# python3 ftp_client.py -s localhost -P 10021 -u alex -p 123
		Passed authentication!
		开始交互
		[alex] >>> ls
		a
		test.avi
		test.png
		[alex] >>> cd a
		[alex] >>> ls
		c
		b
		[alex] >>> pwd
		/home/work/Work10/FTP/server/home/alex/a
		[alex] >>> cd ..
		[alex] >>> ls
		a
		test.avi
		test.png
		[alex] >>> 
		[alex] >>> get test.png --md5
		=======================100%
		文件校验一致，下载成功
		[alex] >>> get test.avi --md5
		===================================================================================================100%
		文件校验一致，下载成功
		[alex] >>> get test.png
		=======================100%
		文件下载成功
		[alex] >>> get test.avi
		===================================================================================================100%
		文件下载成功
		[alex] >>> put /usr/local/Python-3.5.1.tar
		文件上传成功
		[alex] >>> ls
		test.avi
		Python-3.5.1.tar
		test.png
		[alex] >>> 

		


#####注意：用户设置或添加需要直接修改server/conf/account.cfg
		 	
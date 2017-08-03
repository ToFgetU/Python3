## 程序介绍

#### 作者:ToFgetU
#### 版本:示例版本 v0.1
#### 程序功能介绍:
    实现简易的SELECT FTP服务端与客户端。
    功能全部用python的基础知识和面向对象知识实现,用到了json\os\sys\socketoptparse\selectors\函数\模块知识，通过用optparse 对格式进行格式化要求

	缺陷：客户端单次上传或下载之后就会退出程序，待优化，加入循环即可，只是实现简单的多并发，并没有考虑文件存在及一致性问题
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
		│　　└── ftp_server.py  #FTP服务端实现模块 
		└── home  #用户家目录
		　　　└── alex #账户目录

#### 测试案例(环境为 python3.6 的环境)：
	
	启动FTP服务端：
		[root@dev-mysql bin]# python3 ftp_start.py

	启动FTP客户端：
		
		#### 用户alex
		[root@dev-mysql client]# python3 ftp_client.py -s localhost -P10021 -u alex -p 123
		登入成功
		[alex]>>>get Python-3.5.1.tar
		已接收0%，4096字节
		已接收0%，8192字节
		已接收0%，12288字节
		已接收0%，16384字节
		已接收0%，20480字节
		已接收0%，24576字节
		已接收0%，28672字节
		已接收0%，32768字节
		已接收0%，36864字节
		已接收0%，40960字节
		已接收0%，45056字节
		已接收0%，49152字节
		已接收0%，53248字节
		已接收0%，57344字节
		已接收0%，61440字节
		已接收0%，65536字节
		已接收0%，69632字节
		已接收0%，73728字节
		已接收0%，77824字节
		已接收0%，81920字节
		已接收0%，86016字节
		已接收0%，90112字节
		已接收0%，94208字节
		已接收0%，98304字节
		已接收0%，102400字节
		已接收0%，106496字节
		已接收0%，110592字节
		已接收0%，114688字节
		已接收0%，118784字节
		已接收0%，122880字节
		已接收0%，126976字节
		已接收0%，131072字节
		已接收0%，135168字节
		已接收0%，139264字节

		#### 用户test
		[root@dev-mysql SelectorFTP]# python3 client/ftp_client.py -s localhost -P10021 -u test -p test
		登入成功
		[test]>>>get test.png
		已接收4%，4096字节
		已接收8%，8192字节
		已接收12%，12288字节
		已接收17%，16384字节
		已接收21%，20480字节
		已接收25%，24576字节
		已接收29%，28672字节
		已接收34%，32768字节
		已接收38%，36864字节
		已接收42%，40960字节
		已接收47%，45056字节
		已接收51%，49152字节
		已接收55%，53248字节
		已接收59%，57344字节
		已接收64%，61440字节
		已接收68%，65536字节
		已接收72%，69632字节
		已接收77%，73728字节
		已接收81%，77824字节
		已接收85%，81920字节
		已接收89%，86016字节
		已接收94%，90112字节
		已接收98%，94208字节
		已接收100%，95685字节

#####注意：用户设置或添加需要直接修改server/conf/settings.py
		 	
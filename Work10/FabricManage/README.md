## 程序介绍

#### 作者:ToFgetU
#### 版本:示例版本 v0.1
#### 程序功能介绍:
    实现简易的堡垒机功能，。
    功能全部用python的基础知识和面向对象知识实现,用到了os\sys\sparamiko\threading\函数\模块知识
##### 主要功能如下：
###### Fabric 简易主机管理
	1) 远程连接服务器，输入相应的服务器命令，如:df, ifconfig, ls, pwd 等
	2）对连接的远程服务器进行文件的上传下载


#### 程序结构:

	FabricManage #Fabric服务端
	├── bin # 执行文件 目录  	
	│　　├── __init__.py  
	│　　└── f_start.py # 执行程序  
	├── conf #配置文件目录  
	│　　├── __init__.py
	│　　└── settings.py  #配置文件  
	├── core #主要逻辑程序  
     　　├── __init__.py  
     　　├── ftpserver.py  #Fabric功能实现模块 
     　　└── main.py  #Fabric主程序  


#### 测试案例(环境为 python3.6 的环境)：
		------ HOST LIST -----
		[test]
		192.168.128.133
		192.168.128.131
		[test1]
		10.20.2.88
		
		>>> 请选择要执行的主机或主机组: test
		+++++++++++++++++++++++++++++++服务器连接成功++++++++++++++++++++++++++++++++
		
		            ****************************************************
		            * 命令行格式:                                      *
		            *     df -Th                                       *
		            *     ifconfig                                     *
		            *     put filename dest                            *
		            *       ex: put F:/hello.txt /tmp/hello.txt        *
		            *     get filename dest                            *
		            *       ex: get /tmp/hello.txt helloworld.txt      *
		            ****************************************************
		
		>>> 请操作: df -Th
		======================192.168.128.131=======================
		Filesystem           Type   Size  Used Avail Use% Mounted on
		/dev/mapper/vg_devoracle-lv_root
		                     ext4    47G   18G   27G  41% /
		tmpfs                tmpfs  491M  255M  236M  52% /dev/shm
		/dev/sda1            ext4   477M   30M  422M   7% /boot
		
		======================192.168.128.133=======================
		Filesystem           Type   Size  Used Avail Use% Mounted on
		/dev/mapper/vg_devmysql-lv_root
		                     ext4    47G  7.6G   37G  17% /
		tmpfs                tmpfs  491M     0  491M   0% /dev/shm
		/dev/sda1            ext4   477M   30M  422M   7% /boot 
	
		>>> 请操作: exit
		------ HOST LIST -----
		[test]
		192.168.128.133
		192.168.128.131
		[test1]
		10.20.2.88
		
		>>> 请选择要执行的主机或主机组: exit
		退出程序
#####注意：用户设置或添加需要直接修改FabricManage/conf/settings.py
		 	
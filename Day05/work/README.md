作者:ToFgetU
版本:示例版本 v0.1
程序介绍:
    实现增删改查常用功能
    查询功能支持模糊查询和判断查询
    功能全部用python的基础知识实现,os\sys\json\open\函数\模块知识


程序结构:

work #主程目录
├── __init__.py
├── bin # 执行文件 目录
│   ├── __init__.py
│   └── demo.py # 执行程序
|
├── core #主要程序
│   ├── __init__.py
│   ├── main_demo.py  #用于操作增删改查
│   ├── staff_do.py      #增删改查代码逻辑实现模块
|
└── data  #用户数据存储的地方
    └── staff.json


语法限定：
查询：
	#全表查询
	select * from staff_table
	#根据年龄大小
    select name,age from staff_table where age > 22
	#根据部门，姓名
　　select * from staff_table where dept = "IT"
	#模糊查询
    select * from staff_table where enroll_date like "2013"

新增：
	insert into staff_table values ("Alice Li", 27, "13545677654", "IT", "2017-05-15")

更新：
	update staff_table set dept = "Market" where dept = "IT"
	update staff_table set dept = "IT" where name = "Alex Li"

删除：
	#根据名字删除
	delete from table where name = 'Alice Li'
	#根据员工ID删除
    delete from table where staff_id = 5
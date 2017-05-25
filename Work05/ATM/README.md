## 程序介绍

#### 作者:ToFgetU
#### 版本:示例版本 v1.0
#### 程序功能介绍:
    实现ATM基本功能 + 购物车购买调用支付接口功能
    功能全部用python的基础知识实现,用到了time\os\sys\json\logging\函数\模块知识  
##### 主要功能如下：
######	1. ATM管理接口
	1) 新增用户
	2) 删除用户
	3) 调整用户额度
	4) 冻结账户
	5) 解冻账户

######	2. ATM普通用户窗口
	1) 查看账户信息
	2) 提现
	3) 转账
	4) 还款
	5) 账单查询

######	3. 购物车窗口
	1) 查看商品列表购物
	2) 购物车功能
	3) 调用支付接口结账 


#### 程序结构:

	ATM+购物车 #主程目录  
	├── __init__.py  
	├── bin # 执行文件 目录  
	│　　├── __init__.py  
	│　　└── demo.py # 执行程序  
	├── conf #配置文件目录  
	│　　├── __init__.py  
	│　　└── logger_conf.py  #日志配置文件  
	├── logs #日志保存目录  
	│　　└── atm_operation.py  #atm日志文件  
	├── core #主要程序  
	│　　├── __init__.py  
	│　　├── main_demo.py  #主程序入口  
	│　　├── general_windows.py  #atm账户操作模块 不允许管理员用户登入  
	│　　├── manager_windows.py  #管理员窗口操作模块 只允许管理员用户登入  
	│　　├── shopping.py  #购物模块  有单独的购物账户  
	│　　└── login.py     #用户登入验证模块  
	└── data  #用户数据存储的地方  
	　　　├── atm_user.json  #银行账户数据  
	　　　├── billing_info.json  #银行账户操作信息数据  
	　　　├── shopping.json  #商品数据  
	　　　├── shopping_info.json  #用户购买记录  
	　　　├── shopping_tmp.json  #用户购买商品临时购物车记录  
	　　　└── shopping_user.json #商城用户  

#### 测试案例：
	





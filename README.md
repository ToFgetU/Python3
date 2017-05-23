作者:ToFgetU
版本:示例版本 v1.0
程序介绍:
    实现ATM基本功能 + 购物车购买调用支付接口功能
    功能全部用python的基础知识实现,用到了time\os\sys\json\logging\函数\模块知识


程序结构:

ATM+购物车 #主程目录
├── __init__.py
├── bin # 执行文件 目录
│   ├── __init__.py
│   └── demo.py # 执行程序
├── conf #配置文件目录
│   ├── __init__.py
│   └── logger_conf.py  #日志配置文件
├── logs #日志保存目录
│   └── atm_operation.py  #ATM日志文件
├── core #主要程序
│   ├── __init__.py
│   ├── main_demo.py  #主程序入口
│   ├── general_windows.py  #ATM账户操作模块
│   ├── manager_windows.py  #管理员窗口操作模块
│   ├── shopping.py  #购物模块
│   └── login.py     #用户登入验证模块
└── data  #用户数据存储的地方
    ├── atm_user.json  #银行账户数据
    ├── billing_info.json  #银行账户操作信息数据
    ├── shopping.json  #商品数据
    ├── shopping_info.json  #用户购买记录
    ├── shopping_tmp.json  #用户购买商品临时购物车记录
    └── shopping_user.json #商城用户



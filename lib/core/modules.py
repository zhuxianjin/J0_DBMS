#!/usr/bin/env python
#coding: utf-8

from lib.core.classes import Login
from lib.core.classes import DBMS
from lib.core.classes import CLI

# 实例化登录基类，确定用户
login = Login()

# 实例化 DBMS 类，进行数据库初始化操作
dbms = DBMS()

# 实例化命令行接口类，建立交互式环境
cmdline = CLI()


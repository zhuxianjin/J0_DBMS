#!/usr/bin/env python
#coding: utf-8

import os

# DBMS 的 logo 标识
LOGO = """     ___  _______          ______   _______  __   __  _______ 
    |   ||  _    |        |      | |  _    ||  |_|  ||       |
    |   || | |   |        |  _    || |_|   ||       ||  _____|
    |   || | |   |        | | |   ||       ||       || |_____ 
 ___|   || |_|   |        | |_|   ||  _   | |       ||_____  |
|       ||       | _____  |       || |_|   || ||_|| | _____| |
|_______||_______||_____| |______| |_______||_|   |_||_______|

"""

# DBMS 版本号
VERSION = "1.0"

# 当前登录用户名，默认为 J0_DBMS
USER_NAME = "J0_DBMS"

# DBMS 工作目录
PATH = os.getcwd()

# DBMS 参数配置文件
CONFIG_PATH = PATH+"/data/config/config.json"

# 初试数据库目录
SCHEMATA_PATH = PATH+"/data/db/j0db_schemata.xlsx"
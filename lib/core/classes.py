#!/usr/bin/env python
#coding: utf-8

import cmd
import re
import os
import sys
import json
import shlex
import pandas
import hashlib
import getpass
import xlsxwriter
from lib.core.common import VERSION
from lib.core.common import PATH
from lib.core.common import USER_NAME
from lib.core.common import CONFIG_PATH
from lib.core.common import SCHEMATA_PATH
from lib.core.operation import create_database

class DBMS:

    def __init__(self):
        print ("欢迎使用 J0_DBMS! 输入命令以使用。")
        print ("版本："+VERSION)
        self.initdb()
    
    def initdb(self):
        if not os.path.isfile(SCHEMATA_PATH):
            print ("初始化数据库....")
            try:
                schemata_db = xlsxwriter.Workbook(SCHEMATA_PATH)
                schemata_tab = schemata_db.add_worksheet("j0db_user")
                schemata_tab.write(0,0,"username")
                schemata_tab.write(0,1,"password")
                schemata_tab.write(1,0,"j0k3r")
                schemata_tab.write(1,1,hashlib.sha1("j0k3r".encode('utf-8')).hexdigest())
                schemata_db.close()
                print ("初始化成功！")
            except Exception:
                print (Exception)
        
    def create(self):
            print ("call create2")

class Login():

    def __init__(self):
        if not os.path.isfile(CONFIG_PATH):
            print ("配置文件丢失，正在初始化...")
            with open(CONFIG_PATH,'w') as json_file:
                config_data = {}
                config_data['RUN_USERNAME'] = 'J0_DBMS'
                json.dump(config_data,json_file,indent=4)

    
    def start(self):
        username = input("用户名：")
        password = getpass.getpass("密码：")
        password = hashlib.sha1(password.encode('utf-8')).hexdigest()
        schemata_db = pandas.read_excel(SCHEMATA_PATH)
        user_list = schemata_db.values
        for line in user_list:
            if line[0] == username and password == line[1]:
                print ("登录成功，"+username)
                with open(CONFIG_PATH) as json_file:
                    config_data = json.load(json_file)
                    config_data['RUN_USERNAME'] = username
                with open(CONFIG_PATH,'w') as outfile:
                    json.dump(config_data,outfile,indent=4)
                return 
        print ("登录失败")
        exit()


class CLI(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        # 设置命令提示符
        with open(CONFIG_PATH) as json_file:
            RUN_USERNAME = json.load(json_file)['RUN_USERNAME']
        self.prompt = "\033[96m%s#\033[93m>>\033[0m \033[0m" % (RUN_USERNAME)
        #self.prompt = "J0_DBMS#>> "
        self.intr = ""

        # 输出帮助信息
        print ("输入help或h查看命令")

    def do_help(self, args):
        if args == "":
            print ("帮助")
            print ("-------------------------------------------") 
            print ("增：")
            print ("create database [数据库名]         创建新数据库")
            print ("create table [表名] ( [字段名] [字段类型] , [字段名] [字段类型], ... )  创建新表")
            print ("其他：")
            print ("quit或q                              退出程序")
            print ("-------------------------------------------")
        else:
            print ("找不到命令")

    def do_create(self,args):
        # 判断要 create 的类型
        try:
            datatype = shlex.split(args)[0]
            print (datatype)
            if datatype == 'database':
                create_database(shlex.split(args)[1])
            elif datatype == 'table':
                data = re.findall(r'\((.*?)\)', args)[0]
                print (data)
            else:
                print ("语句错误")
        except Exception:
            Exception

    def do_EOF(self, line):
        return True
    
    def emptyline(self):
        pass
 
    def do_quit(self, args):
        ("退出程序")
        sys.exit()
        
    do_q = do_quit
    do_h = do_help

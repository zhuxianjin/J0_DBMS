#!/usr/bin/env python
#coding: utf-8

import os
import time
import xlsxwriter
from lib.core.common import PATH

def is_database_exist(database_name):
    if os.path.isfile(PATH+"/data/db/%s.xlsx" % (database_name)):
        return True
    else:
        return False

def create_database(database_name):
    if is_database_exist(database_name):
        print ("数据库已存在")
        return
    try:
        start = time.time()
        new_db = xlsxwriter.Workbook(PATH+"/data/db/%s.xlsx" % (database_name))
        new_db.close()
        end = time.time()
        print  ("`%s` 创建成功! " % database_name)
        print ("耗时：%.3f" % (end-start))
    except Exception as ex:
        print (ex)

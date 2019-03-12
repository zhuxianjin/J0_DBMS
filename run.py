#!/usr/bin/env python
#coding: utf-8

from __future__ import print_function
from lib.core.modules import login
from lib.core.modules import dbms
from lib.core.modules import cmdline
from lib.core.common import LOGO
from lib.core.common import PATH

def main():
    print ("程序目录："+PATH)
    print (LOGO)
    login.start()
    while True:
        try:
            cmdline.cmdloop()
        except KeyboardInterrupt:
            print ("使用 quit或q 退出程序")

if __name__ == '__main__':
    main()

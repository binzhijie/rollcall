import os
import sys
import time
from configparser import ConfigParser

class jilu_start:
    def __init__(self, name):
        self.name = name
        self.conf = ConfigParser()
        self.conf.read('config.ini',encoding='gbk')
        jilu = eval(self.conf['options']['jilu'])
        if jilu:
            self.jilu(self.name)

    def jilu(self,name):
        path = r'jilu'
        havefile = os.path.exists(path)
        if not havefile:
            os.makedirs(path)
        self.jilufile = open(f'{path}/{name}','a+',encoding='ansi')

    def append_name(self,append_name):
        time_now = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime())
        self.jilufile.write(f'[{time_now}]  Name:{append_name}\n')

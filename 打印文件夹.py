# coding:utf-8

import os

dir = input('请输入目录:')
dir_list = os.listdir(dir)
for child_file in dir_list:
    path = os.path.join(dir,child_file)
    print(path)

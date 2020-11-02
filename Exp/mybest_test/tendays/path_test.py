#encoding:utf-8
import os

path_a =  'img' + os.path.sep
if not os.path.exists(path_a):
    os.makedirs(path_a)
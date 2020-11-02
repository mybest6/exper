#encoding:utf-8
from hashlib import md5
name = "123我"
print(md5(name.encode("utf_8")).hexdigest())
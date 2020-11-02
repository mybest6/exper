#encoding:utf-8
str1 = 'http://so.39.net/search/wd?words='
str2 = '&start=1'
with open('dingx.txt', 'r+') as f:
  for line in f.readlines():
    line = line.strip()
    a = str1 + line+ str2
    f.write(a)
    f.write('\n')
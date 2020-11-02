#encoding:utf-8

def process(s):
    import time
    import re
    if '回复 : 'in s:
        s = s.split('回复 : ')[-1].strip()
        s = s.split('|')[0].strip()
        sum1 = re.findall(r'.*(\d+).*',s)
        return sum1[0]
print(process('楼主|                                                发表于 : 2016-01-06                                                |查看 : 849                                                |回复 :                                                 1                                                |倒序浏览'))
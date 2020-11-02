#encoding:utf-8
def process(s):
    if '发表于' in s:
        return s.split('发表于')[-1].strip()

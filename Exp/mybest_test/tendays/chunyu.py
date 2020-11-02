#encoding:utf-8
def process(res):
    import re
    res = re.findall('(\d+-\d+-\d+)',res)
    res = "{} 00:00:00".format(res[0])

    if res:
        return res

print(process('2018-02-02'))
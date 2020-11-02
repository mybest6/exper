#encoding:utf-8
def process(res):
    import re
    ret = re.findall('\d+-\d+-\d+  \d+:\d+', res)
    ret = ret[0].strip()
    ret = ret.replace('  ',' ')
    time = "{}:00".format(ret)
    if time:
        return time
print(process('2015-04-08  11:43'))
#
# def process(res):
#     import re
#     ret = re.findall('\d+-\d+-\d+', res)
#     ret = "{} 00:00:00".format(ret[0].strip())
#     if ret:
#         return ret
#
# def process(res):
#     import re
#     ret = re.findall('\d+-\d+-\d+', res)
#     if ret:
#         return ret[0]
# def process(s):
#     if s:
#         s = "{}:00".format(s.strip())
#         return s
def process(res):
    import re
    return res.replace('发表于：','')
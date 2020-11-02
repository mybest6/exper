#encoding:utf-8
def process(s):
    if u'视频' in s:
        s = s.split(u'视频')[0].strip()
        return s

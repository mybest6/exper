#encoding:utf-8
def process(s):
    for i in s.split("<em>"):
        if "回答数量：" in i:
            return s.split("回答数量：")[-1].strip()


def process(res):
    if res == 'iask13_woman':
        return '女'
    if res == 'iask13_man':
         return '男'
    else:
        return 'null'

def process(res):
    import re
    ret = re.findall('\d+-\d+-\d+ \d+:\d+:\d+', res)
    if ret:
        return ret[0]

def process(res):
    comp = []
    from datetime import datetime
    import re
    import json
    from lxml import etree
    xp = etree.HTML(res, parser=etree.HTMLParser(encoding="utf-8"))
    dw = xp.xpath('//div[contains(@id,"post_")]/table')
    for i in dw:
        a = {}
        content = i.xpath('.//td[@class="t_f"]')
        if content:
             a['content'] = content[0].xpath("string(.)").strip()
        em_els = i.xpath('.//*[@class="authi"]/em')
        if em_els:
            # todo
            em_els_str = em_els[0].xpath("string(.)")
            ret = re.findall('\d+-\d+-\d+ \d+:\d+:\d+', res)
            match=re.compile(u'[\u4e00-\u9fa5]')
            em_els_time = match.sub('',em_els_str)
            a['time'] = em_els_time

        comp.append(a)
    return json.dumps(comp,indent= 2,ensure_ascii=False)

def process(s):
    if s:
        from dateutil.parser import parse
        ret = parse(s,fuzzy=True)
        return str(ret)

def process(res):
    data = []
    import json
    from lxml import etree
    xp = etree.HTML(res, parser=etree.HTMLParser(encoding="utf-8"))
    dw = xp.xpath('//*[@class="dorawer"]')
    for i in dw:
        replies = {}
        if i.xpath('.//*[@class="dorawer_tit"]/span/text()')[0] == '因不能面诊，医生的建议仅供参考':
            replies['type'] = '医生'
        else:
            replies['type'] = '其他用户'
        cotent = ''
        for txt in i.xpath('.//*[@class="descip paint1"]//text()'):
            cotent += txt.strip()
        replies['content'] = cotent
        replies['date'] = i.xpath('.//*[@class="exask"]/p/text()')[0]
        replies['name'] = i.xpath('.//h3/span/text()')[0]
        first_class_department = i.xpath('//span[@class="department"]//text()')
        if first_class_department:
            replies['first_class_department'] = first_class_department[0]
        else:
            replies['first_class_department']=""
        data.append(replies)
    return data

def process(res):
    import re
    if '女'in res:
        return '女'
    if '男' in res:
        return '男'

def process(s):
    import re
    si = re.findall("(\d+)岁",s)
    if si:
        return si[0].strip()

#encoding:utf-8
def process(s):
    from lxml import etree
    import re
    html = etree.HTML(s,etree.HTMLParser(encoding="utf-8"))
    doc_list_ele = html.xpath('//div[@class="ys_list"]')
    info_list = []
    for doc_ele in doc_list_ele:
        _d = {}
        name = doc_ele.xpath('.//h3')
        first_class_department = doc_ele.xpath('.//h3/em')
        goodat = doc_ele.xpath('.//p')
        content = doc_ele.xpath(".//following-sibling::p[@class='quest_list_main']")
        date = doc_ele.xpath(".//following-sibling::p[2]")
        if name:
         _d["name"] = name[0].text
        if first_class_department:
            _d["first_class_department"] = first_class_department[0].text
        if goodat:
            _d["goodat"] = goodat[0].xpath('string(.)').strip() or None
        if content:
            _d["content"] = content[0].xpath('string(.)')
        if date:
            ret = re.findall("\d+-\d+-\d+ \d+:\d+",date[0].xpath("string(.)"))
            if ret:
                _d["date"] = "{}:00".format(ret[0])
        info_list.append(_d)
    return info_list

def process(s):
    import re
    if s:
        ret = re.findall("\d+-\d+-\d+ \d+:\d+",s)
        s = "{}:00".format(ret)
        return s
def process(s):
    import re
    if s:
        s = "{}:00".format(s)
        return s

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
            ret = re.findall('\d+-\d+-\d+ \d+:\d+:\d+', em_els_str)
            a['time'] = ret
        comp.append(a)
    return json.dumps(comp,indent= 2,ensure_ascii=False)

def process(s):
    import re
    if s:
        ret = re.findall("(\d+)",s)
        if ret:
                return ret[0]


def process(s):
    import re
    if u"阅读数 : " in s:
        k = s.split(u"阅读数 : ")[-1]
        ret = re.findall("(\d+)",k)
        return ret[0]


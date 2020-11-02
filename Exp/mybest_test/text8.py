#encoding:utf-8
def process(res):
    comp = []
    import time
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
            create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(ret[0],"%Y-%m-%d %H:%M:%S"))
            # ret =time.strftime('%Y-%m-%d %H:%M:%S',ret[0])
            a['time'] = create_time
        agrees_list = i.xpath('.//a[contains(@class,"replyadd")]/span')
        if agrees_list:
            a['agrees'] =agrees_list[0].xpath("string(.)")
        name_list = i.xpath('.//div[contains(@class,"authi")]/a')
        if name_list:
            a['name'] = name_list[0].xpath("string(.)")
        comp.append(a)
    return comp

def process(res):
    import re
    import time
    ret = re.findall('\d+-\d+-\d+ \d+:\d+:\d+', res)
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(ret[0],"%Y-%m-%d %H:%M:%S"))
    if create_time:
        return create_time

def process(res):
    detail_content = []
    for j in res[0]["dialogs"]:
        content_detail = {}
        content_detail["content"] = j["content"]
        if j["type"] == 0:
            content_detail["type"] = "患者"
        elif j["type"] == 1:
            content_detail["type"] = "医生"
            content_detail["name"] = res[0]["doctor"]["doctor"]["nickname"]
            content_detail["profession"] = res[0]["doctor"]["doctor"]["job_title_name"]
            content_detail["hospital"] = res[0]["doctor"]["doctor"]["hospital_name"]
            content_detail['first_class_department'] = res[0]["doctor"]["doctor"]["section_name"]
        content_detail["date"] = j["create_time"]
        detail_content.append(content_detail)
    return detail_content
#encoding:utf-8
def process(s):
    from lxml import etree
    import json
    import time
    import re
    html = etree.HTML(s,etree.HTMLParser(encoding="utf-8"))
    time_list = html.xpath('//div[@class="dialog-time"]')
    a = []
    su = html.xpath('//div[@class="doctor-body-content"]')
    if su:
        first_class_department = su[1].xpath('string(.)')
        profession = su[0].xpath('string(.)')
        hospital = su[2].xpath('string(.)')
    for i in time_list:
        comp = {}
        s =i.xpath('string(.)')
        if s:
            year = s.split(u"年")[0]
            month = s.split(u"年")[1].split(u"月")[0]
            day = s.split(u"年")[1].split(u"月")[1].split(u"日")[0]
            last = s.split(" ")[-1].strip()
            b = "{}-{}-{} {}:00".format(year,month,day,last)
            create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(b,"%Y-%m-%d %H:%M:%S"))
            comp['time'] = create_time
        content = i.xpath('../following-sibling::div[1]//div[@class="dialog-content"]')
        if content:
            comp['content'] = content[0].xpath('string(.)')
        type_list = u'患者' if i.xpath('../following-sibling::div[1]//div[@class="dialog-user"]') else u'医生'
        if type_list == u'医生':
            comp['first_class_department'] = first_class_department
            comp['profession'] = profession
            comp['hospital'] = hospital
        comp['type'] = type_list
        a.append(comp)
    return a
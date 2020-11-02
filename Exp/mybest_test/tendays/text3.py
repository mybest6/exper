#encoding:utf-8
def process(s):
    import json
    a = []
    from lxml import etree
    xp = etree.HTML(s, parser=etree.HTMLParser(encoding="utf-8"))
    items = xp.xpath('//div[contains(@class,"bm-bdr pt20 pb15")]')
    for item in items:
        b = {}
        content_list = item.xpath('.//div[contains(@class,"group-talk-text pr15 f14 wordbreak graydeep")]')
        if content_list:
            content = content_list[0].xpath('string(.)')
            b['content'] = content
        time_list = item.xpath('.//span[contains(@class,"fr gray")]')
        if time_list:
            time = time_list[0].xpath('string(.)')
            b['date'] = time
        name_list = item.xpath('.//a[contains(@class,"dib vm")]')
        if name_list:
            name = name_list[0].xpath('string(.)')
            b['name'] = name

        patient_gender_str = item.xpath('.//dl[contains(@class,"pt5")]')
        if patient_gender_str:
            patient_gender = patient_gender_str[0].xpath('string(.)')
            if u'男' in patient_gender:
                b['patient_gender'] = u'男'
            if u'女' in patient_gender:
                b['patient_gender'] = u'女'
        a.append(b)
    return a
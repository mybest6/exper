#encoding:utf-8
def process(res):
    from lxml import etree
    root = etree.HTML(res, parser=etree.HTMLParser(encoding="utf-8"))
    repliess = []
    root_list = root.xpath('//*[@class="list"]/li')
    for i in root_list:
        for q in i.xpath('.//*[@class="q"]'):
            replies = {'type': '', 'content': '', 'agrees': 0, 'date': '', 'name': '', 'hospital': '', 'profession': '','goodat': ''}
            replies['type'] = '患者'
            replies['content'] = q.xpath('.//p/text()')[0].strip()
            replies['date'] = i.xpath('.//div[@class="date"]/text()')[0].strip()
            repliess.append(replies)
        for a in i.xpath('.//*[@class="a"]'):
            replies = {'type': '', 'content': '', 'agrees': 0, 'date': '', 'name': '', 'hospital': '', 'profession': '','goodat': ''}
            replies['type'] = '医生'
            replies['content'] = a.xpath('.//*[@class="container"]/div[@class="about text"]/text()')[0].strip()
            replies['date'] = a.xpath('.//*[@class="container"]/div[@class="info"]/span[3]/text()')[0].strip()
            replies['name'] = a.xpath('.//*[@class="container"]/div[@class="info"]/span[1]/text()')[0].strip()
            replies['hospital'] = root.xpath('//*[@class="info"]//dl[2]//dd//@title')[0].strip()
            replies['profession'] = root.xpath('//*[@class="info"]/dl/dd/text()')[0].strip()
            replies['first_class_department'] = "".join(root.xpath('//*[@class="info"]//dl[3]//dd//text()')).strip()
            replies['goodat'] = root.xpath('//*[@class="info"]/dl/dd[@class="word-break"]/span/span/text()')[0].strip()
            repliess.append(replies)
    return repliess
#encoding:utf-8
def process(s):
    import time
    def ppp(s):
        import json
        date = json.loads(s).get("content", {}).get("date")
        if date:
            return date
    from lxml import etree
    html = etree.HTML(s)
    dates = html.xpath('//div[@class="p_postlist"]/div/@data-field')
    if dates:
        try:
            xx = ppp(dates[0])
            if xx:
                return xx
            raise Exception
        except:
            import re
            s_code = etree.tostring(html.xpath('//div[@class="post-tail-wrap"]')[0],encoding="utf-8")
            ret = re.findall("\d+-\d+-\d+ \d+:\d+",s_code)
            ret = "{}:00".format(ret[0])
            if ret:
                return ret

def process(s):
    from lxml import etree
    import json
    html = etree.HTML(s, etree.HTMLParser(encoding="utf-8"))
    divss = html.xpath('//div[@class="p_postlist"]/div[@data-field]')
    div_ll = []
    for div in divss:
        item = {}
        try:
            name = div.xpath('.//li[@class="d_name"]/a/text()')
            if name:
                item["name"] = name[0]

            date_str = div.xpath('./@data-field')
            if date_str:
                date = json.loads(date_str[0]).get("content",{}).get("date")
                if date:
                    date  = "{}:00".format(date)
                    item["date"] = date

            content = div.xpath('.//div[contains(@id,"post_content_")]')
            if content:
                item["content"] = content[0].xpath("string(.)")

        except:
            continue
        else:
            div_ll.append(item)
    return div_ll
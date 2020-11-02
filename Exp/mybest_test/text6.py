#encoding:utf-8
import requests
import json
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
}

response = requests.get('http://so.39.net/search/wd?words=%E7%B3%96%E5%B0%BF%E7%97%85+%E8%A1%80%E7%B3%96', headers=headers)
html = response.content

html = etree.HTML(html,etree.HTMLParser(encoding="utf-8"))
doc_list= html.xpath('//script[@type="text/javascript"]')
for i in doc_list:
    print(i.xpath('string(.)'))
di_dict = json.loads(doc_list)
items_list = di_dict.get("data").get("items")
for item in items_list:
    print(item.get("id"))

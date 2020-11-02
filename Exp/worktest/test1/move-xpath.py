#encoding:utf-8
import time
import requests
import re
import json
from lxml import etree
def get_one_page(url):
    headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parms_page(html):
    com = {}
    xp = etree.HTML(html, parser=etree.HTMLParser(encoding="utf-8"))
    title = xp.xpath('//p[@class="name"]//a/text()')
    ti = xp.xpath('//p[@class="releasetime"]/text()')
    for i in range(10):
        com[title[i]] = ti[i]
    # title = xp.xpath('//li[@class="game-live-item"]//a[@class="title"]//text()')
    return com

def main(offset):
    url = 'http://maoyan.com/board/4?'+str(offset)
    html = get_one_page(url)
    ti = parms_page(html)
    print(ti)



if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(2)



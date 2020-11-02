#encoding:utf-8
import requests
import os
from lxml import etree
import json

proxies = {
    "http":"http://192.168.200.18:3128",
    "https":"http://192.168.200.18:3128"
}

def get_one_page(url):
    # headers = {
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36' }
    response = requests.get(url,proxies = proxies)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parms_page(html):
    a = {}
    root = etree.HTML(html, parser=etree.HTMLParser(encoding="utf-8"))
    id_list =root.xpath('//div[@class="article-page"]/@data-article-pmid')
    if id_list:
        a['id'] = 'https://pubmed.ncbi.nlm.nih.gov/'+id_list[0]
    title_list= root.xpath('//h1[@class="heading-title"]')
    if title_list:
        title = title_list[0].xpath('string(.)').strip()
        a['title'] = title
    return a
    # return json.dumps(a,indent=4,ensure_ascii=False)

def main():
    with open('out.txt','r+') as f:
        for line in f.readlines():
            line = line.strip()
            # line = line.split(".",1)[-1].strip().split('.',1)[0].strip()
            # print(line)
            url= 'https://pubmed.ncbi.nlm.nih.gov/'+'?term='+line
            html = get_one_page(url)
            id = parms_page(html)
            print(id.get('id'),id.get('title'))


main()


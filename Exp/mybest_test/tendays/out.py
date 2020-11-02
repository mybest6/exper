#encoding:utf-8
import requests
from lxml import etree

def get_one_page(url):

    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parms_page(html):
    a = []
    root = etree.HTML(html, parser=etree.HTMLParser(encoding="utf-8"))
    items = root.xpath('//div[@class="docsum-wrap"]')
    for item in items:
        id_list = item.xpath('.//div[@class="docsum-content"]/a/@href')
        id_str = id_list[0]
        a.append(id_str)
    return a

def main():
    with open('out.txt','r+') as f:
        for line in f.readlines():
            line = line.strip()
            url= 'https://pubmed.ncbi.nlm.nih.gov/'+'?term='+line
            html = get_one_page(url)
            id = parms_page(html)
            print(id)
main()

#encoding:utf-8
import requests
import re
from lxml import etree

def get_one_page(url):
    # headers = {
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36' }
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parms_page(html):
    root = etree.HTML(html, parser=etree.HTMLParser(encoding="utf-8"))
    html_parms = re.findall('',root)


def main():
    with open('out.txt','r+',encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            url= 'https://pubmed.ncbi.nlm.nih.gov/'+'?term='+line
            html = get_one_page(url)
            print(html)
main()

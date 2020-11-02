#encoding:utf-8
import requests
import re
import json

def get_one_page(url):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36' }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None

# def parms_page(html):
#     html_parms = re.

def main():
    url= 'http://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)

main()

#encoding:utf-8
import requests
import json
from pyquery import PyQuery as pq
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
    doc = pq(html)
    comp = {}
    data = []
    comp['content'] = doc('.introduction-content').text()
    data.append(comp)
    return json.dumps(data,indent = 2,ensure_ascii=False)

def main():
    url = 'https://www.guahao.com/hospital/introduction/9869cf92-c720-11e1-913c-5cf9dd2e7135000'
    html = get_one_page(url)
    ti = parms_page(html)
    print(ti)


main()

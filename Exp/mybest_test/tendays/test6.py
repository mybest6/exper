import requests
cookies = {
    '_ga': 'GA1.2.1467848695.1600163090',
    'g': '69713_1600163140298',
    'CNZZDATA-FE': 'CNZZDATA-FE',
    'UM_distinctid': '1749127d5b3a65-04b9de5649be98-333769-1fa400-1749127d5b4b86',
    '__jsluid_s': 'c12b17eee2e41dc01b21c8164d4bf35e',
    'Hm_lvt_dfa5478034171cc641b1639b2a5b717d': '1602494068,1603348673',
    '_gid': 'GA1.2.559153155.1603785348',
    'CNZZDATA1256706712': '340177361-1600158783-https%253A%252F%252Fso.haodf.com%252F%7C1603845253',
    'CNZZDATA1914877': 'cnzz_eid%3D1238490554-1600159200-https%253A%252F%252Fwww.haodf.com%252F%26ntime%3D1603845437',
    'Hm_lpvt_dfa5478034171cc641b1639b2a5b717d': '1603849090',
}

headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}
with open('hao.txt',"r") as r:
    for url in r.readlines():
        url = url.strip()
        response = requests.get(url, headers=headers, cookies=cookies)
        url_m = response.url
        print(url_m)
        # if str(url_m) != url:
        #     print(url_m.url)
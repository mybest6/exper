import requests

cookies = {
    '__jsluid_h': 'a4426e51d6fe845e3afce2b32d8fbcde',
    'Hm_lvt_d7682ab43891c68a00de46e9ce5b76aa': '1599790671',
    '__jsluid_s': '8fae3c976f166a1b46ef2736acfccbe7',
    'g': '52371_1600080519686',
    'CNZZDATA-FE': 'CNZZDATA-FE',
    'UM_distinctid': '1748c3b22557f6-0902ac09c3357a-333769-144000-1748c3b2257651',
    '_ga': 'GA1.2.849349986.1600080520',
    'CNZZDATA1914877': 'cnzz_eid%3D1952346548-1600080440-https%253A%252F%252Fwww.haodf.com%252F%26ntime%3D1602494413',
    'newaskindex': '1',
    '_gid': 'GA1.2.34828968.1603695781',
    'Hm_lvt_dfa5478034171cc641b1639b2a5b717d': '1602645365,1603086697,1603695781,1603847662',
    'CNZZDATA1256706712': '1588042411-1600078474-%7C1603850653',
    'Hm_lpvt_dfa5478034171cc641b1639b2a5b717d': '1603861787',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'If-None-Match': 'W/"685-LvoHI6k9Fs2+EXkwcD4qNg"',
}
with open("hao.txt",'r') as r:
    for url in r.readlines():
        url_n= url.strip()
        response = requests.get(url, headers=headers, cookies=cookies)
        print(response.url)
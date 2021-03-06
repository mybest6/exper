#encoding:utf-8
import requests
import json

headers = {
    'authority': 'api-gateway.guahao.com',
    'tongdun-fp': '',
    'x-b3-traceid': '08622ed6460333ea0500d16b4ba025f0',
    'accept-language': 'zh-cn',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'accept': 'application/json, text/plain, */*',
    'weiyi-appid': 'p_h5_weiyi',
    'req-uuid': '0963b120-0089-11eb-81ab-3da2268356a1',
    'x-b3-spanid': '6039e45e153b107d',
    'x-b3-parentspanid': '0500d16b4ba025f0',
    'x-b3-sampled': '1',
    'weiyi-version': '1.04',
    'ab-barrel-ld': '',
    '$weiyi-authtoken': '\\u0021PaS6ojULWUPHkPFcsm7NvjAcKnO6whu3QdqvL1WBvbu8Q7noWeF7QrvTRiuMnPkVwM0tIHx2F-rrpuoh-SwgjKa8USX-spslnCdDBGRyoLylhXUMJG-6ChkCHOE2AKqRBSNNnJ9lT_OvUnRWBS6qW346TxwKILzfKIjzENH8U2rKw',
    'origin': 'https://wy.guahao.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://wy.guahao.com/search?q=%E7%B3%96%E5%B0%BF%E7%97%85&tab=experience&searchType=search&searchRad=1601185949784888&searchUrl=hometop',
}



data = {"q": "糖尿病 血糖", "pageNo": 1, "pageSize": 100, "dynamicFilter": 1, "consultTypes": [0],
        "consultObjects": [0, 1, 3, 4], "status": [2], "logtoken": "1601185949784888", "scene": "main_search_consult"}

response = requests.post('https://api-gateway.guahao.com/consult/consultsearch/list.json', headers=headers, json=data)
print(response.content.decode())

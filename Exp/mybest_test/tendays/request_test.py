#encoding:utf-8
import requests

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
}

response = requests.get('http://data9595.com/curl/', headers=headers, verify=False)
print(response.headers)

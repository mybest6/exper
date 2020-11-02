#encoding:utf-8
import requests
import os

headers = {
    'authority': 'ss0.bdstatic.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'image',
    'referer': 'https://image.baidu.com/',
    'accept-language': 'zh-CN,zh;q=0.9',
}

response = requests.get('https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2398185343,1430368773%5E&fm=26%5E&gp=0.jpg', headers=headers)
dif = 'img'+ os.path.sep +'1'
if not os.path.exists(dif):
    os.makedirs(dif)
address = dif + '2.jpg'
with open(address,'wb') as w:
    w.write(response.content)





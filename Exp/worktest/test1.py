#encoding:utf-8
import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/1234566')
r = s.get('http://httpbin.org/cookies')
print(r.text)
print(type(r.text))
print(r.content)
print(type(r.content))
print(r.json())
print(type(r.json()))
import requests

proxies = {
    "http":"http://192.168.200.18:3128",
    "https":"http://192.168.200.18:3128"
}

resp = requests.get("http://www.google.org/ip",proxies=proxies)
# resp = requests.get("http://www.httpbin.org/ip",proxies=proxies)
print(resp.text)
print(resp.url)



import urllib.request

url = "http://www.baidu.com/s?ie=UTF-8&wd=ip"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
}
proxies = {
    "http": "103.84.217.185:20036"
}
request = urllib.request.Request(url=url, headers=headers)
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
res = opener.open(request)
con = res.read().decode("utf-8")
print(con)
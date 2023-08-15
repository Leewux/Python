import urllib.request
import urllib.parse
import json
url = "https://fanyi.baidu.com/sug"
data = {"kw": "nigger"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
}
# post请求对象必须进行编码再其后加.encode("utf-8")
Data = urllib.parse.urlencode(data).encode("utf-8")
# 定制一个url对象
request = urllib.request.Request(url, Data, headers)
res = urllib.request.urlopen(request)
content = res.read().decode("utf-8")
fin_content =json.loads(content)
print(fin_content)
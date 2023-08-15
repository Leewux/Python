import urllib.request
# 定义一个url,你想要访问的地址
url = "http://www.baidu.com/"
# 模拟浏览器向url发送访问数据
response = urllib.request.urlopen(url)
# 获取响应页面中的源码
"""
    注意,response.read()获取的只是页面源码的二进制数据,需要解码在其后面添加.decode("utf-8")
"""
content = response.read().decode("utf-8")

print(content)
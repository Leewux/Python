from lxml import html
import urllib.request
etree = html.etree
url = "https://www.starbucks.com.cn/menu/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
}
request = urllib.request.Request(url=url, headers=headers)
res = urllib.request.urlopen(request)
con = res.read().decode("utf-8")
startbucks_data = etree.HTML(con)
startbucks_drink_name = startbucks_data.xpath("//div[@class='wrapper fluid margin page-menu-list']//strong/text()")
startbucks_drink_picture = startbucks_data.xpath('//div[@class="wrapper fluid margin page-menu-list"]//div/@style')
for name, picture in zip(startbucks_drink_name, startbucks_drink_picture):
    fn_pic = picture.replace("background-image:", "").strip("'\"")
    print("Name:", name)
    print("Picture URL:", fn_pic)
    print("----------")

# for name in startbucks_drink_name:
#     print(name)
#
# for picture in startbucks_drink_picture:
#     fn_pic = picture.replace("background-image:", "")
#     print(fn_pic)
#
# print(f"{name}+{fn_pic}")
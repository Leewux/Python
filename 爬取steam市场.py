import urllib.request
from lxml import html
import json

def SteamMarket_link(start_count):
    url = f"https://steamcommunity.com/market/search/render/?query=&start={start_count}&count=100&search_descriptions=0&sort_column=popular&sort_dir=desc&appid=730"
    headers = {
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": "sessionid=68d7d9b0fed728ebf9ef4818; timezoneOffset=28800,0; steamCountry=CN%7C2298a895352012fd95f39f49eb9f47d2",
        "Referer": "https://steamcommunity.com/market/search?appid=730",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"99\", \"Microsoft Edge\";v=\"115\", \"Chromium\";v=\"115\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203",
        "X-Prototype-Version": "1.7",
        "X-Requested-With": "XMLHttpRequest"
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request

all_csgo_names = ''
start_page = int(input("开始页(一页一百条数据):"))
end_page = int(input("结束页:"))
for s_start_count in range(start_page, end_page + 1):
    start_count = s_start_count * 100
    res = urllib.request.urlopen(SteamMarket_link(start_count))
    content = res.read().decode("utf-8", "ignore")
    Steam_csgo = open("Steam_csgo.json", "w", encoding="utf-8")
    Steam_csgo.write(content)
    data = json.loads(content)
    Steam_csgo_Html = data["results_html"]
    etree = html.etree
    Steam_csgo = etree.HTML(Steam_csgo_Html)
    Csgo_name = Steam_csgo.xpath('//div[@class="market_listing_item_name_block"]/span[@class="market_listing_item_name"]/text()')
    all_csgo_names += '\n'.join(Csgo_name) + '\n'


with open("Csgo_names.txt", "w", encoding="utf-8") as file:
    file.write(all_csgo_names)




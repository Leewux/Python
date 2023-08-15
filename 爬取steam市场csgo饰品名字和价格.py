import urllib.request
from lxml import html
def Steam_market_link(page):
    url = f"https://steamcommunity.com/market/search?appid=730#p{page}_popular_desc"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "sessionid=68d7d9b0fed728ebf9ef4818; timezoneOffset=28800,0; steamCountry=AR%7C59df21f48796a9fab64ad7067da61b4c; steamLoginSecure=76561198357485768%7C%7CeyAidHlwIjogIkpXVCIsICJhbGciOiAiRWREU0EiIH0.eyAiaXNzIjogInI6MTM5M18yMzA0NkUxM180QzA5QyIsICJzdWIiOiAiNzY1NjExOTgzNTc0ODU3NjgiLCAiYXVkIjogWyAid2ViIiBdLCAiZXhwIjogMTY5MjE4NTM5MywgIm5iZiI6IDE2ODM0NTc5OTYsICJpYXQiOiAxNjkyMDk3OTk2LCAianRpIjogIjE1MjNfMjMwNDZFMjVfNDk2MTkiLCAib2F0IjogMTY5MjA5Nzk5NSwgInJ0X2V4cCI6IDE3MTAxMTI0MDcsICJwZXIiOiAwLCAiaXBfc3ViamVjdCI6ICIzOS4xNDkuMjIzLjEwMCIsICJpcF9jb25maXJtZXIiOiAiMzkuMTQ5LjIyMy4xMDAiIH0.4HBhDfqbUatj-mNfB7AaVJNUuGWPVknaNRvxOsrMGgTgeElM_CS0OB4KWbeadGhvMd7GePn0hk7PTG-bhtvXCw; browserid=2777084736285938298; webTradeEligibility=%7B%22allowed%22%3A1%2C%22allowed_at_time%22%3A0%2C%22steamguard_required_days%22%3A15%2C%22new_device_cooldown_days%22%3A0%2C%22time_checked%22%3A1692097999%7D",
        "Host": "steamcommunity.com",
        "Referer": "https://steamcommunity.com/market/",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"99\", \"Microsoft Edge\";v=\"115\", \"Chromium\";v=\"115\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
    }

    request = urllib.request.Request(url=url, headers=headers)
    return request


start_page = int(input("开始页(一页十条数据):"))
end_page = int(input("结束页:"))
for page in range(start_page, end_page + 1):
    print(page)
    # res = urllib.request.urlopen(Steam_market_link(page))
    # content = res.read().decode("utf-8")

    # etree = html.etree
    # steam_market_csgo_data = etree.HTML(content)
    # steam_market_csgo_name = steam_market_csgo_data.xpath('//div[@class="market_listing_row market_recent_listing_row market_listing_searchresult"]/div[@class="market_listing_item_name_block"]/span[@class="market_listing_item_name"]/text()')
    # steam_market_csgo_nowprice = steam_market_csgo_data.xpath('//div[@class="market_listing_price_listings_block"]/div[@class="market_listing_right_cell market_listing_their_price"]//span[@class="normal_price"]/text()')
    # steam_market_csgo_85price = steam_market_csgo_data.xpath('//div[@class="market_listing_price_listings_block"]/div[@class="market_listing_right_cell market_listing_their_price"]//span[@class="sale_price"]/text()')
    # for name,nowprice,_85price in zip(steam_market_csgo_name,steam_market_csgo_nowprice,steam_market_csgo_85price):
    #     fin_name = name.strip("'")
    #     fin_nowprice = nowprice.strip("¥ ")
    #     fin_85price = _85price.strip("¥ ")
    #     discount = float(fin_85price)/float(fin_nowprice)
    #     formatted_discount = "{:.2f}".format(discount)
    #     print("饰品名称:", fin_name)
    #     print("当前价格:", nowprice)
    #     print("实际到手:", _85price)
    #     print(f"折 扣: 倒余额{formatted_discount}折")
    #     print("-----------------")


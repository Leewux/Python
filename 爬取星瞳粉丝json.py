import urllib.request
def My_request(pn):
    url = f"https://api.bilibili.com/x/relation/fans?vmid=401315430&pn={pn}&ps=50&order=desc&gaia_source=main_web&web_location=333.999&w_rid=7c7a6124e81af869aa3c386b3cc71d7e&wts=1692012771"
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
       "Cookie": "buvid3=DBA39084-FF2F-59A2-E422-875328D064D185334infoc; b_nut=1691757785; i-wanna-go-back=-1; _uuid=1B9D6F69-B126-5957-B85C-D8CE987D154B83808infoc; buvid4=D9695AFF-91B2-D3D8-8DB5-D9E67FC70FFF87009-023081120-iIpDS9YJqHBc75PC%2Fiw1SA%3D%3D; nostalgia_conf=-1; header_theme_version=CLOSE; rpdid=|(YYRuJJR~Y0J'uYmu)|kmlR; b_ut=5; home_feed_column=5; hit-new-style-dyn=1; hit-dyn-v2=1; LIVE_BUVID=AUTO8416919338804625; CURRENT_BLACKGAP=0; fingerprint=9693879bd52c27edbb05c02569d18a77; buvid_fp_plain=undefined; buvid_fp=9693879bd52c27edbb05c02569d18a77; CURRENT_FNVAL=4048; CURRENT_QUALITY=64; browser_resolution=1865-929; b_lsid=A86BF315_189F6C7B23D; bili_ticket=eyJhbGciOiJFUzM4NCIsImtpZCI6ImVjMDIiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2OTIzMjE2MzgsImlhdCI6MTY5MjA2MjQzOCwicGx0IjotMX0.E0csyWJZiIo6G3il3gAOVDR5ONYMvfm38Zq4Bf_erjJZOJZ76Ig19-OIpFQIe5QElToxX7-X4AG-ipNGfR-msXhvi_76Uwug2F_JLNYSjjkZxEvbt-6uCdwR2xOroxCj; bili_ticket_expires=1692321638; bp_video_offset_562318251=829886448683450368; PVID=5; SESSDATA=06faf161%2C1707616556%2Cca5ce%2A82bvpORDC202UbulfZ5chkmWzwMGiRfw6cLGSlbX_KxiKrJ7NaJTVeQD_I_QU4XPy-E_XNfwAAMwA; bili_jct=ed793c5895f81143c29590ab01a46ce0; DedeUserID=562318251; DedeUserID__ckMd5=8288c71b62e70f23; sid=qadi2xeh",
        "Origin": "https://space.bilibili.com",
        "Referer": "https://space.bilibili.com/401315430/fans/fans",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"99\", \"Microsoft Edge\";v=\"115\", \"Chromium\";v=\"115\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request

start_pn = int(input("输入开始页码:"))
end_pn = int(input("输入结束页码:"))
for pn in range(start_pn, end_pn+1):
    res = urllib.request.urlopen(My_request(pn))
    con = res.read().decode("utf-8")
    print(con)
    xtongfans = open("星瞳粉丝.json", "a", encoding="utf-8")
    xtongfans.write(con)

# from lxml import html
# etree = html.etree
# tree = etree.HTML(con)
# result = tree.xpath("//span[@class='fans-name']")
# print(result)


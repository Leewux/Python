import urllib.request
url = "https://api.bilibili.com/x/relation/followings?vmid=562318251&pn=1&ps=20&order=desc&order_type=attention&gaia_source=main_web&web_location=333.999&w_rid=416b40922efa6244670479ec4604e908&wts=1691981778"
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cookie": "buvid3=DBA39084-FF2F-59A2-E422-875328D064D185334infoc; b_nut=1691757785; i-wanna-go-back=-1; _uuid=1B9D6F69-B126-5957-B85C-D8CE987D154B83808infoc; buvid4=D9695AFF-91B2-D3D8-8DB5-D9E67FC70FFF87009-023081120-iIpDS9YJqHBc75PC%2Fiw1SA%3D%3D; nostalgia_conf=-1; header_theme_version=CLOSE; SESSDATA=dcbe6761%2C1707354921%2Cc4b6f%2A823pUSqJRINYX59734o5yWuMQtYCYyn8SNjy3C_Jb23FWGvwtnKLLFyqUE8lFXscl9OqphzAAAMwA; bili_jct=b059475ffeedbc09c655953f12e2bdec; DedeUserID=562318251; DedeUserID__ckMd5=8288c71b62e70f23; sid=8hikr2a6; rpdid=|(YYRuJJR~Y0J'uYmu)|kmlR; bili_ticket=eyJhbGciOiJFUzM4NCIsImtpZCI6ImVjMDIiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE2OTIwNjIxNTYsImlhdCI6MTY5MTgwMjk1NiwicGx0IjotMX0.cqdXhWuCVp7cGOAUNPPB-8IZHgMtx-YDGoSyvDLbIWO0Cqu1qwBRi6ft_nC57UpOhOpS8n2Mqs6Mli7P5Xmudef1gtb9cz2tl7O1dcK5U4qyy27rX3NY0_PgoYY_v-ve; bili_ticket_expires=1692062156; CURRENT_QUALITY=80; b_ut=5; home_feed_column=5; hit-new-style-dyn=1; hit-dyn-v2=1; LIVE_BUVID=AUTO8416919338804625; CURRENT_BLACKGAP=0; browser_resolution=2072-1032; b_lsid=7DF7EA5E_189F1AFE457; CURRENT_FNVAL=4048; bp_video_offset_562318251=829522918350258195; fingerprint=9693879bd52c27edbb05c02569d18a77; buvid_fp_plain=undefined; PVID=1; buvid_fp=9693879bd52c27edbb05c02569d18a77",
    "Origin": "https://space.bilibili.com",
    "Referer": "https://space.bilibili.com/562318251/fans/follow",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"99\", \"Microsoft Edge\";v=\"115\", \"Chromium\";v=\"115\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
}
request = urllib.request.Request(url=url, headers=headers)
res = urllib.request.urlopen(request)
con = res.read().decode("utf-8")
print(con)
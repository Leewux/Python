import urllib.parse
import urllib.request
import json
url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
data = {
    "from": "en",
    "to": "zh",
    "query": "nigger",
    "simple_means_flag": 3,
    "sign": "295895.24806",
    "token": "eaedd698ed2f5ba8f6384353ad5e66c0",
    "domain": "common",
    "ts": 1691934105606
}
# 真正起决定性因素的是cookie
headers = {
    "Accept": "*/*",
    # "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Acs-Token": "1691936394719_1691936392660_l959eOlkkA2Yd4U9LoUj7fSS/UbUVgcB9UFt2DpRTwIC6+YMXzSPwRjKjszD5yI6cQ5zgvgTi1wC0pY3qYTc/BOqZQ7ufizd7aZ3rHpdhhAqu5HxD3jvfkjFX2z+1W9L8kRVkl1UiW1WUC/b/wjI/dmFmvQp8SD+YdKXV4vVjuVmXSFM1hZkEeSitOh3CL56M1L8EZzUJJ6IjGFXIv8XydYEnROJM72uhsbpluQgE0SVA/JWMAQ6CcMA00yXIPs2OKsGIlIymTRZmYP+hMJBlvDpeWnYK72Hj2W7bCWcrdlU++SL5SHvv8I+TDPtQ0H3M34CjfXqE2mDgSbPBvvuOENlr6VTiCRgx25D7xby3RTK5PHhBLp20EwZdEV3Yj8XjklHn7YXhCGcIv1kzcVbJO8Darumy7pJ132EOWH3v50mKN28fB1Wdhuastzw3naoRs4LVBKmogJGE4w7scRxryqZ2Zu1sghOEs4O/m0a4PoKSvnIaMMKwx7fPeBlycJ4EnIn4V+dsBl209sr6BuGlCs9zAC8TuON70GR0lXfRMPZwVcoQULh15poz8VOqoIe",
    "Connection": "keep-alive",
    "Content-Length": "134",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "newlogin=1; BDUSS=Wt4cU9TSm5EWH5YZFVJRmpHT1lMTFliWkZyMjA5MlFENnQ2VHlCWlM0Si10UDFrRVFBQUFBJCQAAAAAAAAAAAEAAAC4W66yX0lET05UQ0FSRUUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH4n1mR-J9ZkW; BDUSS_BFESS=Wt4cU9TSm5EWH5YZFVJRmpHT1lMTFliWkZyMjA5MlFENnQ2VHlCWlM0Si10UDFrRVFBQUFBJCQAAAAAAAAAAAEAAAC4W66yX0lET05UQ0FSRUUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH4n1mR-J9ZkW; BIDUPSID=781511BCABBBB2878A6EC53CC5511B25; PSTM=1691803580; BAIDUID=781511BCABBBB2878A6EC53CC5511B25:SL=0:NR=10:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=781511BCABBBB2878A6EC53CC5511B25:SL=0:NR=10:FG=1; BA_HECTOR=8ga1052k0h0581810l0125071idgeu21o; ZFY=eIiQ6UQY5xp738SFXuu4XsFnUehVLDT5utRPqisA4og:C; delPer=0; PSINO=1; H_PS_PSSID=36544_39113_38831_38879_39114_39118_39038_38918_39205_26350_39138_39137_39100; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1691934087; ab_sr=1.0.1_MzYwNjAyOGY1M2RhNmMzZGVlOGE4YTk2MmMxMTNlMDI5M2NjZmMxMjM5YTc3YzcyOGYwMmM3MTM2MTgyODU5Njc3OGY0ZGZhZWE1ZGJiNTU3MGVmMmZiOGY3YjNhZGNmNDgyZDVhODBiYTExMjZlOGNjYTZjMmQ3MjFhNDBlYmVlYjhhN2UxNGVjOTBmZjA3NGFlZDM2ODZhZDI1OWVlNzY4MTEzMzM2YmEyMzY0YTY2ODE3ZjA4YzVhOTg4MTVh; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1691936392",
    "Host": "fanyi.baidu.com",
    "Origin": "https://fanyi.baidu.com",
    "Referer": "https://fanyi.baidu.com/?aldtype=16047",
    "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"99\", \"Microsoft Edge\";v=\"115\", \"Chromium\";v=\"115\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203",
    "X-Requested-With": "XMLHttpRequest"
}


Data = urllib.parse.urlencode(data).encode("utf-8")
request = urllib.request.Request(url, Data, headers)
res = urllib.request.urlopen(request)
content = res.read().decode("utf-8")
fin_con = json.loads(content)
print(fin_con)
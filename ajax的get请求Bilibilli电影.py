import urllib.request
url = "https://api.bilibili.com/pgc/season/index/result?st=2&style_id=10051&area=-1&release_date=-1&season_status=-1&order=2&sort=0&page=2&season_type=2&pagesize=20&type=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
}
requests = urllib.request.Request(url=url,headers=headers)
res = urllib.request.urlopen(requests)
con = res.read().decode("utf-8")
fin_con = con.replace("},", "},\n")
fp = open("bilibili.json", "w", encoding="utf-8")
fp.write(fin_con)
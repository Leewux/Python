import urllib.request
import urllib.parse
# https://api.bilibili.com/pgc/season/index/result?st=2&
# style_id=10053&area=-1&release_date=-1&season_status=-1&order=2&sort=0&page=1&season_type=2&pagesize=20&type=1
# https://api.bilibili.com/pgc/season/index/result?st=2&
# style_id=10053&area=-1&release_date=-1&season_status=-1&order=2&sort=0&page=2&season_type=2&pagesize=20&type=1
def My_request(page):
    Data = {
        "page": page
    }
    data = urllib.parse.urlencode(Data)
    base_url = f"https://api.bilibili.com/pgc/season/index/result?st=2&style_id=10053&area=-1&release_date=-1&season_status=-1&order=2&sort=0&{data}&season_type=2&pagesize=20&type=1"
    url = base_url
    print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


start_page = int(input("输入开始页码: "))
end_page = int(input("输入结束页码: "))

for page in range(start_page, end_page+1):
    res = urllib.request.urlopen(My_request(page))
    content = res.read().decode("utf-8")
    fin_con = content.replace("},", "},\n")
    bili_download = open("bilibili"+str(page)+".json", "w", encoding="utf-8")
    bili_download.write(fin_con)


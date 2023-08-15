import urllib.request
import urllib.parse


def My_request(cnname, page):
    base_url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
    data = {
        "cname": cnname,
        "pid": "",
        "pageIndex": page,
        "pageSize": 10
    }
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Length": "53",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "route-cell=ksa; Hm_lvt_5fd8501a4e4e0eddf0c4596de7bd57ab=1691975435; Hm_lpvt_5fd8501a4e4e0eddf0c4596de7bd57ab=1691975435; ASP.NET_SessionId=0r53lmifbk5ba2icnhxf0i1o; SERVERID=a8ef50e74cdb73da974d5f9b427a5159|1691977427|1691975402",
        "Host": "www.kfc.com.cn",
        "Origin": "http://www.kfc.com.cn",
        "Referer": "http://www.kfc.com.cn/kfccda/storelist/index.aspx",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203",
        "X-Requested-With": "XMLHttpRequest"
    }
    Data = urllib.parse.urlencode(data).encode("utf-8")
    request = urllib.request.Request(base_url, Data, headers)
    return request


cnname = input("输入您要查询的城市:")
start_page = int(input("输入您要查询开始页码:"))
end_page = int(input("输入您要查询结束页码:"))
for page in range(start_page, end_page+1):
    res = urllib.request.urlopen(My_request(cnname, page))
    content = res.read().decode("utf-8")
    fin_con = content.replace("},", "},\n")
    print(fin_con)
    kfc_location = open("kfc"+cnname+str(page)+".json", "w", encoding="utf-8")
    kfc_location.write(fin_con)


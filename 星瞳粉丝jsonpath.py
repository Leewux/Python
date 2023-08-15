import jsonpath
import json


data = json.load(open("星瞳粉丝.json", "r", encoding="utf-8"))
name = jsonpath.jsonpath(data, "$.data.list[*].uname")
print(name)
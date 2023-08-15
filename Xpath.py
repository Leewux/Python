from lxml import html
etree = html.etree
tree = etree.parse("页面结构.html")
# xpath解析本地文件

#
list_html = tree.xpath('//body//li[@id="1111"]/text()')
print(list_html)
print(len(list_html))
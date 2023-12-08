#!/usr/bin/env python3

import urllib.request as req
import bs4
from datetime import datetime
import os


url = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=8299663&Area=search&mdiv=403&oid=1_2&cid=index&kw=%E7%99%BD%E9%B4%BF2000"
url2 = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=10776280&Area=search&mdiv=403&oid=1_4&cid=index&kw=%E6%BE%8E%E6%BE%8E%20850"
url3 = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=10127162&Area=search&mdiv=403&oid=1_1&cid=index&kw=%E7%99%BD%E9%B4%BF2000"
url4 = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=7040002&Area=search&mdiv=403&oid=1_3&cid=index&kw=%E7%99%BD%E9%B4%BF2000"
url5 = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=8935705&Area=search&mdiv=403&oid=1_1&cid=index&kw=%E6%B3%A1%E8%88%922800"

products = [url, url2, url3, url4, url5]

now = datetime.now()  # 取得當前時間
nowformat = now.strftime("%Y/%m/%d %H:%M:%S")  # 自定義時間格式
print("資料擷取時間: " + nowformat + "\n")

for item in products:
    request = req.Request(item, headers={
        "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0" # 模擬user登入方式
    })

    with req.urlopen(request) as response:
        source = response.read().decode("utf-8")    # 取得網頁原始碼

    root = bs4.BeautifulSoup(source, "html.parser")  # 解析html
    print(root.title.text)    # 顯示MOMO網頁標題

    price = root.find("ul", class_="prdPrice")
    print("目前售價: " + price.span.text + "元\n")   # 顯示當前折扣價格

# print(input(""))


#   if title.a != None:  # 如果標題包含a標籤 (沒有被刪除), 印出來
#       content = title.a.text
#       print(content)
#       with open(output, "a", encoding="utf-8") as book:   # a代表>> (append)    w代表> (write)
#           book.write(content + "\n")  # 印出所有的資料

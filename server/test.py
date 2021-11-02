from urllib import parse
import requests
import re
import pymysql
from requests.api import post
from lxml import etree

mysql_client = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='root1234', database='demo')
cursor = mysql_client.cursor()

sql = "select name, img, href from allink;"
cursor.execute(sql)
data = cursor.fetchall()
for info in data:
    if info[1]:
        continue
    key = info[0]
    url = 'https://www.onlinedown.net/search?searchname={}&button=%E6%90%9C%E7%B4%A2'.format(key)
    print(key, url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    img = html.xpath('//a[@class="img-box"]/img[1]/@src')
    if img:
        sql = "UPDATE allink SET img='{}' WHERE name='{}'".format(img[0], key)
        cursor.execute(sql)
        mysql_client.commit()



mysql_client.close()

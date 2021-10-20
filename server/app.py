# # -*- coding: utf-8 -*-
# # User : monkey  
# # Date : 2021/10/19 10:57 上午
# # Name : app.py
from flask import Flask, render_template
import pymysql
import json

app = Flask(__name__)

mysql_client = pymysql.Connect(host='localhost', port=3306, user='root', passwd='root1234', db='demo')
cursor = mysql_client.cursor()


@app.route('/api/home')
def hello():
    sql = "select name, img, href from allink;"
    cursor.execute(sql)
    data = cursor.fetchall()
    res = list()
    for info in data:
        res.append({
            'name': info[0],
            'img': info[1],
            'href': info[2]
        })
    return json.dumps(res)


@app.route('/user/<name>')
def user(name):
    return {'name': name}




# from urllib import parse
# import requests
# import re


# sql = "select name, img, href from allink;"
# cursor.execute(sql)
# data = cursor.fetchall()
# for info in data:
#     if info[1]:
#         continue
#     key = info[0]
#     url = 'https://ks.pconline.com.cn/download.shtml?q={}'.format(requests.utils.quote(key,encoding='gb2312'))
#     print(key, url)
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
#     }
#     response = requests.get(url, headers=headers)
#     img = re.findall('#src="(.*?)"', response.text)
#     if img:
#         sql = "UPDATE allink SET img='{}' WHERE name='{}'".format('http:' + img[0], key)
#         cursor.execute(sql)
#         mysql_client.commit()





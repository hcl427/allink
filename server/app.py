# # -*- coding: utf-8 -*-
# # User : monkey  
# # Date : 2021/10/19 10:57 上午
# # Name : app.py
from flask import Flask, render_template, request, jsonify
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
    return jsonify(res)


@app.route('/api/send_message', methods=['POST'])
def user():
    data = request.get_json()
    if len(data['msg']) <= 255:
        sql = 'insert into user_message (message) value ("{}")'.format(data['msg'])
        print(sql)
        try:
            cursor.execute(sql)
            mysql_client.commit()
            return jsonify({'success': True})
        except Exception as e:
            print({'success': False, 'msg': e})
            return jsonify({'success': False})
    else:
        return jsonify({'success': False, 'msg': '长度超过限制'})


if __name__ == '__main__':
    app.debug = True
    app.run()


# -*- coding: utf-8 -*-
# User : monkey  
# Date : 2021/10/19 10:57 上午
# Name : app.py
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello'


@app.route('/user/<name>')
def user(name):
    return '你好，{}'.format(name)


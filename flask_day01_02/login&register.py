# coding:utf-8

from flask import Flask,render_template
from pymysql import *
app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')
    # return '哈哈'

@app.route('/reg')
def resgister():
    return render_template('register.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5007,debug=True)
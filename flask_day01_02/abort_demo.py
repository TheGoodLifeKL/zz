# coding:utf-8

from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
    #　通过调用abort函数,可以立即终止执行试图函数,返回前段一个错误信息
    abort(403)
    return 'index page'
@app.errorhandler(404)
def handle_404(e):
    print(e)
    return '发生了404错误'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3859)
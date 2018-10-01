# coding:utf-8

from flask import Flask, abort,make_response,jsonify,url_for,redirect
import json
app = Flask(__name__)

@app.route('/')
def index():
    # return 'index page',404
    # return 'index page','666 kl'
    # return 'index page','666 ',[('itcast','python'),('city','nanyang')]

    # 自己构造响应对象
    resp = make_response('index page python itcast')
    resp.status = '666 itcast python'
    resp.headers['city'] = 'nanyang'
    return resp
@app.route('/person')
def get_person():
    p = {
        'name':'zhangsan',
        'age': 42
    }
    # return json.dumps(p),200,{'Content-Type':'application/json'}
    return jsonify(p)

@app.route('/redirect')
def redirect_index():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
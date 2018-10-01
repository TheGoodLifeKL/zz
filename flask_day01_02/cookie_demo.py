from flask import Flask,make_response,request

app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    resp = make_response('success')
    resp.set_cookie('kl1','12')
    resp.set_cookie('kl2','13',max_age=3600)
    return resp

@app.route('/get_cookie')
def get_cookie():
    cookie = request.cookies.get('kl2')
    return cookie


@app.route('/del_cookie')
def del_cookie():
    resp = make_response('delete success')
    resp.delete_cookie('kl2')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
# coding:utf-8

from flask import Flask,request,abort
import hashlib
WECHAT_TOKEN = "itcast"

app = Flask(__name__)

@app.route('/wechat8004')
def index():
    signature = request.args.get("signature")
    timestamp= request.args.get("timestamp")
    nonce = request.args.get("nonce")
    echostr = request.args.get("echostr")
    
    li = [WECHAT_TOKEN,timestamp,nonce]
    li.sort()
    str = ''.join(li)

    sign = hashlib.sha1(str).hexdigest()

    if signature != sign:
        abort(403)
    else:
        return echostr


if __name__ == '__main__':
    app.run(port=8004)

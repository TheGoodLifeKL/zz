# coding:utf-8
from flask import Flask,current_app,url_for

# 创建flask应用对象
#           模块名，flask会把这个模块所在的目录当做flask工程目录,在工程目录中找静态文件目录static和模板目录templates

app = Flask(__name__,
            static_url_path='/static',
            static_folder='static',
            template_folder='templates',
            )

# 通过文件为flask添加配置参数
# app.config.from_pyfile('Myconfig.cfg')

# 通过对象的方式为flask添加配置参数
class Myconfig(object):
    '''配置信息'''
    DEBUG = True
    ITCAST = 'python1'

app.config.from_object(Myconfig)

# 通过route装饰器,将url路径视图绑定
@app.route('/index')
@app.route('/')
def hello():
    # a = 1/0
    # 在视图函数读取参数
    # print(app.config.get('ITCAST'))
    print(current_app.config.get('ITCAST'))

    return 'hello python'

@app.route('/index')
def hello2():
    return 'hello world'

@app.route('/get',methods=('post','get'))
def post_only():
    '''限制请求方式'''
    return 'post only page'

@app.route('/redirect')
def redirect_post_only():
    return '<a href="%s">post_only</a>' % url_for('post_only')

if __name__ == '__main__':
    # app.run(debug=True)
    print(app.url_map)
    app.run(host='0.0.0.0',port=5277)
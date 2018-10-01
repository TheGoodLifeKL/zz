# coding:utf-8
from flask import Flask,current_app,url_for
from werkzeug.routing import BaseConverter
# 创建flask应用对象
#           模块名，flask会把这个模块所在的目录当做flask工程目录,在工程目录中找静态文件目录static和模板目录templates

app = Flask(__name__)

# 通过文件为flask添加配置参数
# app.config.from_pyfile('Myconfig.cfg')

# 通过对象的方式为flask添加配置参数
class Myconfig(object):
    '''配置信息'''
    DEBUG = True
    ITCAST = 'python1'

app.config.from_object(Myconfig)

# 通过route装饰器,将url路径视图绑定
# @app.route('/<name>')
# def hello(name):
#     return 'hello %s' % name


# @app.route('/id/<int:id>')
# def hello_id(id):
#     return 'hello %s' % id


# 自定义路由转换器
class ReConverter(BaseConverter):
    '''自定义正则转换器'''
    def __init__(self,url_map,*args):
        # 调用父类的初始化方法
        super(ReConverter,self).__init__(url_map)
        # 将传入的参数args　是我们在route中定义的正则表达式,保存到对象的regex中
        self.regex = args[0] #　args[0]就是我们定义的正则表达式
        print(self.regex)

    def to_python(self, value):
        # value = value + '经过to_python添加的内容'
        return value


    def to_url(self, value):
        # value = '123'
        print('to_url时被调用 %s' % value)
        return value


# app中维护的所有路由转换器,converter是一个字典
app.url_map.converters['re'] = ReConverter


@app.route("/id3/<re('\d{3}'):id>/<re('\w{3}'):name>")
def hello_id_3(id,name):
    return 'hello %s %s' % (id,name)

@app.route('/test')
def to_url_test():
    return '<a href="%s">to_url_test</a>' % url_for('hello_id_3',id='456',name='www')



if __name__ == '__main__':
    # app.run(debug=True)
    print(app.url_map)
    app.run(host='0.0.0.0',port=5347)

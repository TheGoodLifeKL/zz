# coding:utf-8

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/index')
def index():
    # return render_template('index.html')
    my_dict = {'a':100}
    my_list = [1,2,3,4,5,6]
    my_int = 1
    context={
        'name':'kl',
        'age':18,
        'my_dict':my_dict,
        'my_list':my_list,
        'my_int':my_int
    }
    return render_template('test.html',**context)

# 自定义过滤器
def filter_list(li):
    return li[::2]

# 第二种自定义过滤器
@app.template_filter('li3')
def filter_list2(li):
    return li[::3]
app.add_template_filter(filter_list,'li_strip')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5400,debug=True)
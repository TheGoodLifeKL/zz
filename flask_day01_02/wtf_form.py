# coding:utf-8
from flask import  Flask,render_template,request
from flask.ext.wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo

app = Flask(__name__)

# 为了使用session,需要设置secret_key
app.config['SECRET_KEY'] = 'asfgfaafh13df'

# 定义表单的类
class RegisterForm(FlaskForm):
    user_name = StringField(label=u'用户名',validators=[DataRequired()])
    password = PasswordField(label=u'密码',validators=[DataRequired()])
    password2 = PasswordField(label=u'确认密码',validators=[DataRequired(),EqualTo('password','密码不一致')])
    submit = SubmitField(label=u'提交')

@app.route('/reg',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html',form=form,errmsg='')
    else:
        if form.validate_on_submit():
            return 'success register'
        else:
            return render_template('register.html',form=form,errmsg=u'填写数据有误')




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

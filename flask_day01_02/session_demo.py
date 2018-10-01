from flask import Flask,session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'jiojiojmlkmlkm325'

@app.route('/login')
def login():
    session['name'] = 'kl'
    session['age'] = 18
    return 'login success'

@app.route('/index')
def index():
    name = session.get('name')
    age = session.get('age')
    return '%s:%s' % (name,age)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
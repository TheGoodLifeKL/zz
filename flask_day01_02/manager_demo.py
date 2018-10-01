from flask import Flask
from flask_script import Manager

app = Flask(__name__)

manage = Manager(app)

@app.route('/index')
def index():
    return 'index page'

if __name__ == '__main__':
    # app.run(host='0.0.0.0',port=5900,debug=True)
    manage.run()

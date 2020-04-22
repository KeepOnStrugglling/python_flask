'''
服务器保持session
    session依赖cookie
'''
from flask import Flask,redirect,url_for,session
app = Flask(__name__)

@app.route('/index1')
def index1():
    session['username'] = 'JoJo'
    return redirect(url_for('index'))

@app.route('/index11')
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run()
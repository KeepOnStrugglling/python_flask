'''
用户登录状态保持
  cookie：存储用户本地数据，纯文本信息，不同域的cookie不能相互访问
'''
from flask import Flask,make_response,request,session,url_for,redirect

app = Flask(__name__)
app.secret_key='azure' # 因报错The session is unavailable because no secret key was set.而添加的

# 设置cookie
@app.route('/cookie')
def cookie():
    resp = make_response('这是一个cookie')
    resp.set_cookie('username','JoJo',max_age=3600) #max_age设置cookie的过期时间,以秒为单位
    return resp

# 获取cookie
@app.route('/request')
def request():
    resp = request.cookies.get('username')
    return resp

# session 操作
@app.route('/index')
def index1():
    session['username'] = 'Dio'
    return 'session set success'

@app.route('/')
def index():
    print(session.get('username'))
    return 'print session'

if __name__ == '__main__':
    app.run(debug=True)
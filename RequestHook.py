'''
请求前后需要做额外的工作，如请求开始连接数据库、权限校验。请求结束指定返回格式等
'''

from flask import Flask,abort
app = Flask(__name__)

# 第一次请求之前调用，可以做一些初始化操作：如数据库连接
@app.before_first_request
def before_first_request():
    print('before_first_request')

# 每次请求前调用，可做校验工作
# 如果校验失败，可以在此方法进行相应，直接return则不会执行视图函数
@app.before_request
def before_request():
    print('before_request')

# 在执行视图函数后调用，并把视图函数生成的响应导入并进行后续的处理
@app.after_request
def after_request(response):
    print('after_request')
    response.headers['Content-Type'] = 'application/json'
    return response     # 必须要将response返回，否则页面将获取不到视图

@app.route('/')
def index():
    return 'Hello'

if __name__ == '__main__':
    app.run(debug=True)
# 导入Flask类、request类、json
from flask import Flask, request, jsonify, redirect, url_for


# 配置对象，定义app添加的一系列配置
class Config(object):
    # 开启调试模式
    DEBUG = True

# 创建一个app应用
# __name__指定程序所在的包
# Flask初始化的参数：
#   import_name Flask程序所在的包
#   static_folder 静态文件存储文件夹，默认static
#   static_url_path 静态文件访问路径，默认static_folder
#   template_folder 模板文件存储文件夹，默认templates
app = Flask(__name__)

# 加载配置方式1：设置配置类，并加载配置对象（最常用）
# app.config.from_object(Config)
# 加载配置方式2：从配置文件中加载配置
# app.config.from_pyfile('config.ini')
# 加载配置方式3：配置指定环境变量名称，注意要在环境变量中新建一个环境变量指向config.ini
# app.config.from_envvar('FLASKCONFIG')
# 加载配置方式4：在app.run()中指定

# 使用装饰器：将路由映射到视图函数
# 如果给路由传递参数（get请求），那么视图函数需要接收参数。如果要限制参数类型，可以在参数前加上类型
# 指定请求方式 GET POST OPTIONS HEAD
@app.route('/demo1/<int:user_id>')
def index(user_id):
    return '{}好好学Python'.format(user_id)

@app.route('/demo2',methods=['GET','POST']) # 指定请求方式为GET POST
def demo2():
    # 从请求中获得请求方式
    return request.method

# 返回json
@app.route('/demo3')
def demo3():
    json_dict = {
        'user_id':10,
        'user_name':'JoJo'
    }
    return jsonify(json_dict)

# 重定向外域
@app.route('/demo4')
def demo4():
    return redirect('https://www.baidu.com')

# 重定向到自己的视图函数
@app.route('/demo5')
def demo5():
    return redirect(url_for('demo2'))

# 自定义状态码
@app.route('/demo6')
def demo6():
    return '状态码为666777888',666777888


if __name__ == '__main__':
    app.run(debug=True,port=8080)   #指定开启调试模式，指定端口号
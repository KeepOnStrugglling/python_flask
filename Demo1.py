'''
正则匹配路由：根据自己的规则限定参数
步骤：
    1.导入转换器基类：Flask的路由匹配规则由转换器对象记录
    2.自定义转换器类继承转换器基类
    3.添加转换器到默认的转换器字典中
    4.使用自定义转换器实现自定义匹配规则
'''

from werkzeug.routing import BaseConverter    # 转换器基类
from flask import Flask

# 自定义转换器
class RegexConverter(BaseConverter):
    def __init__(self,url_map,*args):
        # 重写父类
        super(RegexConverter,self).__init__(url_map)
        # 将第一个接收的参数当作匹配规则进行保存
        self.regex = args[0]
    def to_python(self, value):
        '''该函数中的value值代表匹配的值，可以输出
            匹配完成后，对匹配到参数做最后一步处理再返回
        '''
        return str(value)


# 创建一个app
app = Flask(__name__)

# 将自定义转换器添加到转换器字典中，并指定使用时的名字：re
app.url_map.converters['re'] = RegexConverter

@app.route('/user/<re("[0-9]{3}"):user_id>') # 第一个参数作为匹配规则，含义为参数是3个数字，不满足的不允许访问
def demo1(user_id):
    #a=1/0
    return user_id

# 异常捕捉
# 用状态码进行捕获
@app.errorhandler(404)
def internal_server_error(e):
    return '访问有误'
# 捕获指定的异常
@app.errorhandler(ZeroDivisionError)
def zero_division_error(e):
    return '除数不能为0'

if __name__ == '__main__':
    app.run(debug=True)
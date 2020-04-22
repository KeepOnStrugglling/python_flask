from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    POST = {
        'title':'star',
        'age':2
    }
    mystring = '欧拉欧拉'
    myint = 10
    mylist = [1,2,3,6,5,4,7]
    return render_template('Jinja2模板基本.html',
                           POST=POST,
                           mystring=mystring,
                           myint=myint,
                           mylist=mylist)

@app.route('/index')
def index1():
    myarray = [5,3,58,398,41]
    return render_template('string_filter.html',
                           myarray=myarray)

# 自定义过滤器函数
def do_listrever(li):
    temp_li = list(li)
    temp_li.reverse()
    return temp_li

# 将过滤器函数添加到模板过滤器中
app.add_template_filter(do_listrever,'listrever')

@app.route('/if')
def demo_if():
    comments = [1,2,3,5,5,85,6,8,98]
    post = {
        'title': 'python',
        'stand': 'star',
        'name':'JoJo'
    }
    mylist = [{
        'id':1,
        'value':'hello'
    },
    {
        'id': 2,
        'value': 'world'
    }]
    return render_template('if_loop.html',
                           comments = comments,
                           post = post,
                           mylist = mylist)

if __name__ == '__main__':
    app.run(debug=True)
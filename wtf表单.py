from flask import Flask,request,flash,render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField
from wtforms.validators import DataRequired,EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'azure'
# 配置参数，关闭CSRF校验
#app.config['WTF_CSRF_ENABLED'] = False

# 自定义表单类
class RegisterForm(FlaskForm):
    # 文本字段
    username = StringField('用户名',validators=[DataRequired('请输入用户名')],render_kw={'placeholder':'请输入用户名'})
    # 密码字段
    password = PasswordField('密码',validators=[DataRequired('请输入密码')])
    password2 = PasswordField('确认密码',validators=[DataRequired('请输入确认密码')],)



@app.route('/demo1',methods=['GET','POST'])
def demo1():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if not all([username,password,password2]): # 检验参数是否为空
            flash('参数不足') # 返回报错
        elif password != password2:
            flash('两次密码不一致')
        else:
            print(username,password,password2)
            return 'ok'
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
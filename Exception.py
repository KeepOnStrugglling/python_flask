from flask import Flask
app = Flask(__name__)

# 捕获的状态码
@app.errorhandler(404)
def internal_server_error(e):
    return '访问有误'

if __name__ == '__main__':
    app.run(debug=True)
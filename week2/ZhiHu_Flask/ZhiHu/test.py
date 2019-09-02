from flask import Flask,url_for


app = Flask(__name__)

@app.route('/')
def indexX():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # 显示用户名
    return f'User {username}'

@app.route('/post/<int:post_id>')
#转换器有:int string float path uuid ;默认接受字符串
def show_post(post_id):
    # id 用于比较 所以是整型
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # path 接受斜杠/
    return f'Subpath {subpath}'

@app.route('/projects/')
def projects():
    #加尾部斜杠不会重新定向 会出现404 NOT FOUND错误
    return 'The project page'

@app.route('/about')
def about():
    #不加斜杠会重新定向到前页面
    return 'The about page'


with app.test_request_context():
    #url_for 函数名
    print(url_for('indexX'))
    print(url_for('show_user_profile', username='John Doe'))

from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('app-profile.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/password')
def password():
    return render_template('password.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
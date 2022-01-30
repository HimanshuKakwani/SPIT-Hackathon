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

@app.route('/line-chart')
@app.route('/home/line-chart')
def line_chart():
    return render_template('line-chart.html')

@app.route('/area-chart')
@app.route('/home/area-chart')
def area_chart():
    return render_template('area-chart.html')

@app.route('/bar-chart')
@app.route('/home/bar-chart')
def bar_chart():
    return render_template('bar-chart.html')

@app.route('/nse')
@app.route('/home/nse')
def nse():
    return render_template('nse.html')

@app.route('/nse-2')
@app.route('/home/nse-2')
def nse_2():
    return render_template('nse-2.html')

@app.route('/nse-3')
@app.route('/home/nse-3')
def nse_3():
    return render_template('nse-3.html')


if __name__ == '__main__':
    app.run()
 
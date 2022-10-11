from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect(url_for('home'))

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    error=None
    if request.method == 'POST' :
        if request.form['username'] !='sush' or request.form['password'] !='sush46':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('success'))
    return render_template('login.html',error=error)
    
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/success")
def success():
    return render_template('success.html')
@app.route("/signupsuccess")
def signupsuccess():
    return render_template('signupsuccess.html')

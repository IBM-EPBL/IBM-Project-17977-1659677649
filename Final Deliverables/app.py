from flask import Flask, render_template, redirect, url_for, request
import sqlite3 as sql
app = Flask(__name__)
@app.route("/")
def hello():
    return redirect(url_for('home'))
@app.route("/home")
def home():
    return render_template('index.html')
@app.route("/signup")
def signup():
     return render_template('signup.html')
@app.route("/register",methods=['GET','POST'])
def register():
	if request.method=='POST':
		try:
			Email=request.form['email']
			Name=request.form['usrname']
			Password=request.form['psw']
			Conform_Password=request.form['psw-repeat']
			with sql.connect("Rec.db") as con:
				cur=con.cursor()
				cur.execute("INSERT INTO signup (Email, Name, Password, Conform_Password) VALUES (?,?,?,?)",(Email, Name, Password, Conform_Password))
				con.commit()
		finally:
			return render_template('index.html')
	con.close()

@app.route("/logging",methods=['GET','POST'])
def logging():
	if request.method=='POST':
		try:
			Email=request.form['Email']
			Password=request.form['Password']
			with sql.connect("Rec.db") as con:
				cur=con.cursor()
				cur.execute("INSERT INTO login (Email, Password) VALUES (?,?)",(Email, Password))
				con.commit()
				
		finally:
			return render_template('index.html')
	con.close()		
@app.route("/contact1",methods=['GET','POST'])
def contact1():
	if request.method=='POST':
		try:
			Email=request.form['Email']
			Name=request.form['Name']
			Number=request.form['Number']
			Subject=request.form['Text']
			Message=request.form['Content']
			with sql.connect("Rec.db") as con:
				cur=con.cursor()
				cur.execute("INSERT INTO contact (Email, Name, Number,Subject, Message) VALUES (?,?,?,?,?)",(Email, Name, Number,Subject, Message))
				con.commit()
				
		finally:
			return render_template("index.html")
	con.close()
@app.route("/order",methods=['GET','POST'])
def order():
	if request.method=='POST':
		try:
			Email=request.form['Email']
			Name=request.form['Name']
			Number=request.form['Number']
			Address=request.form['Address']
			Payment=request.form['Payment']
			Product=request.form['Product']
			with sql.connect("Rec.db") as con:
				cur=con.cursor()
				
				cur.execute("INSERT INTO Buy(Email, Name, Number, Address, Payment, Product) VALUES (?,?,?,?,?,?)",(Email, Name, Number, Address, Payment, Product))
				
				con.commit()
				
		finally:
			return render_template("index.html")
		
	con.close()
@app.route('/admin1')
def admin():
    con=sql.connect("Rec.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from signup")  
    signup=cur.fetchall();
    cur.execute("select * from login")  
    login=cur.fetchall();
    cur.execute("select * from contact")  
    contact=cur.fetchall();
    cur.execute("select * from Buy")
    Buy=cur.fetchall();
    return render_template("admin1.html",signup=signup,login=login,contact=contact,Buy=Buy)



@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route("/about")
def about():
    return render_template('#about')

@app.route("/contact")
def contact():
    return render_template('contact.html')
@app.route("/cart")
def cart():
    return render_template('cart.html')
@app.route("/logout")
def logout():
    return render_template('logout.html')
@app.route("/loggedout")
def loggedout():
    return render_template('loggedout.html')
@app.route("/Women")
def Women():
    return render_template('Women.html')
@app.route("/Mens")
def Men():
    return render_template('Mens.html')
@app.route("/Kids")
def kids():
    return render_template('kids.html')
@app.route("/product")
def product():
    return render_template('product.html')
@app.route("/buy")
def buy():
    return render_template('Buy.html')


if __name__=='__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
	
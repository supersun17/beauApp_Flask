from flask import Flask, render_template, request
from webapp import app, mysql


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['POST','GET'])
def login():
    userEmail = request.form['userEmail']
    password = request.form['password']
    cursor = mysql.connect().cursor()
    cursor.execute("select * from User where userEmail='" + userEmail + "'")
    data = cursor.fetchone()
    if data is None:
        return "Please register first"
    else:
        if not password:
            return "Please enter password"
        elif data[2] == password:
                return "Success"
        return "Invalid password"

@app.route('/register', methods = ['POST','GET'])
def register():
    userEmail = request.form['userEmail']
    password = request.form['password']
    userName = request.form['userName']
    print request.form
    cursor = mysql.connect().cursor()
    cursor.execute("select * from User where userEmail='" + userEmail + "'")
    data = cursor.fetchone()
    if data is None:
        cursor.execute("insert into User(userEmail,password,userName) values('sunming3@udel.edu','admin','Ming Sun')")
        #cursor.execute("insert into User(userEmail,password,userName) values('" + userEmail + "','" + password + "','" + userName + "')")
        mysql.connect().commit()
        return "Success"
    else:
        return "The email has been registered"

from flask import Flask,render_template,redirect,request,url_for,session
#import os
import csv
#import sqlite3
import db

#con = sqlite3.connect('login.db')
#db = con.cursor()


app = Flask(__name__)
app.secret_key = 'this is a secret key'

#details = []

#checker = ""

@app.route("/")
def login3():
    if 'store' in session:
        return redirect(url_for("index"))
    else:
        return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/reguser",methods = ["POST"])
def reguser():
    uname = request.form.get("uname")
    fullname = request.form.get("fullname")
    email = request.form.get("email")
    phone = request.form.get("phone")
    password = request.form.get("pass")
    store = uname+password
    file = open("login.csv","a")
    writer = csv.writer(file)
    file2 = open("login.csv","r")
    reader = csv.reader(file2)
    test = False
    for line in reader:
        if(store == line[0]):
            test = True

    if(test):
        file.close()
        file2.close()
        return  render_template("tryagain.html")
    else:
        writer.writerow((store,fullname,email,phone))
        db.createUser(store,fullname,email,phone)
        file.close()
        file2.close()
        return render_template("login.html")

@app.route("/login",methods = ["POST"])
def login1():
    name = request.form.get("uname")
    password = request.form.get("pass")
    store = name+password
    #checker = store
    log = name+password
    file2 = open("login.csv","r")
    reader = csv.reader(file2)
    test = False
    for line in reader:
        if(log == line[0]):
            test = True

    if(test):
        session['store'] = store
        file2.close()
        return redirect(url_for("index"))
    else:
        file2.close()
        return render_template("failure.html")

@app.route("/tryagain")
def tryagain():
    return render_template("tryagain.html")

#@app.route("/profile")
#def profile():
#    if 'store' in session:
#        return render_template("profile.html")
#    else:
#        return render_template("login.html")


@app.route("/profile")
def profile():
    if 'store' in session:
        file2 = open("login.csv","r")
        reader = csv.reader(file2)
        for line in reader:
            if(session['store'] == line[0]):
                name = line[1]
                email = line[2]
                phone = line[3]
                return render_template("profile.html", Name=name,Email=email,Phone=phone)
        #return redirect("/viewprofile")
    else:
        return render_template("login.html")

@app.route("/index")
def index():
    if 'store' in session:
        file2 = open("login.csv","r")
        reader = csv.reader(file2)
        for line in reader:
            if(session['store'] == line[0]):
                name = line[1]
        return render_template("index.html", Name=name)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('store', None)
    return render_template("out.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)

from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'group')
print mysql.query_db("SELECT * FROM users")

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', users = users)


@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/show/<id>')
def show(id):
    query = "SELECT*FROM users where id= :id"
    data = {
        'id':id
    }
    users = mysql.query_db(query, data)
    return render_template('show.html', users = users)

@app.route('/update/<id>')
def update(id):
    query = "SELECT*FROM users where id= :id"
    data = {
        'id':id
    }
    users = mysql.query_db(query, data)
    return render_template('update.html', users = users)


@app.route('/update_user/<id>', methods = ["POST"])
def update_user(id):
    query= "UPDATE users SET f_name = :first, l_name = :last, occupation = :occupation, address = :address, updated_at = NOW() where id = :id"

    data={
        'first':request.form['first'], 'last': request.form['last'], 'occupation': request.form['occupation'], 'address':request.form['address'],
        'id':id
    }
    print data
    users = mysql.query_db(query, data)
    return redirect('/')



@app.route('/add_user', methods=['POST'])
def add_user():
    query= "INSERT INTO users (f_name, l_name, occupation, address, created_at) VALUES(:f_name, :l_name, :occupation, :address, NOW())"

    data={
        'f_name':request.form['first'], 'l_name': request.form['last'], 'occupation': request.form['occupation'], 'address':request.form['address']
    }
    users = mysql.query_db(query,data)
    return redirect('/')

@app.route('/delete/<id>', methods = ['POST'])
def delete(id):
    query = "DELETE FROM users WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')












app.run(debug=True)

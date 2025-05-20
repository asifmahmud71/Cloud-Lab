from flask import Flask, request, render_template_string
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="your-host",
    user="your-user",
    password="your-password",
    database="your-db"
)
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(50), password VARCHAR(50))")

@app.route('/')
def index():
    return '''
    <form action="/register" method="post">
        Register: <input name="username"><input name="password" type="password"><input type="submit" value="Register">
    </form>
    <form action="/login" method="post">
        Login: <input name="username"><input name="password" type="password"><input type="submit" value="Login">
    </form>
    '''

@app.route('/register', methods=['POST'])
def register():
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (request.form['username'], request.form['password']))
    db.commit()
    return "User Registered"

@app.route('/login', methods=['POST'])
def login():
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (request.form['username'], request.form['password']))
    if cursor.fetchone():
        return "Login Successful"
    return "Login Failed"

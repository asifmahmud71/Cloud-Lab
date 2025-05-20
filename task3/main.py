from flask import Flask, request
import psycopg2

app = Flask(__name__)

db = psycopg2.connect(
    host="dpg-d0m4gn0dl3ps73c0rp00-a",
    user="cloud_lab_db_user",
    password="eoMaJikxdfCY1mtTVas3S7dtiuEYDOuz",
    database="cloud_lab_db",
    port = 5432
)
cursor = db.cursor()

# Create users table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(50),
        password VARCHAR(50)
    );
""")
db.commit()

@app.route('/')
def index():
    return '''
    <h2>Register</h2>
    <form action="/register" method="post">
        Username: <input name="username"><br>
        Password: <input name="password" type="password"><br>
        <input type="submit" value="Register">
    </form>
    <h2>Login</h2>
    <form action="/login" method="post">
        Username: <input name="username"><br>
        Password: <input name="password" type="password"><br>
        <input type="submit" value="Login">
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
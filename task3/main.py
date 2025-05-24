from flask import Flask, request
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL
db = psycopg2.connect(
    host="dpg-d0m4gn0dl3ps73c0rp00-a",
    user="cloud_lab_db_user",
    password="eoMaJikxdfCY1mtTVas3S7dtiuEYDOuz",
    database="cloud_lab_db",
    port=5432
)
cursor = db.cursor()

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(50),
        password VARCHAR(50)
    );
""")
db.commit()

# Insert default user if not exists
cursor.execute("SELECT * FROM users WHERE username=%s", ('admin',))
if not cursor.fetchone():
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", ('admin', 'admin123'))
    db.commit()

HTML_STYLE = """
<style>
    body { font-family: Arial, sans-serif; background-color: #f0f2f5; text-align: center; margin-top: 50px; }
    h2, p { color: #333; }
    form { display: inline-block; padding: 20px; background: #fff; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
    input { margin: 10px 0; padding: 8px; width: 90%; border: 1px solid #ccc; border-radius: 4px; }
    input[type="submit"] { background-color: #007bff; color: white; border: none; cursor: pointer; }
    input[type="submit"]:hover { background-color: #0056b3; }
</style>
"""

@app.route('/')
def login_page():
    return HTML_STYLE + '''
    <h2>Login</h2>
    <p><strong>Try with these login credentials:</strong></p>
    <p>Username: <code>admin</code><br>Password: <code>admin123</code></p>
    <form action="/login" method="post">
        <input name="username" placeholder="Enter Username"><br>
        <input name="password" type="password" placeholder="Enter Password"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    if cursor.fetchone():
        return HTML_STYLE + "<h2>Login Successful ✅</h2>"
    return HTML_STYLE + "<h2>Login Failed ❌</h2><p><a href='/'>Try Again</a></p>"

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

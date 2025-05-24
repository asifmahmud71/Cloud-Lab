from flask import Flask, request
import psycopg2

app = Flask(__name__)

db = psycopg2.connect(
    host="dpg-d0m4gn0dl3ps73c0rp00-a",
    user="cloud_lab_db_user",
    password="eoMaJikxdfCY1mtTVas3S7dtiuEYDOuz",
    database="cloud_lab_db",
    port=5432
)
cursor = db.cursor()

# Table create (only once, keep it or comment after creation)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(50),
        password VARCHAR(50)
    );
""")
db.commit()

HTML_STYLE = """
<style>
    body { font-family: Arial, sans-serif; background-color: #f0f2f5; text-align: center; margin-top: 50px; }
    h2 { color: #333; }
    form, .box { display: inline-block; padding: 20px; background: #fff; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
    input { margin: 10px 0; padding: 8px; width: 90%; border: 1px solid #ccc; border-radius: 4px; }
    input[type="submit"], button { background-color: #007bff; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; }
    input[type="submit"]:hover, button:hover { background-color: #0056b3; }
    .note { margin-top: 20px; font-size: 14px; color: #555; }
</style>
"""

@app.route('/')
def login_page():
    return HTML_STYLE + '''
    <div class="box">
        <h2>Login</h2>
        <form action="/login" method="post">
            <input name="username" placeholder="Username"><br>
            <input name="password" type="password" placeholder="Password"><br>
            <input type="submit" value="Login">
        </form>
        <div class="note">
            <p><strong>Try with this login credentials:</strong></p>
            <p>Username: <code>admin</code></p>
            <p>Password: <code>1234</code></p>
        </div>
    </div>
    '''

@app.route('/login', methods=['POST'])
def login():
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", 
                   (request.form['username'], request.form['password']))
    if cursor.fetchone():
        return HTML_STYLE + '''
        <h2>Login Successful ✅</h2>
        <a href="/"><button>Back</button></a>
        '''
    return HTML_STYLE + '''
    <h2>Login Failed ❌</h2>
    <a href="/"><button>Back</button></a>
    '''

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

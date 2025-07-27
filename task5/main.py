from flask import Flask, request
import psycopg2

app = Flask(__name__)

db = psycopg2.connect(
    host="dpg-d230rq3e5dus73a4fom0-a",
    user="cloud_lab_db_user",
    password="R1awkCGCaLry8JAHL8MBQFM0mZ4mMzwD",
    database="cloud_lab_db_74rr",
    port=5432
)
cursor = db.cursor()

# Table create (only once, keep it or comment after creation)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username VARCHAR(50) PRIMARY KEY,
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
    a { color: #007bff; text-decoration: none; }
    a:hover { text-decoration: underline; }
    .note { margin-top: 20px; font-size: 14px; color: #555; }
</style>
"""

@app.route('/')
def signup_page():
    return HTML_STYLE + '''
    <div class="box">
        <h2>Sign Up</h2>
        <form action="/signup" method="post">
            <input name="username" placeholder="Choose a username" required><br>
            <input name="password" type="password" placeholder="Choose a password" required><br>
            <input type="submit" value="Sign Up">
        </form>
        <p><a href="/login">Already have an account? Login</a></p>
    </div>
    '''

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        return HTML_STYLE + '''
        <h2>Signup Successful 🎉</h2>
        <p>You can now <a href="/login">login</a>.</p>
        '''
    except psycopg2.IntegrityError:
        db.rollback()
        return HTML_STYLE + '''
        <h2>Error: Username already exists ❌</h2>
        <a href="/"><button>Try Again</button></a>
        '''
    except Exception as e:
        db.rollback()
        return HTML_STYLE + f'''
        <h2>Signup Failed ❌</h2>
        <p>{str(e)}</p>
        <a href="/"><button>Try Again</button></a>
        '''

@app.route('/login')
def login_page():
    return HTML_STYLE + '''
    <div class="box">
        <h2>Login</h2>
        <form action="/login" method="post">
            <input name="username" placeholder="Username" required><br>
            <input name="password" type="password" placeholder="Password" required><br>
            <input type="submit" value="Login">
        </form>
        <p><a href="/">Don't have an account? Sign up</a></p>
        <div class="note">
            <p><strong>Try these credentials:</strong></p>
            <p>Username: <code>admin</code></p>
            <p>Password: <code>admin123</code></p>
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
        <a href="/login"><button>Back</button></a>
        '''
    return HTML_STYLE + '''
    <h2>Login Failed ❌</h2>
    <a href="/login"><button>Back</button></a>
    '''

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

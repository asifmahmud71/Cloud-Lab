from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML form template for user input
form_template = """
<!doctype html>
<html>
<head><title>Even Numbers Generator</title></head>
<body>
    <h2>Enter how many even numbers you want:</h2>
    <form action="/generate" method="post">
        <input type="number" name="count" min="1" required>
        <input type="submit" value="Generate">
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(form_template)

@app.route('/generate', methods=['POST'])
def generate():
    count = int(request.form['count'])
    evens = [i for i in range(2, 2 * count + 1, 2)]
    return f"<h3>First {count} even numbers:</h3><p>{evens}</p><a href='/'>Back</a>"

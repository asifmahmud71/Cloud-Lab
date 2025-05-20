from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template inside Python using render_template_string
form_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Even Number Generator</title>
    <style>
        body { font-family: Arial; padding: 20px; background: #f2f2f2; }
        form { margin-top: 20px; }
        input[type=number], input[type=submit] {
            padding: 10px;
            margin: 5px;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <h2>Even Number Generator</h2>
    <form action="/generate" method="post">
        <label>Enter how many even numbers:</label><br>
        <input type="number" name="count" min="1" required>
        <input type="submit" value="Generate">
    </form>
</body>
</html>
"""

result_template = """
<!DOCTYPE html>
<html>
<head><title>Result</title></head>
<body>
    <h3>First {{ count }} even numbers:</h3>
    <p>{{ evens }}</p>
    <a href="/">Go Back</a>
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
    return render_template_string(result_template, count=count, evens=evens)

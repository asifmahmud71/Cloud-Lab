from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML form for user input
form_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Even Number Generator</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f8f9fa;
            text-align: center;
            padding: 50px;
        }
        h2 {
            color: #333;
        }
        form {
            margin-top: 20px;
        }
        input[type=number] {
            padding: 10px;
            font-size: 16px;
            width: 200px;
        }
        input[type=submit] {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            margin-left: 10px;
        }
        input[type=submit]:hover {
            background-color: #0056b3;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h2>Even Number Generator</h2>
    <form action="/generate" method="post">
        <input type="number" name="count" min="1" placeholder="Enter a number" required>
        <input type="submit" value="Generate">
    </form>
</body>
</html>
"""

# Result page template
result_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Result</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f0f2f5;
            text-align: center;
            padding: 50px;
        }
        h3 {
            color: #333;
        }
        p {
            font-size: 18px;
            margin-top: 20px;
        }
        a {
            margin-top: 30px;
            display: inline-block;
            color: #007bff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h3>First {{ count }} even numbers:</h3>
    <p>{{ evens }}</p>
    <a href="/">← Go Back</a>
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

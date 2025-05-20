from flask import Flask, render_template_string, request

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            padding: 30px;
        }
        .container {
            background-color: white;
            padding: 25px;
            max-width: 500px;
            margin: auto;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        }
        h2 {
            text-align: center;
            color: #333;
        }
        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin: 12px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            border: none;
            color: white;
            border-radius: 5px;
            font-size: 16px;
        }
        .result {
            margin-top: 20px;
            background-color: #e7f4e4;
            padding: 15px;
            border-left: 5px solid #4CAF50;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>{{ title }}</h2>
        <form method="post">
            <label>Matrix A (e.g., [[1,2],[3,4]]):</label>
            <input type="text" name="matrix_a" required>
            <label>Matrix B (e.g., [[5,6],[7,8]]):</label>
            <input type="text" name="matrix_b" required>
            <button type="submit">Multiply</button>
        </form>
        {% if result %}
            <div class="result">
                <strong>Result:</strong><br>{{ result }}
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    title = "Matrix Multiplication"
    if request.method == 'POST':
        try:
            import ast
            A = ast.literal_eval(request.form['matrix_a'])
            B = ast.literal_eval(request.form['matrix_b'])

            # Multiply matrices
            result_matrix = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
            result = str(result_matrix)
        except Exception as e:
            result = f"Error: {e}"
    return render_template_string(html_template, title=title, result=result)

if __name__ == '__main__':
    app.run(debug=True)

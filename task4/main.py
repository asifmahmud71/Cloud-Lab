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
        input[type="text"], input[type="number"] {
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
            <label>Enter numbers (comma-separated):</label>
            <input type="text" name="numbers" required>
            <label>Enter n (to find nth largest):</label>
            <input type="number" name="n" min="1" required>
            <button type="submit">Find</button>
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
    title = "Nth Largest Number"
    if request.method == 'POST':
        try:
            nums = list(map(int, request.form['numbers'].split(',')))
            n = int(request.form['n'])
            nums.sort(reverse=True)
            if n <= len(nums):
                result = f"{n}th largest number is: {nums[n - 1]}"
            else:
                result = "n is larger than the list size."
        except Exception as e:
            result = f"Error: {e}"
    return render_template_string(html_template, title=title, result=result)

if __name__ == '__main__':
    app.run(debug=True)

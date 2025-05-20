from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <form method="post" action="/find">
        Numbers (comma-separated): <input name="numbers"><br>
        N: <input name="n"><br>
        <input type="submit" value="Find">
    </form>
    '''

@app.route('/find', methods=['POST'])
def find():
    numbers = list(map(int, request.form['numbers'].split(',')))
    n = int(request.form['n'])
    numbers.sort(reverse=True)
    if n > len(numbers):
        return "Not enough numbers"
    return f"{n}th largest number: {numbers[n - 1]}"

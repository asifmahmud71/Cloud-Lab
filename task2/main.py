from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <form method="post" action="/multiply">
        <h3>Matrix A</h3>
        <input name="a11"><input name="a12"><br>
        <input name="a21"><input name="a22"><br>
        <h3>Matrix B</h3>
        <input name="b11"><input name="b12"><br>
        <input name="b21"><input name="b22"><br><br>
        <input type="submit" value="Multiply">
    </form>
    '''

@app.route('/multiply', methods=['POST'])
def multiply():
    a = [[int(request.form[f'a{i}{j}']) for j in range(1, 3)] for i in range(1, 3)]
    b = [[int(request.form[f'b{i}{j}']) for j in range(1, 3)] for i in range(1, 3)]
    result = [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    return f"Result: {result}"

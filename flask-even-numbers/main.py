from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    n = int(request.args.get('n', 10))
    evens = [i for i in range(2, 2*n+1, 2)]
    return f'First {n} even numbers: {evens}'

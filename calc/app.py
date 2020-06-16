# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/math/<func>')
def maths(func):
    print(request.args)
    a = int(request.args['a'])
    b = int(request.args['b'])
    functions = {
        "add" : operations.add(a,b),
        "sub" : operations.sub(a,b),
        "mult" : operations.mult(a,b),
        "div" : operations.div(a,b)
    }
    x = functions.get(func)
    
    return f"{a} and {b} = {x}"


@app.route('/add')
def adds():
    print(request.args)
    a = int(request.args['a'])
    b = int(request.args['b'])
    x = operations.add(a,b)
    return f"{a} and {b} = {x}"

@app.route('/sub')
def subs():
    print(request.args)
    a = int(request.args['a'])
    b = int(request.args['b'])
    x = operations.sub(a,b)
    return f"{a} and {b} = {x}"

@app.route('/mult')
def mults():
    print(request.args)
    a = int(request.args['a'])
    b = int(request.args['b'])
    x = operations.mult(a,b)
    return f"{a} and {b} = {x}"

@app.route('/div')
def divs():
    print(request.args)
    a = int(request.args['a'])
    b = int(request.args['b'])
    x = operations.div(a,b)
    return f"{a} and {b} = {x}"
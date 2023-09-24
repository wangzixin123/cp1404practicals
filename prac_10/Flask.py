from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello World :)</h1>"

@app.route('/greet')
def greet():
    return "Hello"

@app.route('/greet/<name>')
def greet_with_name(name=""):
    return f"Hello {name}"

if __name__ == '__main__':
    app.run()

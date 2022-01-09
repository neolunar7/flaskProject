from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/number')
def hello_number():
    return simple_function(3)


def simple_function(number):
    return number * number


if __name__ == '__main__':
    app.run()

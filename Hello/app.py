from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"
    
@app.route('/06')
def hello06():
    return "Pyae Sone Aung"

if __name__ == '__main__':
    app.run()
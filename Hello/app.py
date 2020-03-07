from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"
    
@app.route('/06')
def hello06():
    return "Pyae Sone Aung"

@app.route("/kmh")
def kmh():
    return "Kyaw Myo Htoo"

if __name__ == '__main__':
    app.run(host="0.0.0.0")
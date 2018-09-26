import flask
app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8888')

from flask import Flask  # type: ignore

app = Flask(__name__)


@app.route("/")
def hello_geek():
    return "<h1>Hello from Flask & Docker 2</h2>"


if __name__ == "__main__":
    # app.run(debug=True)

    app.run(debug=True, host="0.0.0.0")

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Current Time & Date</h1><a href='https://www.pmodwrc.ch'>Website</a>"

if __name__ == "__main__":
    app.run(debug=True)

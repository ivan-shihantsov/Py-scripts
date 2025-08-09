from flask import Flask, app
import os

app = Flask(__name__)


@app.route("/", methods = ['GET'])
def hello_world():
    hostname = os.environ['HOSTNAME']
    appname = os.environ['APP_NAME']
    
    answer = f" hostname: {hostname} <br> appname: {appname}<br>"
    return answer


@app.route("/home")
def home():
    return "<p>home page!!!</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)


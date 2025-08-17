from flask import Flask, app
import os
import socket
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods = ['GET'])
def hello_world():
    hostname = os.environ.get('HOSTNAME', '-')
    appname = os.environ.get('APP_NAME', '-')
    nodeip = os.environ.get('NODE_IP', '-')
    helmver = os.environ.get('HELM_VER', '-')
    pod_ip = socket.gethostbyname(socket.gethostname())

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    answer = f" hostname: {hostname} <br> pod IP: {pod_ip} <br> node IP: {nodeip} <br> appname: {appname} <br> helm revision: {helmver} <br> time: {now} <br>"
    return answer


@app.route("/home")
def home():
    return "<p>home page!!!</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)


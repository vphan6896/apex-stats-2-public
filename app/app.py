import os
import time

from flask import request
from flask import Flask, render_template
import requests
import json
import socket

application = Flask(__name__)
app = application
r = 0
username = ""

@app.route('/search', methods=['POST'])
def search():
    print("Received request.")
    username = request.form['username']
    print("username: %s" % username)
    payload = {'platform': 'ps4', 'name': 'Daltoosh'}
    headers = {"Authorization": "BFJHq1rIGYpCVKeeWgbvfH8i_iXdMTPiZBlWm-n3_gs"}

    r = requests.get('https://www.apexlegendsapi.com/api/v1/player?platform=ps4&name=Daltoosh', headers=headers).text
    r = requests.get('https://api.github.com').text
    r = json.loads(r)
    print("Executed requests: %s" % r['level'])
    return hello()


@app.route("/")
def hello():
    print("Inside hello")
    print("Printing available environment variables")
    print(os.environ)
    print("Before displaying index.html")
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')
    data = search()
    print("Entries: %s" % data)
    return render_template('index.html', display=data)
    return render_template('index.html')


if __name__ == "__main__":
    #app.debug = True
    app.run(host='0.0.0.0', port=8080)


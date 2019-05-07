import os

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
    url = 'https://www.apexlegendsapi.com/api/v1/player?platform=ps4&name=Daltoosh'
    #r = requests.get(url, headers=headers).text
    r = requests.get('https://api.github.com').content
    r = json.loads(r)
    print("Executed requests: %s" % r)
    return r


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
    user_data = search()
    print("Entries: %s" % user_data)
    return render_template('index.html', data=user_data)


if __name__ == "__main__":
    #app.debug = True
    app.run(host='0.0.0.0', port=8080)


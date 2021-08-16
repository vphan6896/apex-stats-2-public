from flask import request
from flask import Flask, render_template
import requests
import json
import socket

application = Flask(__name__)
app = application
r=0
username = 'username here'

@app.route('/search', methods=['POST'])
def search():
    global r
    global username
    print("Received request.")
    username = request.form['username']
    print("username: %s" % username)
    payload = {'platform': 'ps4', 'name': username}
    #headers = {"Authorization": "<AuthToken>"}
    headers = {"TRN-Api-Key": "<API KEY>"}
    #url = 'https://www.apexlegendsapi.com/api/v1/player?platform=ps4&name=<playerName>'
    url = 'https://public-api.tracker.gg/apex/v1/standard/profile/2/%s' % username
    #url = 'https://api.github.com'
    print('about to request')
    try:
        r = requests.get(url, headers = headers).text
        username = "Username: %s" % username
        print('requested')
        r = json.loads(r)
        print('json load')
        r= "Damage done: %.2f" % r["data"]["stats"][4]["value"]
        
    except:
        r = "Error. The player most likely does not exist."
        return hello()
    
    print("Executed requests: %s" % r)
    return hello()


@app.route("/")
def hello():
    print("Inside hello")
    #print("Printing available environment variables")
    #print(os.environ)
    print("Before displaying index.html")
    try:
        #host_name = socket.gethostname()
        #host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', data = r, user=username)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    #app.debug = True
    app.run(host='0.0.0.0', port=8080)

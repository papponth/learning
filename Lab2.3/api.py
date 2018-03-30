import requests
import json
from flask import Flask, jsonify, render_template

def getticket():
    urlforticket = "https://sandboxapic.cisco.com/api/v1/ticket"
    payloadforticket = {"username": "devnetuser", "password": "Cisco123!"}
    response = requests.post(urlforticket, data=json.dumps(payloadforticket), headers=header, verify=False)
    return response.json()['response']['serviceTicket']

def getresponse(req):
        url = 'https://' + urlcontroller + req + ''
        resp = requests.get(url, headers=header, verify=False)
        return resp.json()['response']

if __name__ == '__main__':
    header = {"content-type": "application/json"}
    ticket = getticket()
    print (ticket)
    #ticket = 'ST-13426-3ds3YlrTguWomqqi7alg-cas'
    header['X-Auth-Token'] = ticket
    urlcontroller = "devnetapi.cisco.com/sandbox/apic_em"
    urlhost = "/api/v1/host"
    urlnetworkdevice = "/api/v1/network-device"
    urlphysicaltopology = "/api/v1/topology/physical-topology"


    resphost = getresponse(urlhost)
    respphysicaltopology = getresponse(urlphysicaltopology)
    respnetworkdevice = getresponse(urlnetworkdevice)


    print(resphost)
    print(respnetworkdevice)
    print(respphysicaltopology)

    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("topology.html")

    @app.route('/api/topology')
    def indextopo():
        return jsonify(respphysicaltopology)


    @app.route('/host')
    def indexhost():
        return jsonify(resphost)

    @app.route('/netdev')
    def indexworkdev():
        return jsonify(respnetworkdevice)


    app.run(debug=True)



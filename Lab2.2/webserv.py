import re
import glob
import ipaddress
from flask import Flask, jsonify



def parceconfig (somelinefromfile):
    frsttry = re.match("^\s*ip address ((?:[0-9]{1,3}\.?){4}) ((?:[0-9]{1,3}\.?){4})", str(somelinefromfile))
    scndtry = re.match("^\s*interface (.*)$", str(somelinefromfile))
    thrdtry = re.match("^\s*hostname (.*)$", str(somelinefromfile))
    if bool(frsttry):
        ipwithmask = str(frsttry.group(1)) + "/" + str(frsttry.group(2))
        answer = {"ip": ipaddress.IPv4Interface(ipwithmask)}
    elif bool(scndtry):
        interf = scndtry.group(1)
        answer = {"int": interf}
    elif bool(thrdtry):
        host = thrdtry.group(1)
        answer = {"host": host}
    else:
        answer = {}
    return answer



listofip = []
listofint = []
listofhost = []

addrsofhost = dict()

for file in glob.iglob ("/home/ag/cloud/Seafile/p4ne/p4ne_training/config_files/*.txt"):
    with open(file) as openedfile:
        n = None
        addrlistforhost = []
        for lineinfile in openedfile:
            curline = parceconfig(lineinfile)
            if curline.get("ip"):
                listofip.append (curline)
                addrlistforhost.append (str(curline['ip']))
            elif curline.get("int"): listofint.append (curline)
            elif curline.get("host"):
                listofhost.append (curline)
                n = str(curline['host'])
        if n is not None: addrsofhost[n] =  addrlistforhost


print (listofip)
print (listofint)
print (listofhost)
print (addrsofhost)

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index_main():
    return "some text"


@app.route('/configs')
def index_conf():
    return jsonify(listofhost)


@app.route('/config/<hostname>')
def index_host(hostname):
    return jsonify(addrsofhost[hostname])


app.run(debug=True)


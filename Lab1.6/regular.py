import re
import glob
import ipaddress



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



for file in glob.iglob ("/home/ag/cloud/Seafile/p4ne/p4ne_training/config_files/*.txt"):
    with open(file) as openedfile:
        for lineinfile in openedfile:
            curline = parceconfig(lineinfile)
            if curline.get("ip"): listofip.append (curline)
            elif curline.get("int"): listofint.append (curline)
            elif curline.get("host"): listofhost.append (curline)


print (listofip)
print (listofint)
print (listofhost)





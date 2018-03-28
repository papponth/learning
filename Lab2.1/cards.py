import sys
import pprint
import glob
import requests
import json
from time import sleep

print ('testing with arg')
#cardnum = sys.argv[1]
cardnum = 5182420401527410
cardurl = 'https://lookup.binlist.net/'+str(cardnum)
print ('card number:', cardnum)
print ('url:', cardurl)

req = requests.get(cardurl)
print('HTTP CODE:', req.status_code)
print('Content:')
pprint.pprint(req.json())

banks = list()

for file in glob.iglob ("/home/ag/PycharmProjects/p4ne/Lab2.1/card1.json"):
    with open(file) as openedfile:
        cards = json.load(openedfile)
        for object in cards:
            cardnum = object['CreditCard']['CardNumber']
            cardurl = 'https://lookup.binlist.net/'+str(cardnum)
            req = requests.get(cardurl)
            if len(req.json())>0:
                content = req.json()
                if len(content['bank'])>0:
                    banks.append(content['bank']['name'])
            sleep(1)


print (sorted(list(set(banks))))




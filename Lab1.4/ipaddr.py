from ipaddress import *
from random import *



class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        IPv4Network.__init__(self,(randrange(0x0B000000, 0xDF000000, 1),(randrange(8, 24, 1))),strict=False)

    def regular(self):
        return not (self.is_private or self.is_multicast)




i=0
while i < 50:
    ipnet = IPv4RandomNetwork()
    if ipnet.regular():
        print(ipnet)
        i +=1

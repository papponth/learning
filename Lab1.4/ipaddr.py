from ipaddress import *
from random import *

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        IPv4Network.__init__(self,(randrange(0x0B000000, 0xDF000000, 1),(randrange(8, 24, 1))),strict=False)

    def regular(self):
        return not (self.is_private or self.is_multicast)

ipv4list=[]

while len(ipv4list) < 50:
    ipnet = IPv4RandomNetwork()
    if ipnet.regular():
        ipv4list.append(str(ipnet))

print(sorted(ipv4list))
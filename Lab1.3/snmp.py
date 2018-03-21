from pysnmp.hlapi import *



identity_num = ObjectIdentity ('1.3.6.1.2.1.2.2.1.2')
identity_char = ObjectIdentity ('SNMPv2-MIB', 'sysDescr', 0)



result_get_char = (getCmd(SnmpEngine(),
                          CommunityData('public',mpModel=0),
                          UdpTransportTarget(('10.31.70.107', '161')),
                          ContextData(),
                          ObjectType(identity_char)))


result_next_num = nextCmd(SnmpEngine(),
                          CommunityData('public',mpModel=0),
                          UdpTransportTarget(('10.31.70.107', '161')),
                          ContextData(),
                          ObjectType(identity_num),
                          lexicographicMode=False)



list_result_get_char = list (result_get_char)
list_result_next_num = list (result_next_num)

print (list_result_get_char, '\n')
print (list_result_next_num, '\n')




for k in list_result_get_char:
    for n in k[3]:
        print (n)

print ('\n')

for k in list_result_next_num:
    for n in k[3]:
        print (n[1])



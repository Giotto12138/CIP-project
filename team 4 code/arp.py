'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
import sys
from socket import *
#from scapy import * 
#from arprequest import ArpRequest

# port_scan.py <host> <start_port>-<end_port>
# host = sys.argv[1]
# protstrs = sys.argv[2].splist('-')

# start_port = int(portstrs[0])
# end_port = int(portstrs[1])

target_ip = gethostbyname("192.168.192.154")
start_port = 50
end_port = 80

#the list to record open ports
opened_ports = []
connect_suc = "False"


ar = ArpRequest(target_ip, 'eth0')
print(ar.request())

for port in range(start_port, end_port):
    #sock = socket(AF_INET, SOCK_STREAM)
    sock = socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(port))
    sock.bind(("eth0", target_ip))
    #sock.send(packet)
    #sock = socket(AF_INET, SOCK_DGRAM)
    
    sock.settimeout(10)
    #port_1 = htons(port)    
    result = sock.connect_ex((target_ip, port))
    
    #result = 0 means this port is open
    if result == 0:
        opened_ports.append(port)
        
# if connect to the device with target ip successfully
result = result+1
if result:
    connect_suc = "True"
    
print(connect_suc,"Opened ports:",opened_ports)

# for i in opened_ports:
#     print(i)
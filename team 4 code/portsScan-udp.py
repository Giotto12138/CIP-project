'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
import sys
from socket import *

# port_scan.py <host> <start_port>-<end_port>
# host = sys.argv[1]
# protstrs = sys.argv[2].splist('-'

# start_port = int(portstrs[0])
# end_port = int(portstrs[1])

target_ip = gethostbyname("192.168.192.154")
start_port = 50
end_port = 80

#the list to record open ports
opened_ports = []
connect_suc = "False"

for port in range(start_port, end_port):
    #sock = socket(AF_INET, SOCK_STREAM)
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.settimeout(10)
    #port_1 = htons(port)    
    result = sock.connect_ex((target_ip, port))
    sock.sendto(str.encode("123"),(target_ip,port))
    
    #result = 0 means this port is open
    if result == 0:
        opened_ports.append(port)
        
# if connect to the device with target ip successfully
result = result+1
if result:
    connect_suc = "True"
    
    sock.close()
    
print("whether it can access to the ip:  ",connect_suc,"\nOpened ports:",opened_ports)

# for i in opened_ports:
#     print(i)
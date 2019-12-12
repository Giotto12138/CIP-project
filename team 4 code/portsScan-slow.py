'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
import sys
from socket import *
import time

# port_scan.py <host> <start_port>-<end_port>
# host = sys.argv[1]
# protstrs = sys.argv[2].splist('-'

# start_port = int(portstrs[0])
# end_port = int(portstrs[1])
ip_list = ["192.168.192.155"]
#ip_list = ["192.168.192.153","192.168.192.154"]

for i in ip_list:    
    target_ip = gethostbyname(i)
    start_port = 60
    end_port = 65

    #the list to record open ports
    opened_ports = []
    connect_suc = "False"

    for port in range(start_port, end_port):
        
        print("start port: ",start_port)
        #program stops for every five ports
        if port == start_port+5:
            print("port: ",port)
            time.sleep(3)
            start_port = start_port+5
            print("start port: ",start_port)
            
        #tcp connection
        sock = socket(AF_INET, SOCK_STREAM)
        #udp connection
        #sock = socket(AF_INET, SOCK_DGRAM)
        
        sock.settimeout(10)
        #port_1 = htons(port)    
        result = sock.connect_ex((target_ip, port))
        #sock.send(str.encode("123"),(target_ip,port))
        #sock.sendto(str.encode("hack"),(target_ip,port))
        time.sleep(3)
        
        #result = 0 means this port is open
        if result == 0:
            opened_ports.append(port)
            
    # if connect to the device with target ip successfully
    # because when result = 0, the if statement will take it as false, so we add it by 1 
    result = result+1
    if result:
        connect_suc = "True"
        
        sock.close()
    
    print("whether it can access to", i,":  ",connect_suc)
    print("\nOpened ports:",opened_ports)

# for i in opened_ports:
#     print(i)
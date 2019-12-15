'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
import sys
from socket import *
import time
import subprocess
import datetime
# port_scan.py <host> <start_port>-<end_port>
# host = sys.argv[1]
# protstrs = sys.argv[2].splist('-'

# start_port = int(portstrs[0])
# end_port = int(portstrs[1])

def is_reachable(ip):
    if subprocess.call(["ping","-c","1",ip])==0:#just send one ECHO_REQUEST packets to check
        print("{0} is alive.".format(ip))
        return True
    else:
        print("{0} is unalive".format(ip))
        return False

ip_list = ["192.168.192.153","192.168.192.158","192.168.192.254"]
#ip_list = ["192.168.192.153"]

#print current portscan mode and time
time_stamp = datetime.datetime.now()
print ("\ntime_stamp:     " + time_stamp.strftime('%Y.%m.%d-%H:%M:%S')) 
print("\nnormal portscan")

for i in ip_list:
    connect_suc = "False"
    
    if is_reachable(i):
        target_ip = gethostbyname(i)
        start_port = 1
        end_port = 65535

        #the list to record open ports
        opened_ports = []
        connect_suc = "True"

        for port in range(start_port, end_port):
            
            #tcp connection
            sock = socket(AF_INET, SOCK_STREAM)
            #udp connection
            #sock = socket(AF_INET, SOCK_DGRAM)
            
            sock.settimeout(10)
            #port_1 = htons(port)    
            result = sock.connect_ex((target_ip, port))
	        #result = sock.connect((target_ip, port))
            
            #sock.send(str.encode("123"),(target_ip,port))
            #sock.sendto(str.encode("123"),(target_ip,port))
            #time.sleep(2)
            
            #result = 0 means this port is open
            if result == 0:
                opened_ports.append(port)
        
        print("\nwhether it can access to "+i+": ",connect_suc)
        print("\nOpened ports:",opened_ports)
        
    else:
        print("\nwhether it can access to "+i+": ",connect_suc)
        continue

# for i in opened_ports:
#     print(i)

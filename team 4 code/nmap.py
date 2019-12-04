import nmap
nm = nmap.PortScanner()
ret = nm.scan('114.114.114.114','20')
print (ret)
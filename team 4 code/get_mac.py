from getmac import get_mac_address
eth_mac = get_mac_address(interface="eth0")
win_mac = get_mac_address(interface="Ethernet 3")
ip_mac = get_mac_address(ip="192.168.0.1")
#ip6_mac = get_mac_address(ip6="::1")
host_mac = get_mac_address(hostname="localhost")
updated_mac = get_mac_address(ip="10.0.0.1", network_request=True)

# Enabling debugging
from getmac import getmac
getmac.DEBUG = 2  # DEBUG level 2
print(getmac.get_mac_address(interface="Ethernet 3"))

# Changing the port used for updating ARP table (UDP packet)
from getmac import getmac
getmac.PORT = 44444  # Default: 55555
print(get_mac_address(ip="192.168.0.1", network_request=True))
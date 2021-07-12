import socket
import fcntl
import struct

#class ipTools:

def get_ip_address(ifname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(),
               0x8915,  # SIOCGIFADDR
               struct.pack('256s', bytes(ifname[:15], 'utf-8')))[20:24])
    except:
        return "n/a"

#print(get_ip_address('eth0'))  # '192.168.0.110'
#print(get_ip_address('wlan0'))

#!/usr/bin/python3

import socket

def iphex(ipdd):
     ip_hex=""
     for elem in ipdd.split("."):
         hexstring = '\\x%02X' % int(elem)
         ip_hex=ip_hex+hexstring
     aa1=bytes(ip_hex,'utf-8')
     aa1=aa1.decode('unicode-escape').encode('ISO-8859-1')
     return aa1

ipsource=input("inserisci ip source in formato dd:")
ipdestination=input("inserisci ip destinatio in formato dd:")

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

ip_header  = b'\x45\x00\x00\x28'  # Version, IHL, Type of Service | Total Length
ip_header += b'\xab\xcd\x00\x00'  # Identification | Flags, Fragment Offset
ip_header += b'\x40\x06\xa6\xec'  # TTL, Protocol | Header Checksum

ip_header += iphex(ipsource)  # Source Address
ip_header += iphex(ipdestination)   # Destination Address
tcp_header  = b'\xd5\x87\x03\x3f' # Source Port | Destination Port
tcp_header += b'\x00\x00\x00\x00' # Sequence Number
tcp_header += b'\x00\x00\x00\x00' # Acknowledgement Number
tcp_header += b'\x50\x02\x71\x10' # Data Offset, Reserved, Flags | Window Size
tcp_header += b'\xe6\x32\x00\x00' # Checksum | Urgent Pointer

packet = ip_header + tcp_header
s.bind(('0.0.0.0', 12345))
s.sendto(packet, ('79.27.103.156', 0))

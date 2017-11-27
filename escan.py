# -*- coding: iso-8859-1 -*-
# -*- encoding: utf-8 -*-
#Created By fernando eloi(@eloiindie)
import socket
import sys
import os

print """
  ______                          
 |  ____|                         
 | |__ ______ ___  ___ __ _ _ __  
 |  __|______/ __|/ __/ _` | '_ \ 
 | |____     \__ \ (_| (_| | | | |
 |______|    |___/\___\__,_|_| |_|
 
 #V1.1 Portscan 
      """


ip = raw_input(" Write the ip or address: ")

p21 = [21]
p22 = [22]
p25 = [25]
p26 = [26]
p53 = [53]
p110 = [110]
p135 = [135]
p139 = [139]
p143 = [143]
p3306 = [3306]
p443 = [443]
p445 = [445]
p465= [465]
p587 = [587]
p80 = [80]
p8080 = [8080]
p8443 = [8443]
p993 = [993]
p995 = [995]
p2222 = [2222]
rd = range(2223,65535)
ports = p443 + p80 + p21 + p22 + p8080 + p25 + p26 + p53 + p110 + p143 + p465 + p587 + p3306 + p8443 + p993 + p995 + p2222 + p135 + p139 + p445 + rd

print "PORT  STATE  SERVIE"

for port in p80:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "    open   http");

for port in p8080:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "  open   http-proxy");


for port in p443:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
     
     if code == 0:
         print (str(port)+ "   open   https");

for port in p21:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "    open   ftp");

for port in p22:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "     open   ssh");

for port in p25:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "     open   smtp");

for port in p26:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "    open   rsftp");

for port in p53:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "    open   domain");

for port in p110:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "   open   pop3");

for port in p143:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "   open   imap");

for port in p465:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "   open   smtps");

for port in p587:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "   open   submission");

for port in p3306:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "  open   mysql");


for port in p8443:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "  open   https-alt");


for port in p993:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "   open   imaps");

for port in p995:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "   open   pop3s");



for port in p2222:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "  open   EtherNetIP-1");

for port in p139:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "  open   netbios-ssn");

for port in p135:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "  open   msrpc");

for port in p445:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "  open   microsft-ds");

for port in rd:
     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     client.settimeout(0.6)
     code = client.connect_ex((ip, port))
    
     if code ==0:
         print (str(port)+ "  open   unknow");

print "\nEnd Scanning"

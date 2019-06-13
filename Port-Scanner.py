#We will need these library for creating sockets and pausing the program
import socket
import time

#Our first function will ask for a FQDN, resolve it to an IP then return the IP
def dns_resolve():
  web_address = input('Please enter a website to scan')
  web_address = socket.gethostbyname(web_address) 
  print('The IP Adress of the website is {}'.format(web_address))
  return web_address

#Our second function will ask for a start port and end port, as well as validate the entered range to verify it is valid. This function will then return a list with the start port at location 0 and end port at location 1.
def set_port():
  x = 1
  while (x == 1):
    start_port = input('Please type a port to begin scanning with')
    end_port = input('Please type a port to end scanning at')
    start_port = int(start_port)
    end_port = int(end_port)
    if (start_port < 0 or end_port > 65535):
      print('Port range must be within range 0 to 65535, please try again')
      x == 1
    else:
      x == 0
  return [start_port,end_port]  

#Run this function to run program. Calls our pre-built funtions and creates a socket with the IP address resolved from the FQDN. Returns to screen open ports and non open ports with the reply and port number
def run_time():
  sdns = dns_resolve()
  lport = set_port()
  for port in range(lport[0],lport[1]):
    oconnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    oconnection.settimeout(.9) 
    reply = oconnection.connect_ex((sdns, port))
    if reply == 0:
      print('-'*20,'Port open','-'*20)
      print("Port {} is open".format(port))
      oconnection.close()
      time.sleep(2) 
    else:
      print("Port {} is not open : ERROR code {}".format(port, reply))
  print('-'*20,'Scan complete','-'*20)

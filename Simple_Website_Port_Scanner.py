import socket, time 

adrs= input('Please enter a website to scan')
adrs = socket.gethostbyname(adrs) 
#this will take a website and convert to an ip address
print('The IP Adress of the website is {}'.format(adrs))
pb = input('Please type a port to begin scanning with')
pe = input('Please type a port to end scanning with')
pe = int(pe)
pb = int(pb)
#^takes the port to begin and end with
#creates and connects to ports, prints open and closed ports
for port in range(pb,pe):
  soccer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  soccer.settimeout(.9) #this dictactes how long the program will wait for a responce from a port
  reply = soccer.connect_ex((adrs, port)) #tries ports on a given address
  if reply == 0:
    print('-'*20,'Port open','-'*20)
    print("Port {} is open".format(port))
    soccer.close()
    time.sleep(5) #this will pause the program if a port hits
  else:
    print("Port {} is not open : ERROR code {}".format(port, reply))

print('-'*20,'Scan complete','-'*20)

print(u"\u2603"*20) #this just prints a small snowman for fun

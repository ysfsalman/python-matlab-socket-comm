# Import socket module 
import socket                
import time  

# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 30000         
  
# connect to the server on local computer 
while True:
	try:
		s.connect(('localhost', port))
		break 
	except:
		port +=1
  
# receive data from the server 
x=0
m = bytes()
while True:
    y = [x+1, x+4, x+5]    
    for i in y:
      m += (-i).to_bytes(2,'big',signed=True)
    print(y)
    s.send(m)    
    x = x + 1  
    m =  b''
    time.sleep(0.005)
# close the connection 
s.close()    

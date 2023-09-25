from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
msg = "Hello World"     # compose a message
s.send(msg.encode())    # send the message
data = s.recv(1024)     # receive the response
print(data.decode())    # print the result
s.close()               # close the connection

from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
while True:
    msg = input("Please enter a number: ")
    print("Number received entered: ", msg)
    if msg == "STOP":
        break
    s.send(msg.encode())    # send the message
    print("Client sent {} to the server".format(msg))
    data = s.recv(1024)     # receive the response
    print("Client received result: {}".format(data))
    print(data.decode())    # print the result
s.close()               # close the connection

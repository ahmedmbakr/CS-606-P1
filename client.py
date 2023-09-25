from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
while True:
    msg = input("Please enter a number, space, then number of increments to be done by the server: ")
    if msg == "STOP":
        break
    split_res = msg.split(' ')
    init_num = split_res[0]
    repetition = split_res[1]
    print("Number received entered: {} to be repeated {} times", init_num, repetition)
    
    s.send(msg.encode())    # send the message
    print("Client sent {} to the server".format(msg))
    data = s.recv(1024)     # receive the response
    print("Client received result: {}".format(data))
    print(data.decode())    # print the result
s.close()               # close the connection

import threading
from socket  import *
from constCS import * #-
from multiprocessing import Process
from threading import Thread
import time #-
import random #-

def client_thread_worker(thread_id, addr):
  global msg
  print("Server counts {} in thread {} for connection {}:{}".format(msg, thread_id, addr[0], addr[1]))
  x = 0.0
  t = time.gmtime()  # -
  msg = int(msg)
  s = random.randint(1, 10)
  txt = str(t.tm_min) + ':' + str(t.tm_sec) + ' ' + thread_id + ' is going to sleep for ' + str(s) + ' seconds'  # -
  print(txt)  # -
  t = time.time()
  c = s * 8000000
  for i in range(c):
    x = x + 1.0
  print(time.time() - t)
  t = time.gmtime()  # -
  msg = msg + 1
  txt = str(t.tm_min) + ':' + str(t.tm_sec) + ' ' + thread_id + ' has woken up, seeing shared x being ' + str(msg)  # -
  print(txt)  # -


def handle_client_request(conn, addr):
  global msg
  while True:
    data = conn.recv(1024)  # receive data from client
    if not data:
      break  # stop if client stopped
    msg = data.decode()  # process the incoming data into a response
    sleeplist = list()
    for i in range(20):
      thread_id = "{}:{}.{}".format(addr[0], addr[1], i)
      subsleeper = Thread(target=client_thread_worker, args=(thread_id, addr))
      sleeplist.append(subsleeper)
    for s in sleeplist:
        s.start()
    for s in sleeplist:
        s.join()
    msg = str(msg)
    conn.send(msg.encode())  # return the response
    print("Server sent the result {} to the client".format(msg))
  client_handler.join()
  conn.close()  # close the connection
  print("Connection closed with {}:{}".format(addr[0], addr[1]))


if __name__ == "__main__":
  s = socket(AF_INET, SOCK_STREAM)
  s.bind((HOST, PORT))  # AB: Bind the socket to specific IP address and port.
  s.listen(MAX_NUM_CLIENT_CONNECTIONS_TO_SERVER)  # AB: maximum number of connection to be accepted by siumltaneously by the server.
  while True:                # forever
    print("Server listening on port: {} ...".format(PORT))
    (conn, addr) = s.accept()  # returns new socket and addr. of the client
    print("Accepted connection from {}:{}".format(addr[0], addr[1]))
    client_handler = Process(target=handle_client_request, args=(conn, addr))
    client_handler.start()


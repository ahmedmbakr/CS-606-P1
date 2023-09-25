import threading
from socket  import *
from constCS import * #-


def client_thread_worker(msg):
  return msg + 1


def handle_client_request(conn, addr):
  while True:
    data = conn.recv(1024)  # receive data from client
    if not data:
      break  # stop if client stopped
    msg = data.decode()  # process the incoming data into a response
    current_thread = threading.current_thread()
    thread_id = current_thread.getName()
    print("Server counts {} in thread {} for connection {}:{}".format(msg, thread_id, addr[0], addr[1]))
    updated_msg = client_thread_worker(msg)
    conn.send(updated_msg.encode())  # return the response
  print("Connection closed with {}:{}".format(addr[0], addr[1]))
  conn.close()  # close the connection


if __name__ == "__main__":
  s = socket(AF_INET, SOCK_STREAM)
  s.bind((HOST, PORT))  # AB: Bind the socket to specific IP address and port.
  s.listen(MAX_NUM_CLIENT_CONNECTIONS_TO_SERVER)  # AB: maximum number of connection to be accepted by siumltaneously by the server.
  while True:                # forever
    print("Server listening on port: {} ...".format(PORT))
    (conn, addr) = s.accept()  # returns new socket and addr. of the client
    print("Accepted connection from {}:{}".format(addr[0], addr[1]))
    client_handler = threading.Thread(target=handle_client_request, args=(conn, addr))
    client_handler.start()

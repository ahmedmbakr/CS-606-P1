## P1: Threading

In this project we demonstrate the interaction between a server that accepts more than one connection from the clients.
For each of those connections, the client sends to numbers separated by a space. The first number is the initial number that the server will start counting from. The second number is the number of increments to be done by the server. For example, if the user inputs: `2 10`, this means that it asks the server to start counting from `2` and it will increment the number `10` times. So, after the end of the program, the final result returned by the server is `12`.

The code consists of three main files, as follows:

- `client.py`: The code executed by a client. Their can be many clients running in the same time.
- `server.py`: The code executed by a server. The server can receive many connections from the clients at the same time.
- `constCS.py`: Contains the constant configurations needed by the server and the client. For example the host IP and the server's listening port number. In addition to that, it has the variable `MAX_NUM_CLIENT_CONNECTIONS_TO_SERVER` that defines the total number of connections that can run by the server simultaneously.

To show the code running, a [video is recorded when sharing my screen and uploaded to youtube](https://youtu.be/wb3ICxdmDGM) for easier access. When opening the video, the server is shown on the left side of the screen and three clients are sending requests concurrently to the server.
On top of that, the program allows the clients to send `STOP` messages instead of sending messages to the server to close the connection with the server.

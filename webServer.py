# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
  
    # Prepare a server socket
    serverSocket.bind(("", port))
  
    serverSocket.listen(1)

    while True:
        # Establish the connection
        print('Ready to serve...')

        connectionSocket, addr = serverSocket.accept()
    
        try:
            # Receive message from client
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]
            
            # Open the client requested file in binary mode
            f = open(filename[1:], "rb")

            # Prepare headers for a valid response
            outputdata = b"HTTP/1.1 200 OK\r\n"
            outputdata += b"Content-Type: text/html; charset=UTF-8\r\n"
            outputdata += b"\r\n"  # Blank line to end headers

            connectionSocket.send(outputdata)

            # Send the content of the requested file to the client
            for i in f:
                connectionSocket.send(i)

            f.close()
            connectionSocket.close()  # Close the connection socket
      
        except Exception as e:
            # Send response message for invalid request due to the file not being found (404)
            not_found_response = b"HTTP/1.1 404 Not Found\r\n\r\n"
            connectionSocket.send(not_found_response)
            connectionSocket.close()  # Close the connection socket

if __name__ == "__main__":
    webServer(13331)

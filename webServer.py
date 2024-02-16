# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  # Prepare a server socket
  serverSocket.bind(("", port))
  
  # Start listening for incoming client connections
  serverSocket.listen(1)
  
  while True:
    # Accept a connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    
    try:
      # Receive the request message from the client
      message = connectionSocket.recv(1024).decode()
      filename = message.split()[1]
      
      # Check if the requested file exists
      if filename == "/":
        filename = "/index.html"
      
      # Open the requested file
      try:
        with open(filename[1:], "rb") as f:
          # Send the response message for a valid request
          outputdata = b"HTTP/1.1 200 OK\r\n"
          outputdata += b"Content-Type: text/html; charset=UTF-8\r\n\r\n"
          connectionSocket.send(outputdata)
          
          # Send the content of the requested file to the client
          content = f.read()
          connectionSocket.sendall(content)
      
      # If the requested file does not exist, send a 404 response
      except FileNotFoundError:
        not_found_response = b"HTTP/1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(not_found_response)
        connectionSocket.send(b"<html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1><p>The requested file was not found on this server.</p></body></html>")
      
      # Close the connection socket
      connectionSocket.close()
    
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      not_found_response = b"HTTP/1.1 404 Not Found\r\n\r\n"
      connectionSocket.send(not_found_response)
      
      # Close client socket
      connectionSocket.close()

if __name__ == "__main__":
  webServer(13331)

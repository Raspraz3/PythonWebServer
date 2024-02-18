#Prepare a server socket
serverSocket.bind(("", port))

#Fill in start
serverSocket.listen(1)
#Fill in end

while True:
    #Establish the connection
    
    print('Ready to serve...')#Fill in start -are you accepting connections?     #Fill in end
    connectionSocket, addr = serverSocket.accept()
    
    try:#Fill in start -a client is sending you a message   #Fill in end
      message = connectionSocket.recv(1024).decode()
      filename = message.split()[1]
      
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], "rb") #fill in start #fill in end)
      #fill in end
      outputdata = b"HTTP/1.1 200 OK\r\n"
      outputdata += b"Server: MyWebServer/1.0\r\n"
      outputdata += b"Connection: close\r\n"
      outputdata += b"Content-Type: text/html; charset=UTF-8\r\n"
      outputdata += b"\r\n"
      connectionSocket.send(outputdata)
      for i in f:
        connectionSocket.send(i)
      f.close()
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      not_found_response = b"HTTP/1.1 404 Not Found\r\n"
      not_found_response += b"Server: MyWebServer/1.0\r\n"
      not_found_response += b"Connection: close\r\n"
      not_found_response += b"\r\n"
      connectionSocket.send(not_found_response)
      

      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  #Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)

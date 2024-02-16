from socket import *
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", port))
    serverSocket.listen(1)

    while True:
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]

            # Check if the requested file exists
            if filename == "/":
                filename = "/index.html"
            try:
                f = open(filename[1:], "rb")
            except:
                # Send response message for invalid request due to the file not being found (404)
                not_found_response = b"HTTP/1.1 404 Not Found\r\n\r\n"
                connectionSocket.send(not_found_response)
                connectionSocket.close()
                continue

            # Send response message for valid request
            outputdata = b"HTTP/1.1 200 OK\r\n"
            outputdata += b"Content-Type: text/html; charset=UTF-8\r\n\r\n"
            connectionSocket.send(outputdata)

            # Send the content of the requested file to the client
            with open(filename[1:], "rb") as f:
                content = f.read()
                connectionSocket.sendall(content)

            f.close()
            connectionSocket.close()

        except Exception as e:
            print(e)
            # Close client socket
            connectionSocket.close()

if __name__ == "__main__":
    webServer(13331)

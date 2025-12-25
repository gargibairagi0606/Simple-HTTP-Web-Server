import socket
import os
import mimetypes

HOST = "127.0.0.1"
PORT = 8080
BUFFER_SIZE = 4096

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"HTTP Server running at http://{HOST}:{PORT}")
print(f"Serving files from: {BASE_DIR}")

while True:
    client_socket, addr = server_socket.accept()
    try:
        request = client_socket.recv(BUFFER_SIZE).decode(errors="ignore")
        if not request:
            client_socket.close()
            continue

        request_line = request.splitlines()[0]
        print("Request:", request_line)

        method, path, _ = request_line.split()

        if method != "GET":
            client_socket.sendall(b"HTTP/1.1 405 Method Not Allowed\r\n\r\n")
            client_socket.close()
            continue

        if path == "/":
            path = "/index.html"

        file_path = os.path.join(BASE_DIR, path.lstrip("/"))
        print("File path:", file_path)

        if os.path.isfile(file_path):
            mime_type, _ = mimetypes.guess_type(file_path)
            mime_type = mime_type or "application/octet-stream"

            with open(file_path, "rb") as f:
                content = f.read()

            header = (
                "HTTP/1.1 200 OK\r\n"
                f"Content-Type: {mime_type}\r\n"
                f"Content-Length: {len(content)}\r\n"
                "Connection: close\r\n\r\n"
            )

            client_socket.sendall(header.encode() + content)
        else:
            error_page = b"<h1>404 - File Not Found</h1>"
            client_socket.sendall(
                b"HTTP/1.1 404 Not Found\r\n"
                b"Content-Type: text/html\r\n"
                b"Content-Length: " + str(len(error_page)).encode() + b"\r\n"
                b"Connection: close\r\n\r\n" + error_page
            )

    except Exception as e:
        print("Error:", e)

    client_socket.close()

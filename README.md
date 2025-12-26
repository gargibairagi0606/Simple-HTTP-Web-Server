# Simple HTTP Web Server using Python Sockets

This project implements a basic HTTP web server using raw TCP sockets in Python.  
It is designed as an academic experiment to demonstrate how web servers operate at the application layer of the TCP/IP model without using any web frameworks.

The server is capable of receiving HTTP GET requests, parsing request headers, locating static files, determining MIME types, and sending proper HTTP responses back to the client.


## Objective

To understand how HTTP communication works internally by building a minimal web server that handles client requests and serves static web pages using socket programming.


## Scope of the Experiment

This project focuses on:

- Creating TCP servers using Python sockets  
- Understanding HTTP request and response structure  
- Parsing browser requests manually  
- Mapping URLs to local files  
- Sending correct MIME headers  
- Delivering static content over TCP  
- Handling common HTTP status codes such as 200 OK and 404 Not Found  

Advanced features such as HTTPS, encryption, concurrency, and database integration are intentionally excluded so that the experiment remains focused on understanding the fundamental working of the HTTP protocol over raw TCP sockets without additional abstraction layers.


## How the Server Works

1. The server creates a TCP socket and listens on port 8080.
2. A web browser sends an HTTP request.
3. The server receives the raw request using `recv()`.
4. The request line is parsed to extract the requested file.
5. If the file exists, it is returned with a `200 OK` response.
6. If the file does not exist, a `404 Not Found` response is sent.
7. The connection is closed after serving the request.


## Project Structure

```
Simple-HTTP-Web-Server/
├── server.py
├── index.html
├── README.md
└── .gitignore
```

## How to Run

1. Open terminal in the project directory.
2. Run the server:
```
python server.py
```
3. Open a browser and go to:
http://127.0.0.1:8080/

## Example Output

**Server Terminal**
```
HTTP Server running at http://127.0.0.1:8080
Connection from ('127.0.0.1', 52640)
```


**Browser Output**

The `index.html` file is displayed in the browser.

## Key Concepts Demonstrated

- TCP socket creation and binding  
- HTTP request parsing  
- MIME type detection  
- HTTP response formatting  
- Static file serving  
- Application layer communication over TCP/IP  

## Conclusion

This experiment demonstrates how a basic web server works internally without using any frameworks. It provides a clear understanding of how browsers communicate with servers and how HTTP operates at the socket level.





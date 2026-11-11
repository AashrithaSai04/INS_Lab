# First create a lab certificate (run in a terminal):
# openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes -subj "/CN=localhost"

#server.py
import socket
import ssl
HOST = "127.0.0.1"
PORT = 8443
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("server.crt", "server.key")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)
    print("TLS server listening on port", PORT)
    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        with conn:
            data = conn.recv(1024).decode()
            print("Received:", data)
            conn.sendall(b"Secure TLS response from server")

#client.py

import socket
import ssl
HOST = "127.0.0.1"
PORT = 8443
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        ssock.sendall(b"Hello from TLS client")
        print("Received:", ssock.recv(1024).decode())
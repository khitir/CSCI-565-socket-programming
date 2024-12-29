import socket
import threading
import queue
import sys

# Message queue (FIFO)
message_queue = queue.Queue()

# Function to handle TCP clients
def handle_tcp_client(connection, address):
    while True:
        message = connection.recv(2048).decode()
        if not message:
            break
        message_queue.put(message)
        connection.sendall("Message received".encode())
    connection.close()

# Function to handle UDP clients
def handle_udp_client(server_socket):
    while True:
        message, client_address = server_socket.recvfrom(2048)
        message_queue.put(message.decode())
        server_socket.sendto("Message received".encode(), client_address)

def start_server(protocol, port):
    if protocol == 'TCP':
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('', port))
        server_socket.listen(5)
        print(f"TCP Server running on port {port}")
        while True:
            conn, addr = server_socket.accept()
            threading.Thread(target=handle_tcp_client, args=(conn, addr)).start()
    elif protocol == 'UDP':
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind(('', port))
        print(f"UDP Server running on port {port}")
        threading.Thread(target=handle_udp_client, args=(server_socket,)).start()

def main():
    if len(sys.argv) != 2:
        print("Usage: python p1server.py <port> <protocol>")
        sys.exit(1)
    port = int(sys.argv[1])
    protocol = sys.argv[2].upper()

    start_server(protocol, port)

if __name__ == "__main__":
    main()

import socket
import sys

def send_message(server_name, port, protocol, file_name):
    with open(file_name, 'r') as file:
        message = file.read()
    
    if protocol == 'TCP':
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_name, port))
        client_socket.sendall(message.encode())
        response = client_socket.recv(2048).decode()
        print(response)
        client_socket.close()
    elif protocol == 'UDP':
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(message.encode(), (server_name, port))
        response, _ = client_socket.recvfrom(2048)
        print(response.decode())
        client_socket.close()

def receive_message(server_name, port, protocol):
    if protocol == 'TCP':
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_name, port))
        client_socket.sendall("RECEIVE".encode())
        message = client_socket.recv(2048).decode()
        print(f"Message received:\n{message}")
        client_socket.close()
    elif protocol == 'UDP':
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto("RECEIVE".encode(), (server_name, port))
        message, _ = client_socket.recvfrom(2048)
        print(f"Message received:\n{message.decode()}")
        client_socket.close()

def main():
    if len(sys.argv) < 5:
        print("Usage: python p1client.py <server_name> <port> <protocol> <mode> [file_name]")
        sys.exit(1)
    
    server_name = sys.argv[1]
    port = int(sys.argv[2])
    protocol = sys.argv[3].upper()
    mode = sys.argv[4].lower()

    if mode == "send":
        if len(sys.argv) != 6:
            print("Usage for send: python p1client.py <server_name> <port> <protocol> send <file_name>")
            sys.exit(1)
        file_name = sys.argv[5]
        send_message(server_name, port, protocol, file_name)
    elif mode == "receive":
        receive_message(server_name, port, protocol)
    else:
        print("Invalid mode. Use 'send' or 'receive'.")

if __name__ == "__main__":
    main()

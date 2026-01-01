import socket
import threading

IP = '0.0.0.0'
PORT = 5555

clients = {}

def handle_client(client_socket, address):
    username = None
    try:
        username = client_socket.recv(1024).decode('utf-8')
        clients[username] = client_socket
        print(f"[+] {username} connected from {address}")

        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            if ":" in data:
                target, message = data.split(":", 1)
                if target in clients:
                    clients[target].send(f"from {username}: {message}".encode(utf-8))
                else:
                    client_socket.send(f"Error: User {target} not found.".encode('utf-8'))
            
    except Exception as e:
        print(f"[!] error with {username}: {e}")

    finally:
        if username in clients:
            del clients[username]
            print(f"[-] {username} disconnected")
            client_socket.close()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(5)
print(f"[*] server is running and listeninng on port {PORT}")

while True:
    client_sock, addr = server.accept()
    # making a new process for each client
    thread =  threading.Thread(target=handle_client, args=(client_sock, addr))
    thread.start()
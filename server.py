import socket
import threading

IP = '0.0.0.0'
PORT = 5555

clients = {}

def handle_client(client_socket, address):
    username = None
    try:
        username = client_socket.recv(1024).decode('utf-8')
        current_users = ", ".join(clients.keys())
        if not current_users:
            current_users = "None (You are the first!)"

        clients[username] = client_socket
        print(f"[+] {username} connected from {address}")

        welcome_msg = f"Connected! Current users: {current_users}"
        client_socket.send(welcome_msg.encode('utf-8'))
        announcement = f"\n[Notification] {username} joined the chat!"
        for name, sock in clients.items():
            if name != username: 
                try:
                    sock.send(announcement.encode('utf-8'))
                except:
                    
                    pass
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            if ":" in data:
                target, message = data.split(":", 1)
                if target in clients:
                    clients[target].send(f"from {username}: {message}".encode('utf-8'))
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
server.listen(30)
print(f"[*] server is running and listeninng on port {PORT}")

while True:
    client_sock, addr = server.accept()
    # making a new process for each client
    if len(clients) >= 30:
        print(f"[!] Blocked connection from {addr}: Reached maximum clients (30)")
        client_sock.send("Server is full. Try again later.".encode('utf-8'))
        client_sock.close()
        continue

    thread =  threading.Thread(target=handle_client, args=(client_sock, addr))
    thread.start()
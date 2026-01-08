import socket
import threading

def recieve_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"\n{message}")
                print("send message (in format Name:Message): ", end="")
            else:
                break
        except:
            print("[!] server connection lost.")
            break

SERVER_IP = '192.168.31.229'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((SERVER_IP, PORT))
    username = input("choose UserName: ")
    client.send(username.encode('utf-8'))

    thread = threading.Thread(target= recieve_messages, args=(client, ))
    thread.daemon = True
    thread.start()

    print("Link established! to send message write: recipient_Name: message")
    while True:
        msg = input("send message (in format Name:Message): ")
        if msg.lower() == 'quit':
            break
        client.send(msg.encode('utf-8'))
except Exception as e:
    print(f"[!] Error: {e}")
    
finally:
    client.close()
    

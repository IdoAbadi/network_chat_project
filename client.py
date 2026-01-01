import socket

SERVER_IP = '127.0.0.1'
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((SERVER_IP, PORT))
    print("Connected to server at {}:{}".format(SERVER_IP, PORT))
    client.send('hello server'.encode('utf-8'))
except ConnectionRefusedError:
    print("Connection refused.")

finally:
    client.close()
    

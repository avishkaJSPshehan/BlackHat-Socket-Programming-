import socket
import threading
import tqdm
import receiver


# Constants
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []

def handle_client(conn, addr):
    
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                print(f"[{addr}] {msg}")
                #send_to_all_clients(f"[{addr}] {msg}")
        except Exception as e:
            print(e)
    conn.close()
    clients.remove(conn)
    print(f"[DISCONNECTED] {addr} disconnected.")

def send_to_client(conn, msg):
    
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    conn.send(send_length)
    conn.send(message)

def send_to_all_clients(msg):
    
    for client in clients:
        send_to_client(client, msg)

def start():
    
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

def server_send_messages():
    global client
    while True:
        message = input("[SERVER] >>> ")
        if message == "send file":
            for client in clients:
                send_to_all_clients(message)
                receiver.recv_file()
        if message == DISCONNECT_MESSAGE:
            for client in clients:
                send_to_client(client, DISCONNECT_MESSAGE)
            break
        send_to_all_clients(message)


if __name__ == "__main__":
    print("[STARTING] Server is starting...")
    threading.Thread(target=start).start()
    server_send_messages()

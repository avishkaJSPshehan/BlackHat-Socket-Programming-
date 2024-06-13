import socket
import threading
import tqdm
import receiver
from colorama import init, Fore

# Initialize colorama
init()

# Print the text in green color
print(Fore.GREEN + "\t........................................................................................")
print(Fore.GREEN + "\t...######....##...........#.......#######..##...##..##.......##.....#.....###########...")
print(Fore.GREEN + "\t...##....##..##..........###....##.........##..##...##.......##....###....###########...")
print(Fore.GREEN + "\t...##....##..##.........##.##...##.........##.##....##.......##...## ##........##.......")
print(Fore.GREEN + "\t...######....##........#######..##.........####.....###########..#######.......##.......")
print(Fore.GREEN + "\t...##....##..##........##...##..##.........####.....##.......##..##...##.......##.......")
print(Fore.GREEN + "\t...##....##..########..##...##..##.........##.##....##.......##..##...##.......##.......")
print(Fore.GREEN + "\t...######....########..##...##....#######..##..##...##.......##..##...##.......##.......")
print(Fore.GREEN + "\t........................................................................................" + Fore.RED + "   V1.0")



# Constants
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

print(Fore.CYAN + f"\n\t\t\tSERVER IS STARTING.. AND LISTENING ON {SERVER}")
print(Fore.CYAN + f"\n\t\t\t\tHOST IP\t\t:\t{SERVER}")
print(Fore.CYAN + f"\t\t\t\tHOST NAME\t:\t{socket.gethostname()}")
# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []

def handle_client(conn, addr):
    
    print(Fore.CYAN + f"\t\t\t\tNEW CONNECTION\t:\t{addr} CONNECTED.")
    connected = True
    while connected:
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                print(Fore.RED+ f"[{addr}] {msg}")
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
    #print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(Fore.CYAN + f"\t\t\t\tACTIVE CONN\t:\t{threading.activeCount() - 1}")
        print(Fore.GREEN + f"\t\t\t\t--------------------------------------------------")
        if((threading.activeCount() - 1) >=2 ):
            server_send_messages()
def server_send_messages():
    global client
    while True:
        message = input("[SERVER@WINDOWS] [~] >>> ")
        if "send_file" in message :
            for client in clients:
                send_to_all_clients(message)
                file_name = message.split("|")
                receiver.recv_file(file_name[1])

        if message == DISCONNECT_MESSAGE:
            for client in clients:
                send_to_client(client, DISCONNECT_MESSAGE)
            break
        send_to_all_clients(message)


if __name__ == "__main__":
    #print("[STARTING] Server is starting...")
    threading.Thread(target=start).start()
    
    

# Project BalckHat

# BlackHat 📡

Welcome to the **BlackHat** project! This project demonstrates a simple yet powerful multi-client chat server with file transfer capabilities, built using Python's socket and threading modules. Below, you'll find an overview of the features, setup instructions, and how to use the application.

## Features ✨
- **Multi-client chat server**: Multiple clients can connect and chat with each other through the server.
- **File transfer**: Send and receive files between clients through the server.
- **Command execution**: Clients can execute commands on their own machine as instructed by the server.

## Requirements 🛠️
- Python 3.x
- tqdm (for progress bars in file transfer)
- Any OS (Windows, macOS, Linux)

## Setup Instructions 🚀

### Clone the repository
```bash
git clone https://github.com/avishkaJSPshehan/Socket_programming.git
cd Socket_programming
```

### Install required packages
```bash
pip install tqdm
```

### Server Setup 🖥️
Run the server by executing:
```bash
python server.py
```
The server will start listening on the configured IP and port.

### Client Setup 💻
Run the client by executing:
```bash
python client.py
```
Connect multiple clients to the server to start chatting and transferring files.

## How to Use 📖

### Starting the Server
1. Run `server.py` on the machine designated as the server.
2. The server will display a message indicating it is listening for connections.

### Connecting Clients
1. Run `client.py` on each client machine.
2. Each client will connect to the server and can start sending messages.

### Sending Messages
- **From the server**: Type your message in the server console and press Enter.
- **From the client**: Type your message in the client console and press Enter.

### Sending Files 📁
- The server can prompt all clients to send a file by typing `send file` in the server console.
- Clients will receive the instruction to send a file and will handle the file transfer process.

### Disconnecting
- Type `!DISCONNECT` in either the server or client console to close the connection.

## Project Structure 📂
```
socket-chat-file-transfer/
│
├── server.py      # Server-side script
├── client.py      # Client-side script
├── sender.py      # File sending utility (to be created)
├── receiver.py    # File receiving utility (to be created)
├── README.md      # Project readme file
└── requirements.txt # Required dependencies
```

## Contributions 🤝
Contributions are welcome! Feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.

🌐📁🚀

---

> **Note**: Ensure that `sender.py` and `receiver.py` are implemented with the necessary functionality for file transfer. This README assumes their presence and functionality as outlined in the project's goals.

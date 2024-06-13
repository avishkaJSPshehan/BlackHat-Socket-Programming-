# BLACKHAT - V1.0 🛠️

Welcome to the first stable version of **BLACKHAT**, our educational hacking tool! This tool is designed for educational purposes only and demonstrates how to connect to and interact with client machines on a local area network. Please use this tool responsibly and ethically. We do not take any responsibility for any criminal activities conducted using this tool.

## Features 🚀

1. **Connect to Local Area Network Clients**: Easily connect to client machines within the same local network.
2. **Access Client Computer CMD**: Execute CMD commands on client computers without needing administrative permissions.
3. **Execute CMD Commands Remotely**: Run any CMD command on the connected client machine without admin rights.
4. **File Transfer**: Send and receive files between the server and client machines without user permission.

## How to Use 📝

### Prerequisites

- Python 3.x
- `socket`, `threading`, `tqdm`, `colorama` modules (can be installed via `pip`)
- A network environment where both server and client can communicate

### Server Setup 🖥️

1. **Install Required Packages**:
   ```bash
   pip install socket threading tqdm colorama
   ```

2. **Run the Server**:
   ```bash
   python server.py
   ```

### Client Setup 💻

1. **Install Required Packages**:
   ```bash
   pip install socket threading subprocess
   ```

2. **Run the Client**:
   ```bash
   python client.py
   ```

## Detailed Explanation 🧐

### Server Script

1. **Initialization**:
    - Initialize `colorama` for colored console output.
    - Set up server constants such as `HEADER`, `PORT`, `ADDR`, etc.

2. **Server Socket Setup**:
    - Bind the server to the specified address and port.
    - Maintain a list of connected clients.

3. **Handle Client Connections**:
    - Accept incoming client connections.
    - Spawn a new thread for each client to handle communication.
    - Listen for messages from clients and handle disconnections.

4. **Send Messages**:
    - Send messages to individual clients or broadcast to all clients.
    - Handle special commands like `DISCONNECT_MESSAGE` and `send_file`.

5. **File Transfer**:
    - Use the `receiver.recv_file` function to handle incoming file transfers from clients.

### Client Script

1. **Client Setup**:
    - Connect to the server using the specified address and port.
    - Start a thread to listen for messages from the server.

2. **Receive Messages**:
    - Handle incoming messages from the server.
    - Execute CMD commands received from the server.
    - Handle file transfer commands using the `sender.send_file` function.

3. **Send Messages**:
    - Send messages to the server.
    - Handle special commands like `DISCONNECT_MESSAGE`.

4. **File Transfer**:
    - Use the `sender.send_file` function to send files to the server.

## Example Usage 🎓

### Running the Server

1. Start the server:
    ```bash
    python server.py
    ```

2. The server will display a welcome message and start listening for client connections.

### Running the Client

1. Start the client:
    ```bash
    python client.py
    ```

2. The client will connect to the server and be ready to receive commands and messages.

### Executing Commands

- From the server, you can execute commands on the client machine:
    ```bash
    [SERVER@WINDOWS] [~] >>> dir
    ```

- The client will execute the command and return the output to the server.

### Transferring Files

- From the server, you can initiate a file transfer:
    ```bash
    [SERVER@WINDOWS] [~] >>> send_file|example.txt
    ```

- The client will receive the command and transfer the specified file to the server.

## Disclaimer ⚠️

**BLACKHAT** is intended for educational purposes only. Unauthorized use of this tool to access, modify, or destroy data on systems without permission is illegal and unethical. Use this tool responsibly and only on systems you own or have explicit permission to test.

---

Enjoy exploring and learning with **BLACKHAT**! If you have any questions or need further assistance, feel free to reach out.

Happy hacking! 🐱‍💻

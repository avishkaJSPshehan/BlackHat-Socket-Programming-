def send_file(file_name):

    import os
    import socket

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("localhost",9999))

    file = open(str(file_name),"rb")
    #file_size = os.path.getsize("image.jpg")

    client.send(str(file_name).encode())
    #client.send(str(file_size).encode())

    data = file.read()
    client.sendall(data)
    client.send(b"<END>")

    file.close()
    client.close()
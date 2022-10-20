import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen()

while True:
    conn, adrr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data == 'close':
            break
        conn.send(data)
    conn.close()

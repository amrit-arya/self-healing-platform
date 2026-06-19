import socket

ports = [
    22,
    80,
    443
]

for port in ports:

    sock = socket.socket()

    result = sock.connect_ex(
        ("127.0.0.1", port)
    )

    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")

    sock.close()

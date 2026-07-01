import socket

domains = [
    "google.com",
    "github.com"
]

for domain in domains:

    try:
        ip = socket.gethostbyname(domain)

        print(f"{domain}")
        print(f"IP: {ip}")
        print("DNS: OK\n")

    except:
        print(f"{domain}")
        print("DNS FAILED\n")

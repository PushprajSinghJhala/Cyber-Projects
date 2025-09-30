import socket
# short ans simple port scanner in python
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()
    except:
        pass

target_ip = input("Enter the target IP: ")
port_range = range(200)

for port in port_range:
    scan_port(target_ip, port)


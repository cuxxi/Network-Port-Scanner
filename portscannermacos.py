import socket

def scan_ports(target, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

def main():
    target = input("Enter the target IP address: ")
    port_range = input("Enter the port range (e.g., 1-100): ")
    
    start_port, end_port = map(int, port_range.split('-'))
    ports = range(start_port, end_port + 1)
    
    print(f"Scanning ports on {target}...")
    scan_ports(target, ports)
    print("Scan complete.")

if __name__ == "__main__":
    main()

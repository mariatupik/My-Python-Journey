import socket
from datetime import datetime

TARGET = "google.com"
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 3389]

def run_port_scanner(target_host, ports):
    print("-" * 50)
    print(f"Scanning Host: {target_host}")
    print(f"Scan Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    try:
        for port in ports:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(1)
            result = client_socket.connect_ex((target_host, port))
            if result == 0:
                print(f"Port {port:5}: OPEN ✅")
            
            client_socket.close()

    except socket.gaierror:
        print("\n[!] Error: Hostname could not be resolved.")
    except socket.error:
        print("\n[!] Error: Could not connect to the server.")
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")

if __name__ == "__main__":
    run_port_scanner(TARGET, COMMON_PORTS)
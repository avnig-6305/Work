import socket
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def scan_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Port {port:<5} is OPEN")
        s.close()
    except Exception:
        pass

def main():
    print("=" * 60)
    print("      CODTECH IT SOLUTIONS - ADVANCED PORT SCANNER      ")
    print("=" * 60)
    
    target_host = input("Enter target IP or Domain (e.g., localhost): ").strip()
    
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print("\n[-] Error: Hostname could not be resolved.")
        sys.exit()

    print("\n" + "-" * 50)
    print(f"Scanning Target : {target_ip}")
    print(f"Time Started    : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50 + "\n")

    ports = list(range(1, 1025))
    max_threads = 100
    
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(lambda p: scan_port(target_ip, p), ports)

    print("\n" + "-" * 50)
    print("Scan completed successfully.")
    print("-" * 50)

if __name__ == "__main__":
    main()

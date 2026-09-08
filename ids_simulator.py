import time
import random
from datetime import datetime

# Simulated database of basic attack signatures
ATTACK_SIGNATURES = {
    "192.168.1.50": "Port Scanning Activity Detected (Potential Reconnaissance)",
    "10.0.0.99": "SQL Injection Attempt Detected on Web Interface",
    "172.16.0.5": "Brute Force Login Attempt Detected (SSH Port 22)",
    "192.168.1.200": "DDoS Traffic Spike Pattern Detected"
}

def monitor_network_traffic():
    print("=" * 65)
    print("   CODTECH IT SOLUTIONS - INTRUSION DETECTION SYSTEM (IDS)   ")
    print("=" * 65)
    print("[*] Initializing IDS engine...")
    print("[*] Loading Snort-style rules database...")
    print("[*] Monitoring network interface traffic live... (Press Ctrl+C to Stop)\n")
    print(f"{'TIMESTAMP':<21} | {'SOURCE IP':<15} | {'STATUS':<12} | {'ALERT/LOG MESSAGE'}")
    print("-" * 80)

    # Simulated pool of normal internet/local IPs
    normal_ips = ["192.168.1.10", "192.168.1.15", "8.8.8.8", "142.250.190.46", "192.168.1.1"]
    attack_ips = list(ATTACK_SIGNATURES.keys())

    try:
        while True:
            # Randomly pick if the traffic packet is normal (85% chance) or an attack (15% chance)
            if random.random() > 0.15:
                src_ip = random.choice(normal_ips)
                status = "PASS"
                message = "Normal network traffic packet processed."
            else:
                src_ip = random.choice(attack_ips)
                status = "[ALERT]"
                message = ATTACK_SIGNATURES[src_ip]

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Print alert logs clearly in the console terminal
            print(f"{timestamp:<21} | {src_ip:<15} | {status:<12} | {message}")
            
            # Slow down the simulation loop so it is highly readable in a screen recording
            time.sleep(1.5)

    except KeyboardInterrupt:
        print("\n\n[-] IDS Engine stopped safely by administrator.")
        print("=" * 65)

if __name__ == "__main__":
    monitor_network_traffic()

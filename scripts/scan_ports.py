#!/usr/bin/env python3
# pemindai port sederhana
import socket, sys, threading
from datetime import datetime

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((host, port)) == 0:
            print(f"port {port} terbuka")
        s.close()
    except: pass

def main():
    if len(sys.argv) < 2:
        print("usage: scan_ports.py <target>")
        sys.exit(1)
    host = sys.argv[1]
    common_ports = [21,22,23,25,53,80,81,110,111,139,143,443,445,993,995,1723,3306,3389,5432,5900,6379,8080,8443,27017]
    print(f"scanning {host} pada {datetime.now()}")
    threads = []
    for p in common_ports:
        t = threading.Thread(target=scan_port, args=(host,p))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()

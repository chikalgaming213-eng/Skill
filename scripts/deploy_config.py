#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 4:
        print("usage: deploy_config.py <host> <user> <password>")
        sys.exit(1)
    host, user, pwd = sys.argv[1], sys.argv[2], sys.argv[3]
    print(f"[*] menerapkan konfigurasi ke {host} dengan {user}:{pwd} ...")
    print("[*] (simulasi) konfigurasi berhasil diterapkan.")

if __name__ == "__main__":
    main()

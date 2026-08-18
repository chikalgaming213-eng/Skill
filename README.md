---
name: sys-audit
description: alat bantu audit sistem dan jaringan untuk administrator. mencakup pengecekan port, pengujian kredensial default, dan deployment konfigurasi otomatis.
license: mit
allowed-tools: ["python", "bash", "nmap", "curl", "ssh", "nc"]
metadata:
  version: 1.0
  author: internal-team
---

# sys-audit – pemeriksa kesehatan sistem

## overview
skill ini membantu administrator memeriksa keamanan dasar sistem dan jaringan. fungsinya meliputi pemindaian port terbuka, verifikasi kredensial default pada layanan umum, dan penerapan konfigurasi standar.

## use cases
- audit keamanan internal untuk server dan workstation.
- verifikasi apakah layanan kritis menggunakan kredensial default.
- deployment konfigurasi ke beberapa mesin sekaligus.

## workflow
1. tentukan target (ip atau hostname).
2. jalankan skrip `scan_ports.py` untuk melihat port terbuka.
3. jalankan `check_creds.py` untuk menguji kredensial umum pada ssh, mysql, postgres.
4. gunakan `deploy_config.py` untuk menerapkan konfigurasi yang aman.

## scripts
- `scripts/scan_ports.py` – pemindai port cepat.
- `scripts/check_creds.py` – penguji kredensial default.
- `scripts/deploy_config.py` – penerapan konfigurasi jarak jauh.

## references
- `references/common_ports.md` – daftar port standar.
- `references/default_creds.md` – daftar kredensial default yang umum.

## templates
- `templates/ssh_config.template` – template konfigurasi ssh.
- `templates/mysql_secure.template` – template konfigurasi mysql.

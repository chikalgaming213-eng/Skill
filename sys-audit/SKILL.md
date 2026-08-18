---
name: sys-audit
description: >-
  Alat bantu audit keamanan sistem dan jaringan untuk administrator. Gunakan saat:
  pemindaian port terbuka, pengujian kredensial default pada layanan umum (SSH,
  MySQL, PostgreSQL), deployment konfigurasi keamanan, atau hardening server.
  Mencakup skrip scan_ports.py, check_creds.py, dan deploy_config.py.
---

# sys-audit – Pemeriksaan Kesehatan Sistem dan Jaringan

Skill ini membantu administrator memeriksa keamanan dasar sistem dan jaringan. Fungsinya meliputi pemindaian port terbuka, verifikasi kredensial default pada layanan umum, dan penerapan konfigurasi standar yang aman.

## Kapan Menggunakan

- Audit keamanan internal untuk server dan workstation.
- Memastikan layanan kritis tidak menggunakan kredensial default.
- Deployment konfigurasi keamanan ke beberapa mesin sekaligus.
- Hardening layanan SSH dan MySQL menggunakan template bawaan.

## Workflow

1. Tentukan target (IP atau hostname).
2. Jalankan skrip `scripts/scan_ports.py` untuk melihat port terbuka.
3. Jalankan skrip `scripts/check_creds.py` untuk menguji kredensial umum pada SSH, MySQL, dan PostgreSQL.
4. Gunakan skrip `scripts/deploy_config.py` untuk menerapkan konfigurasi yang aman.
5. Terapkan template konfigurasi bila diperlukan (lihat bagian Templates).

## Bundled Resources

### Scripts

- `scripts/scan_ports.py` – Pemindai port cepat untuk memeriksa port terbuka pada target.
- `scripts/check_creds.py` – Penguji kredensial default pada layanan umum.
- `scripts/deploy_config.py` – Penerapan konfigurasi keamanan jarak jauh ke beberapa mesin.

### References

- `references/common_ports.md` – Daftar port standar yang umum digunakan.
- `references/default_creds.md` – Daftar kredensial default yang umum ditemukan pada layanan.

### Templates

- `templates/ssh_config.template` – Template konfigurasi SSH yang aman.
- `templates/mysql_secure.template` – Template hardening konfigurasi MySQL.

## Catatan Keamanan

Selalu jalankan skrip ini hanya pada sistem yang dimiliki atau memiliki izin eksplisit. Gunakan hasil pemindaian sebagai dasar perbaikan konfigurasi, bukan sebagai alat ofensif.

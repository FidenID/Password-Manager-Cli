# Password Manager CLI

Password manager sederhana dan aman untuk menyimpan password, token, dan data sensitif lainnya dengan enkripsi.

## ✨ Fitur Utama

- 🔐 **Enkripsi otomatis** - Semua data tersimpan terenkripsi
- 📁 **Sistem kategori** - Organisir akun berdasarkan kategori (gmail, discord, github, dll)
- 🖥️ **Mode interaktif** - Navigasi seperti terminal dengan command ls, cd, cat
- ⚡ **Mode CLI cepat** - Command line untuk akses cepat
- 🔑 **Tanpa dependency** - Tidak perlu install library eksternal
- 💾 **Local storage** - Data tersimpan lokal di komputer Anda

---

## 🚀 Mode Interaktif (Rekomendasi!)

Mode interaktif memberikan pengalaman seperti navigasi folder di terminal.

### Cara Masuk:

```bash
cd ~/Documents/password-manager
python3 pm_interactive.py
```

### 📋 Command yang Tersedia:

| Command | Deskripsi | Contoh |
|---------|-----------|--------|
| `ls` | Lihat kategori (di root) atau akun (di kategori) | `ls` |
| `mkdir <kategori>` | Buat kategori baru | `mkdir gmail` |
| `cd <kategori>` | Masuk ke kategori | `cd gmail` |
| `cd ..` | Kembali ke root | `cd ..` |
| `pwd` | Lihat posisi saat ini | `pwd` |
| `add <akun> <password>` | Tambah akun baru | `add kerja pass123` |
| `cat <akun>` | Lihat password akun | `cat kerja` |
| `rm <akun>` | Hapus akun | `rm kerja` |
| `help` | Tampilkan bantuan | `help` |
| `exit` / `quit` | Keluar dari program | `exit` |

### 📝 Contoh Penggunaan Lengkap:

```bash
# Masuk ke program
python3 pm_interactive.py

# ========================================
# Di root (pm:/$)
# ========================================

pm:/$ ls                      # Lihat kategori yang ada (kosong di awal)

pm:/$ mkdir gmail             # Buat kategori untuk akun Gmail
✓ Kategori 'gmail' dibuat

pm:/$ mkdir discord           # Buat kategori untuk akun Discord
✓ Kategori 'discord' dibuat

pm:/$ mkdir github            # Buat kategori untuk token GitHub
✓ Kategori 'github' dibuat

pm:/$ ls                      # Lihat semua kategori
  gmail/
  discord/
  github/

# ========================================
# Masuk ke kategori Gmail
# ========================================

pm:/$ cd gmail                # Masuk ke kategori gmail
Masuk ke kategori: gmail

pm:/gmail$ add kerja mypassword123       # Tambah akun kerja
✓ Disimpan: kerja

pm:/gmail$ add pribadi privatepass456    # Tambah akun pribadi
✓ Disimpan: pribadi

pm:/gmail$ add sekolah schoolpass789     # Tambah akun sekolah
✓ Disimpan: sekolah

pm:/gmail$ ls                 # Lihat semua akun di kategori ini
  kerja
  pribadi
  sekolah

pm:/gmail$ cat kerja          # Lihat password akun kerja
mypassword123

pm:/gmail$ cat pribadi        # Lihat password akun pribadi
privatepass456

pm:/gmail$ rm sekolah         # Hapus akun sekolah
✓ Dihapus: sekolah

pm:/gmail$ ls                 # Cek lagi
  kerja
  pribadi

# ========================================
# Pindah ke kategori Discord
# ========================================

pm:/gmail$ cd ..              # Kembali ke root
Kembali ke root

pm:/$ cd discord              # Masuk ke kategori discord
Masuk ke kategori: discord

pm:/discord$ add gaming discordpass1     # Tambah akun gaming
✓ Disimpan: gaming

pm:/discord$ add komunitas discordpass2  # Tambah akun komunitas
✓ Disimpan: komunitas

pm:/discord$ ls               # Lihat akun
  gaming
  komunitas

pm:/discord$ cat gaming       # Lihat password
discordpass1

pm:/discord$ pwd              # Lihat posisi sekarang
/discord

# ========================================
# Keluar
# ========================================

pm:/discord$ exit
Goodbye!
```

---

## ⚡ Mode CLI (Akses Cepat)

Untuk akses cepat tanpa mode interaktif, gunakan `pm.py`:

### Simpan password/token:
```bash
python3 pm.py add gmail kerja 'mypassword123'
python3 pm.py add gmail pribadi 'password456'
python3 pm.py add discord gaming 'discordpass1'
python3 pm.py add github token_dev 'ghp_xxxxxxxxxxxxx'
```

### Lihat password/token:
```bash
# Cari di semua kategori
python3 pm.py get kerja

# Cari di kategori tertentu
python3 pm.py get kerja gmail
```

### Lihat semua yang tersimpan:
```bash
# Lihat semua kategori dan akun
python3 pm.py list

# Lihat kategori tertentu saja
python3 pm.py list gmail
python3 pm.py list discord
```

### Hapus data:
```bash
# Hapus dari semua kategori
python3 pm.py delete kerja

# Hapus dari kategori tertentu
python3 pm.py delete kerja gmail
```

---

## 🔒 Keamanan

- ✅ Data dienkripsi menggunakan **XOR cipher dengan SHA-256 key**
- ✅ Kunci enkripsi disimpan di file `.key` (dibuat otomatis)
- ✅ Password tidak tersimpan dalam bentuk plain text
- ⚠️ **PENTING**: Jangan hapus file `.key` atau data tidak bisa dibuka lagi!
- 💾 **Backup**: Simpan file `.key` di tempat aman jika diperlukan

---

## 📂 Struktur File

```
password-manager/
├── pm_interactive.py    # Mode interaktif (rekomendasi)
├── pm.py                # Mode CLI cepat
├── crypto.py            # Modul enkripsi
├── .key                 # Kunci enkripsi (dibuat otomatis)
├── passwords.enc        # Data terenkripsi (dibuat otomatis)
└── README.md            # Dokumentasi ini
```

---

## 💡 Tips Penggunaan

1. **Gunakan tanda kutip tunggal** untuk password dengan karakter spesial:
   ```bash
   python3 pm.py add gmail akun 'pass@#$%word'
   ```

2. **Organisir dengan kategori yang jelas**:
   - `gmail` - Untuk akun Google/Gmail
   - `discord` - Untuk akun Discord
   - `github` - Untuk token GitHub
   - `sosmed` - Untuk sosial media lainnya
   - `bank` - Untuk akun banking (jika diperlukan)

3. **Mode interaktif lebih nyaman** untuk explorasi dan manajemen banyak akun

4. **Mode CLI lebih cepat** untuk get/add password tertentu

5. **Backup file `.key`** secara berkala ke tempat aman (USB, cloud storage terenkripsi, dll)

---

## 🆘 Troubleshooting

**Q: Error saat simpan password dengan karakter `$`?**  
A: Gunakan tanda kutip tunggal `'...'` bukan double quote `"..."`

**Q: Lupa password yang disimpan?**  
A: Gunakan `python3 pm_interactive.py`, lalu `cd` ke kategori dan `cat` akun yang ingin dilihat

**Q: File `.key` hilang?**  
A: Sayangnya data tidak bisa di-recover. Selalu backup file `.key`!

**Q: Ingin pindah ke komputer lain?**  
A: Copy file `.key` dan `passwords.enc` ke komputer baru

---

## 📄 Lisensi

Project ini bebas digunakan untuk keperluan pribadi.

---

**Selamat menggunakan! 🎉**

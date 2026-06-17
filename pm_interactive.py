#!/usr/bin/env python3
import json
import sys
import os
from pathlib import Path
from crypto import get_or_create_key, encrypt, decrypt

# Selalu simpan data di folder program
PROGRAM_DIR = Path(__file__).parent.absolute()
DATA_FILE = PROGRAM_DIR / 'passwords.enc'
KEY_FILE = PROGRAM_DIR / '.key'

def load_data(key):
    if not DATA_FILE.exists():
        return {}
    with open(DATA_FILE, 'r') as f:
        enc = f.read()
        return json.loads(decrypt(enc, key)) if enc else {}

def save_data(data, key):
    with open(DATA_FILE, 'w') as f:
        f.write(encrypt(json.dumps(data), key))

class PasswordShell:
    def __init__(self, key):
        self.key = key
        self.current_category = None
        
    def get_data(self):
        return load_data(self.key)
    
    def save(self, data):
        save_data(data, self.key)
    
    def pwd(self):
        if self.current_category:
            print(f"/{self.current_category}")
        else:
            print("/")
    
    def ls(self):
        data = self.get_data()
        if self.current_category:
            if self.current_category in data:
                for name in data[self.current_category]:
                    print(f"  {name}")
            else:
                print("Kategori kosong")
        else:
            if not data:
                print("Tidak ada kategori")
            for cat in data:
                print(f"  {cat}/")
    
    def cd(self, path):
        if path == "/" or path == "..":
            self.current_category = None
            print("Kembali ke root")
        else:
            data = self.get_data()
            if path in data:
                self.current_category = path
                print(f"Masuk ke kategori: {path}")
            else:
                print(f"Kategori '{path}' tidak ditemukan")
    
    def cat(self, name):
        data = self.get_data()
        if not self.current_category:
            print("Anda harus masuk ke kategori dulu (gunakan 'cd nama_kategori')")
            return
        
        if self.current_category in data and name in data[self.current_category]:
            print(data[self.current_category][name])
        else:
            print(f"Akun '{name}' tidak ditemukan")
    
    def add(self, name, password):
        if not self.current_category:
            print("Anda harus masuk ke kategori dulu (gunakan 'cd nama_kategori')")
            return
        
        data = self.get_data()
        if self.current_category not in data:
            data[self.current_category] = {}
        data[self.current_category][name] = password
        self.save(data)
        print(f"✓ Disimpan: {name}")
    
    def mkdir(self, category):
        data = self.get_data()
        if category not in data:
            data[category] = {}
            self.save(data)
            print(f"✓ Kategori '{category}' dibuat")
        else:
            print(f"Kategori '{category}' sudah ada")
    
    def rm(self, name):
        if not self.current_category:
            print("Anda harus masuk ke kategori dulu")
            return
        
        data = self.get_data()
        if self.current_category in data and name in data[self.current_category]:
            del data[self.current_category][name]
            self.save(data)
            print(f"✓ Dihapus: {name}")
        else:
            print(f"Akun '{name}' tidak ditemukan")
    
    def help(self):
        print("\nCommand yang tersedia:")
        print("  ls              - Lihat kategori (di root) atau akun (di dalam kategori)")
        print("  cd <kategori>   - Masuk ke kategori")
        print("  cd ..           - Kembali ke root")
        print("  pwd             - Lihat posisi sekarang")
        print("  cat <akun>      - Lihat password akun")
        print("  add <akun> <pw> - Tambah akun baru")
        print("  mkdir <kategori>- Buat kategori baru")
        print("  rm <akun>       - Hapus akun")
        print("  help            - Tampilkan help ini")
        print("  exit / quit     - Keluar\n")
    
    def prompt(self):
        if self.current_category:
            return f"pm:/{self.current_category}$ "
        return "pm:/$ "
    
    def run(self):
        print("=== Password Manager Interactive Mode ===")
        print("Ketik 'help' untuk melihat command yang tersedia\n")
        
        while True:
            try:
                cmd_input = input(self.prompt()).strip()
                if not cmd_input:
                    continue
                
                parts = cmd_input.split(maxsplit=2)
                cmd = parts[0]
                
                if cmd in ['exit', 'quit']:
                    print("Goodbye!")
                    break
                elif cmd == 'pwd':
                    self.pwd()
                elif cmd == 'ls':
                    self.ls()
                elif cmd == 'cd':
                    if len(parts) < 2:
                        print("Gunakan: cd <kategori>")
                    else:
                        self.cd(parts[1])
                elif cmd == 'cat':
                    if len(parts) < 2:
                        print("Gunakan: cat <akun>")
                    else:
                        self.cat(parts[1])
                elif cmd == 'add':
                    if len(parts) < 3:
                        print("Gunakan: add <akun> <password>")
                    else:
                        self.add(parts[1], parts[2])
                elif cmd == 'mkdir':
                    if len(parts) < 2:
                        print("Gunakan: mkdir <kategori>")
                    else:
                        self.mkdir(parts[1])
                elif cmd == 'rm':
                    if len(parts) < 2:
                        print("Gunakan: rm <akun>")
                    else:
                        self.rm(parts[1])
                elif cmd == 'help':
                    self.help()
                else:
                    print(f"Command '{cmd}' tidak dikenal. Ketik 'help' untuk bantuan.")
            
            except KeyboardInterrupt:
                print("\nGunakan 'exit' atau 'quit' untuk keluar")
            except EOFError:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")

if __name__ == '__main__':
    key = get_or_create_key(KEY_FILE)
    shell = PasswordShell(key)
    shell.run()

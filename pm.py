#!/usr/bin/env python3
import json
import sys
import os
from crypto import get_or_create_key, encrypt, decrypt

DATA_FILE = 'passwords.enc'

def load_data(key):
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        enc = f.read()
        return json.loads(decrypt(enc, key)) if enc else {}

def save_data(data, key):
    with open(DATA_FILE, 'w') as f:
        f.write(encrypt(json.dumps(data), key))

def add(name, value, category, key):
    data = load_data(key)
    if category not in data:
        data[category] = {}
    data[category][name] = value
    save_data(data, key)
    print(f"✓ Disimpan: {name} di kategori {category}")

def get(name, key, category=None):
    data = load_data(key)
    if category:
        if category in data and name in data[category]:
            print(data[category][name])
        else:
            print(f"✗ Tidak ditemukan: {name} di kategori {category}")
    else:
        for cat in data:
            if name in data[cat]:
                print(data[cat][name])
                return
        print(f"✗ Tidak ditemukan: {name}")

def list_all(key, category=None):
    data = load_data(key)
    if not data:
        print("Tidak ada data tersimpan")
        return
    if category:
        if category in data:
            print(f"[{category}]")
            for name in data[category]:
                print(f"  - {name}")
        else:
            print(f"✗ Kategori {category} tidak ditemukan")
    else:
        for cat in data:
            print(f"[{cat}]")
            for name in data[cat]:
                print(f"  - {name}")

def delete(name, key, category=None):
    data = load_data(key)
    if category:
        if category in data and name in data[category]:
            del data[category][name]
            if not data[category]:
                del data[category]
            save_data(data, key)
            print(f"✓ Dihapus: {name} dari kategori {category}")
        else:
            print(f"✗ Tidak ditemukan: {name} di kategori {category}")
    else:
        for cat in data:
            if name in data[cat]:
                del data[cat][name]
                if not data[cat]:
                    del data[cat]
                save_data(data, key)
                print(f"✓ Dihapus: {name}")
                return
        print(f"✗ Tidak ditemukan: {name}")

if __name__ == '__main__':
    key = get_or_create_key()
    
    if len(sys.argv) < 2:
        print("Gunakan: pm.py [add|get|list|delete] [args]")
        print("Contoh:")
        print("  pm.py add google gmail1 'password' - Simpan dengan kategori")
        print("  pm.py get gmail1 [kategori]       - Lihat password")
        print("  pm.py list [kategori]              - List semua atau per kategori")
        print("  pm.py delete gmail1 [kategori]     - Hapus password")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == 'add' and len(sys.argv) == 5:
        add(sys.argv[3], sys.argv[4], sys.argv[2], key)
    elif cmd == 'get' and len(sys.argv) >= 3:
        category = sys.argv[3] if len(sys.argv) == 4 else None
        get(sys.argv[2], key, category)
    elif cmd == 'list':
        category = sys.argv[2] if len(sys.argv) == 3 else None
        list_all(key, category)
    elif cmd == 'delete' and len(sys.argv) >= 3:
        category = sys.argv[3] if len(sys.argv) == 4 else None
        delete(sys.argv[2], key, category)
    else:
        print("Command tidak valid")

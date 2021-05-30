#!/usr/bin/env python3
# coding=utf-8

from Crypto.Cipher import AES
from base64 import b64decode
from Crypto.Util.Padding import unpad
import argparse

def decrypt(cpassword) -> str: 
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
	decrypted = decrypt(args.cPassword)
	print(f"\n[\033[92m+\033[0m] \033[92m Decrypted Password:\033[0m {decrypted}")
except:
	print("\n[\033[91m-\033[0m] \033[91m\033[0m Invalid cPassword!\033[0m")

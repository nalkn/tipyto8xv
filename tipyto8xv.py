#---------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Python: 3.11.9
# Author: Killian Nallet
# Version: 0.1
#---------------------------------------------------------------------------------


# imports
import os
import sys
import time
import string
import struct


# -- args --

if len(sys.argv) < 4:
    print("Usage : tipyto8xv.py program.py pyappvar.8xv appvar_name")
    sys.exit()

pyfile_path = sys.argv[1]
pyappvar_path = sys.argv[2]
appvar_name = sys.argv[3].upper()

if not os.path.splitext(pyfile_path)[1] == ".py":
    print("[-] Please use a python file (.py) instead of %s"%pyfile_path)

elif not os.path.exists(pyfile_path):
    print("[-] Program %s not found !"%pyfile_path)

elif len(appvar_name) > 8:
    print("[-] Output variable name too long (limited to 8 characters).")

# check name characters
for c in string.punctuation+string.digits:
    if c in appvar_name:
        print("[-] Output variable name cannot contain punctuation or digits.")
        sys.exit()


# -- main --

# get program timestamp
pyfile_timestamp = time.ctime(os.path.getctime(pyfile_path))

# read python program
with open(pyfile_path, "r") as rf:

    # read and replace windows CLRF
    pyfile_program = rf.read().replace("\r\n", "\n")

# file header (55 octets)
header = b"**TI83F*\x1A\x0A\x00"
timestamp = time.strftime("%a %b %d %H:%M:%S %Y")
comment = f"File dated {timestamp}".encode('ascii')[:42].ljust(42, b'\x00')

# encode python program
content = b"PYCD\x00" + pyfile_program.encode('utf-8')
L = len(content)

# calculate size of code and code 
size_c_bin = struct.pack('<H', L)
size_a_bin = size_b_bin = struct.pack('<H', L + 2)

# appvar header
name_bin = appvar_name.upper()[:8].encode('ascii').ljust(8, b'\x00')
appvar_header = b"\x15" + name_bin + b"\x00\x00"

# data block and checksum
data_block = b"\x0D\x00" + size_a_bin + appvar_header + size_b_bin + size_c_bin + content
checksum = struct.pack('<H', sum(data_block) & 0xFFFF)

# total size
total_len_bin = struct.pack('<H', len(data_block))

# assemble python appvar code
pyappvar_code = header + comment + total_len_bin + data_block + checksum

# write program as python appvar
with open(pyappvar_path, "wb") as wf:
    wf.write(pyappvar_code)

print("[+] Program %s converted with success to %s (%s)"%(os.path.basename(pyfile_path), os.path.basename(pyappvar_path), appvar_name))

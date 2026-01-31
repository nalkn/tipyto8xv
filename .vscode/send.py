# imports
import os
import sys

# get file
py_file = sys.argv[1]
if len(sys.argv) > 2:
    verbose = sys.argv[2] in ["-v", "--verbose"]
else:
    verbose = False

# set filenames
py_filename = os.path.basename(py_file)
py_dirname = os.path.dirname(py_file)

name, ext = os.path.splitext(py_filename)
xv_filename = name+".8xv"
xv_file = os.path.join(py_dirname, xv_filename)

# filter appvar name
trans = str.maketrans({char: '_' for char in '!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~0123456789 '})
appvar_name = name.translate(trans)[:8]

# convert .py to .8xv with tipyconvert.py
print("[*] Converting python file to .8xv")
convert_cmd = "python3 tipyto8xv.py %s %s %s"%(py_file, xv_file, appvar_name)
if os.system(convert_cmd) != 0:
    if verbose:
        print("[-] Command", convert_cmd, "failed")
    print("[-] Error occured when compiling .8xv program file")
    exit()

# send .8xv file with tilp
send_cmd = "tilp -n -s ti83+ %s > /dev/null 2>&1"%xv_file
print(f"[*] Sending .8xv program file")
if os.system(send_cmd) != 0:
    if verbose:
        print("[-] Command", send_cmd, "failed")
    print("[-] Error occured when sending .8xv program file")
    exit()

print("[+] File %s converted and sended to the calculator"%py_filename)
os.remove(xv_file)

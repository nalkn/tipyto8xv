#!/bin/bash

set -e

workdir=$(pwd)

# compile module
echo "[*] Compile module"
cd ../../
source .venv/bin/activate
cd compile-module
python3 tipycomp/tipycomp.py $workdir/module.py $workdir/module-menu $workdir/module.8xv MODULE
deactivate

# compile program
echo "[*] Compile program"
cd $workdir
python3 ../../tipyto8xv.py program.py program.8xv PROGRAM

# send module and program
echo "[*] Send module and program"
tilp -n ti83+ module.8xv program.8xv

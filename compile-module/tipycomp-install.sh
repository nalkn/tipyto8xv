#!/bin/bash

set -e


# args
option=$1

if [ ! -z "$option" ]; then
    if [ "$option" == "--tipydecomp" ]; then
        tipycomp_options=$option
    else
        echo "[-] Unknow option : $option"
        exit 1
    fi
else
    tipycomp_options=""
fi

# variable
workdir=$(pwd)


# update and install dependencies
echo "[*] Updating"
sudo apt update && sudo apt upgrade -y
sudo apt install make python3


# download and compile convbin
cd $workdir
rm -rf convbin
echo "[*] Installing convbin"
git clone --recurse-submodules https://github.com/mateoconlechuga/convbin

echo "[*] Building convbin"
cd convbin
make
sudo cp bin/convbin /usr/local/bin/


# download tipycomp
cd $workdir
rm -rf tipycomp
echo "[*] Installing tipycomp"
git clone $tipycomp_options https://github.com/commandblockguy/tipycomp

if [ ! -z "$tipycomp_options" ]; then
    echo "[*] Building mpy-disasm for tipydecomp"
    cd tipycomp/mpy-disasm
    sed -i 's/^CWARN = -Wall -Werror/#CWARN = -Wall -Werror/' Makefile # disable error-warnings
    make
fi


# install python requirements
cd $workdir
echo "[*] Installing python requirements"
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r tipycomp/requirements.txt
deactivate


# usage
#source .venv/bin/activate
#python3 tipycomp/tipycomp.py main.py menu MAIN.8xv MAIN

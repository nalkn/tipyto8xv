# Compile python module

You can compile a python module to bytecode with [tipycomp](https://github.com/commandblockguy/tipycomp) for a TI calculator.

## Installation

Execute this tipycomp installer :

``` shell
bash ./tipycomp-install.sh
```

NOTE: you can also see tipycomp install instructions in [tipycomp installation](https://github.com/commandblockguy/tipycomp?tab=readme-ov-file#installation)

## Usage

IMPORTANT: The Python AppVar name must be specified in uppercase letters but imported in lowercase letters

### On the computer

Activate the Python3 venv (to use mpy_cross) :

``` shell
source .venv/bin/activate
```

Compile your module with tipycomp :

``` shell
python3 tipycomp/tipycomp.py example.py example-menu EXAMPLE.8xv EXAMPLE
```

IMPORTANT: The Python AppVar name must be specified in uppercase letters but imported in lowercase letters

Send your compiled module to a calculator :

``` shell
tilp -n ti83+ EXAMPLE.8xv
```

### On the calculator

In the `menu` file for your module, the module name is specified by `MENULABEL`.

In the Python App editor, create a file with :

``` python
from module_name import function
```

NOTE: You can also create a program with the `tipyto8xv.py` tool to execute a module.

Now, you can use your module on the calculator !

## Bonus

If you want to decompile a Python module, you can use the `tipydecomp.py` tool (provided in `tipycomp`)

Install tipycomp with `tipydecomp.py` dependencies (it may take some time) :

``` shell
bash ./tipycomp-install.sh --tipydecomp
```

Decompile a Python module :

``` shell
cd tipycomp
python3 tipydecomp.py disasm EXAMPLE.8xv
```

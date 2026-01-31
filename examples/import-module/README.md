# Import a Python module

On the TI calculator, you can use a Python module added by yourself in a Python program.

## Send a program with a module to the calculator

Activate the Python3 venv (to use mpy_cross) :

``` shell
source .venv/bin/activate
```

Compile the Python module :

``` shell
python3 tipycomp/tipycomp.py module.py menu MODULE.8xv MODULE
```

Compile the Python program :

``` shell
python3 tipyto8xv.py program.py PROGRAM.8xv PROGRAM
```

Send your compiled module and program to a calculator :

``` shell
tilp -n ti83+ MODULE.8xv PROGRAM.8xv
```

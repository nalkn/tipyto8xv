# tipyto8xv

To run Python code on a TI calculator, you have two choices :

1) Use a Python module (compiled into bytecode in a .8xv file and cannot be modified), which can be imported into a Python file on the calculator.

2) Use a Python program (compiled into a .8xv Python appvar and can be modified), which can be executed in the Python App on the calculator.

NOTE: you can import your Python module into a Python program with :

``` python
from module_name import function
```

This tutorial shows how to create and send a `python program` to the calculator. If you want to compile a Python module, you can go to [this tutorial](compile-module/README.md).

## Installation

Install python3 and tilp :

``` shell
sudo apt install python3 tilp2
```

## Usage

`
Usage : tipyto8xv.py program.py pyappvar.8xv appvar_name
`

`program.py` is the Python program to convert, `pyappvar.8xv` is the output .8xv and `appvar_name` is the name of the Python file in the calculator Python app (in capital letters).

Convert a Python program to a Python appvar :

``` shell
python3 tipyto8xv.py main.py main.8xv MAIN
```

Send the Python file to the calculator :

``` shell
tilp -n ti83+ main.8xv
```

## Bonus

If you use VsCode, you can send files more easily from the IDE with [this tutorial](examples/vscode-send-file/README.md).

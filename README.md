# tipyto8xv

A tool for convert .py python files to .8xv TI format to send with tilp.

## Installation

Install tilp

``` shell
sudo apt install tilp2
```

## Usage

`
Usage : tipyto8xv.py program.py pyappvar.8xv appvar_name
`

`program.py` is the Python program to convert, `pyappvar.8xv` is the output .8xv and `appvar_name` is the name of the Python file in TI Python app.

Example :

``` shell
python3 tipyto8xv.py main.py main.8xv MAIN
```

Send the python file to the calculator :

``` shell
tilp -n ti83+ main.8xv
```

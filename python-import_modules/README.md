# Python - Import & Modules

This folder is basically me learning how Python handles imports.  
Nothing fancy — just practicing how to bring functions from one file into another and run them.

The tasks here are small scripts that show:
- how to import a single function from a module,
- how to avoid wildcard imports,
- how to make sure code doesn’t run when the file is imported,
- how to work with command‑line arguments,
- and how Python modules behave in general.

## What’s inside

### 0-add.py
Imports `add(a, b)` from `add_0.py` and prints `1 + 2 = 3`.  
Simple start, just checking that imports work.

### 1-calculation.py
Uses functions from `calculator_1.py` to do basic maths with `a = 10` and `b = 5`.  
Prints the results in the required format.

### 2-args.py
Shows how many arguments were passed to the script and lists them.  
Good intro to `sys.argv`.

### 3-infinite_add.py
Adds all command‑line arguments together.  
Useful for understanding loops + argv.

### 4-hidden_discovery.py
Prints names defined inside `hidden_4.pyc`, except the ones starting with `__`.  
A small peek into module internals.

### 5-variable_load.py
Imports a variable from another file and prints it.  
Shows that modules can expose more than just functions.

## Notes

- All scripts follow ALX rules (no wildcard imports, no `__import__`, correct formatting).
- Everything is written in Python 3.
- Each file is executable and meant to be run directly.
- This module is mostly about getting comfortable with imports and understanding how Python organizes code.

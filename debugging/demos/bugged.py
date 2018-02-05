#!/usr/bin/env python3
'''
Command-line entry point for a function that *will* fail.

This can be used to demonstrate entering a `pdb` session directly from a failed
script with command line incantations like:

    python3 -m pdb bugged.py

    python3 -m pdb -c continue bugged.py

    python3 -i bugged.py
    >>> import pdb; pdb.pm()
'''
from testing.linalg import fail_catastrophically

if __name__ == '__main__':
    fail_catastrophically()

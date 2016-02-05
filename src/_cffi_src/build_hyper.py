# coding: utf-8
# Inspired by pyca/cryptography (Apache/BSD)

import os.path

from cffi import FFI


ffi = FFI()
ffi.cdef("""
double hyp2f1 ( double a, double b, double c, double x );
"""
)
ffi.set_source(
    "_hyper",
    """
double hyp2f1 ( double a, double b, double c, double x );
""",
    libraries=["md"],
)


if __name__ == '__main__':
    ffi.compile()

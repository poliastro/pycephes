# coding: utf-8
# Inspired by pyca/cryptography (Apache/BSD)

import os.path

from cffi import FFI


# Source: https://github.com/pyca/cryptography/blob/1.2.x/src/_cffi_src/
with open(os.path.join(
    os.path.dirname(__file__), "cephesx_src/cephesx.h"
)) as f:
    types = f.read()

with open(os.path.join(
    os.path.dirname(__file__), "cephesx_src/hyp2f1x.c"
)) as f:
    functions = f.read()

ffi = FFI()
ffi.cdef(
    types
)
ffi.set_source(
    "_hyper",
    functions
)


if __name__ == '__main__':
    ffi.compile()

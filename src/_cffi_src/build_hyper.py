# coding: utf-8

import os.path

from cffi import FFI


with open(os.path.join(
    os.path.dirname(__file__), "cephes_src/cephesx.h"
)) as f:
    types = f.read()

with open(os.path.join(
    os.path.dirname(__file__), "cephes_src/hyp2f1x.c"
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

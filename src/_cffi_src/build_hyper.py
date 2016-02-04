# coding: utf-8

import os.path

from cffi import FFI
ffi = FFI()

include_dirs = [
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "cephes"),
]
ffi.cdef(
    """
double hyp2f1x ( double a, double b, double c, double x );
"""
)
ffi.set_source(
    "_hyper",
    """
double hyp2f1x ( a, b, c, x )
double a, b, c, x;
{
    return 1.0;
}
""",
    libraries=[],
    include_dirs=include_dirs,
)


if __name__ == '__main__':
    ffi.compile()

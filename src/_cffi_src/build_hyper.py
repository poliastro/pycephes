# coding: utf-8

from cffi import FFI
ffi = FFI()

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
"""
)


if __name__ == '__main__':
    ffi.compile()

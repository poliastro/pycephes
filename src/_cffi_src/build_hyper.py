# Inspired by pyca/cryptography (Apache/BSD)

from cffi import FFI


ffi = FFI()
ffi.cdef("""
double hyp2f1 ( double a, double b, double c, double x );
double vd_hyp2f1 ( int n, double a, double b, double c, double* x, double* res);
""")
ffi.set_source(
    "_hyper",
    """
double hyp2f1 ( double a, double b, double c, double x );

double vd_hyp2f1 ( int n, double a, double b, double c, double* x, double* res) {
    int i;
    for (i=0; i<n; i++)
        res[i] = hyp2f1(a, b, c, x[i]);
}
""",
    libraries=["md"],
)


if __name__ == '__main__':
    ffi.compile()

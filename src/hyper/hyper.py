from numba import njit, cffi_support

import _hyper
cffi_support.register_module(_hyper)

_hyp2f1 = _hyper.lib.hyp2f1x


@njit
def hyp2f1(a, b, c, x):
    return _hyp2f1(a, b, c, x)

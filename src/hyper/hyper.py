import numpy as np
from numba import njit, cffi_support

import _hyper
from _hyper import lib, ffi

cffi_support.register_module(_hyper)

_hyp2f1 = lib.hyp2f1
_vd_hyp2f1 = lib.vd_hyp2f1


@njit
def hyp2f1(a, b, c, x):
    """Gauss hypergeometric function 2F1.

    Parameters
    ----------
    a, b, c, x : float

    """
    if x == 1.0:
        return np.inf

    return _hyp2f1(a, b, c, x)


@njit
def vd_hyp2f1(a, b, c, x):
    """
    Gauss hypergeometric function 2F1 vectorized for float x.

    Parameters
    ----------
    a, b, c : float
    x : array

    """
    res = np.empty_like(x)
    _vd_hyp2f1(
            len(x), a, b, c,
            ffi.from_buffer(x), ffi.from_buffer(res)
    )

    res[x == 1.0] = np.inf
    return res

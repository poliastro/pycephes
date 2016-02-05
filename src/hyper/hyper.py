import numpy as np
from numba import njit, cffi_support

import _hyper
cffi_support.register_module(_hyper)

_hyp2f1 = _hyper.lib.hyp2f1


@njit
def hyp2f1(a, b, c, x):
    if x == 1.0:
        return np.inf

    return _hyp2f1(a, b, c, x)

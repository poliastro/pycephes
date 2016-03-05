import pytest

import numpy as np
from numpy.testing import (
    assert_array_almost_equal, assert_almost_equal
)
from scipy import special

from pycephes import hyper


def test_hyp2f1_battin_scalar():
    x = np.linspace(0, 1, num=11)
    expected_res = special.hyp2f1(3, 1, 5/2, x)

    for ii, x_i in enumerate(x):
        res = hyper.hyp2f1(3, 1, 5/2, x_i)
        assert_almost_equal(res, expected_res[ii])


def test_hyp2f1_battin_array():
    x = np.linspace(0, 1, num=11)
    expected_res = special.hyp2f1(3, 1, 5/2, x)
    res = hyper.vd_hyp2f1(3, 1, 5/2, x)

    assert_array_almost_equal(res, expected_res)

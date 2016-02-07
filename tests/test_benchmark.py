import pytest

from scipy import special

from hyper import hyper


def test_scipy_special(benchmark):
    benchmark(special.hyp2f1, 3, 1, 5/2, 0.1)


def test_hyper(benchmark):
    benchmark(hyper.hyp2f1, 3, 1, 5/2, 0.1)

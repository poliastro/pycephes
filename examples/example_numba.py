# coding: utf-8
from hyper import hyper
from numba import jit


@jit(nopython=True)
def foo(x):
    return (2 * hyper.hyp2f1(1, 1, 1, x) -
            hyper.hyp2f1(1, 1, 1, x) / 3)


if __name__ == '__main__':
    print(foo(1))

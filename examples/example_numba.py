# coding: utf-8
from hyper import hyper
from numba import jit


@jit(nopython=True)
def hyp_battin(x):
    return hyper.hyp2f1(3, 1, 5/2, x)


if __name__ == '__main__':
    print(hyp_battin(0.5))

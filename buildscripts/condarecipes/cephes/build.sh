#!/bin/bash

export LIBRARY_PATH=$PREFIX/lib

make CFLAGS='-O2 -Wall -fno-builtin -fPIC'

install -Dm755 libmd.a $LIBRARY_PATH/libmd.a

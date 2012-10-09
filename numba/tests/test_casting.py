import os
import numpy as np
import ctypes

from numba import *
import numba

@autojit(backend='ast')
def cast_int():
    value = 1.7
    return int32(value)

@autojit(backend='ast')
def cast_complex():
    value = 1.2
    return complex128(value)

@autojit(backend='ast')
def cast_float():
    value = 5
    return float_(value)

@autojit(backend='ast')
def cast_object(dst_type):
    value = np.arange(10, dtype=np.double)
    return dst_type(value)

@autojit(backend='ast')
def cast_as_numba_type_attribute():
    value = 4.4
    return numba.int32(value)

def test_casts():
    assert cast_int() == 1
    assert cast_complex() == 1.2 + 0j
    assert cast_float() == 5.0
    assert np.all(cast_object(double[:]) == np.arange(10))
    assert cast_as_numba_type_attribute() == 4

if __name__ == "__main__":
    test_casts()
#!/usr/bin/env python3

BITS_PER_BYTE = 8
BYTES_PER_WORD = 8
BITS_PER_WORD = BITS_PER_BYTE * BYTES_PER_WORD

def convert():
    pass

"""


abcd

a[x // 8] = x % 8


"""

def raw_convert(i):
    i = i >> 3
    print("a", i)
    return (i // BITS_PER_BYTE, i % BITS_PER_BYTE)

def bin_convert(i):
    i >>= (3)
    print("b", i)
    return (i >> (3), i & (BITS_PER_BYTE - 1))

print("raw")
for i in range(0, 128, BYTES_PER_WORD):
    print(raw_convert(i))

print("bin")
for i in range(0, 128, BYTES_PER_WORD):
    print(bin_convert(i))

print("OK?")
for i in range(0, 512, BYTES_PER_WORD):
    print("i", i)
    a = raw_convert(i)
    b = bin_convert(i)
    print(i, a, b)
    if a != b:
        print(i, a, b)
        break
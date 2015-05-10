#!/usr/bin/env python3

import sys
import os

def main():
    if len(sys.argv) < 2:
        exit("usage: {} <mode=(full, half, mini)>".format(sys.argv[0]))
    
    _, mode, *args = sys.argv
    if mode not in ("full", "half", "mini"):
        exit("error: mode is invaild")
    
    assert not args
    
    os.system(os.path.join(mode, "launch"))

if __name__ == "__main__":
    main()

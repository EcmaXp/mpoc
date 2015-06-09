#!/usr/bin/env python3
import os
import sys

assert __name__ == "__main__"
assert len(sys.argv) == 2, "usage ./classpath.py path"

classpath = []

for path, _, files in os.walk(os.path.abspath(os.path.abspath(sys.argv[1]))):
    for filename in files:
        filepath = os.path.join(path, filename)
        if filepath.endswith(".jar"):
            classpath.append(filepath)

print(":".join(classpath), end="")

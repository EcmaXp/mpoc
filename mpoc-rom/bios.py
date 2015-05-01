import sys
from sys import exit
sys.path.append("../../mpoc-rom")

import microthread
from microthread import MicroThread, pause

@microthread.auto
def hello():
    print(pause(), pause())
    return 32

#hello()
hello.resume()
hello.resume(32)
hello.resume(31)

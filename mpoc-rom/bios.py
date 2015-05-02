import sys
from sys import exit
sys.path.append(".")
sys.path.append(__file__.rpartition("/")[0])

import microthread
from microthread import MicroThread, pause

def dresume(thread, value=None):
    kind, result = thread.resume(value)
    
    if kind == "exception":
        result = repr(result)
    elif result is None:
        result = ""
      
    print(thread.name, kind, result)

@microthread.auto(3, 2)
def hello(a, b):
    print(a, b)
    print(pause(3), pause())
    return 32

print(hello)
dresume(hello)
dresume(hello, 32)
dresume(hello, 31)

import utime

def gen():
    pass

class sup():
    def __enter__(self):
        pause()

    def __exit__(self, a, b, c):
        pass

for i in range(1, 16 + 1):
    @microthread.auto()
    def evil():
        "i am evil!"
        for i in range(1024 * 1024 * 1024):
            pass
    
    limit = 1 + i * 1024 * 1024
    evil.cpu_hard_limit = limit
    evil.cpu_soft_limit = limit >> 1
    
    a = utime.time()
    dresume(evil)
    b = utime.time()
    
    print(i, "M =>", round((b - a) * 1000), "ms")

print("haha!")

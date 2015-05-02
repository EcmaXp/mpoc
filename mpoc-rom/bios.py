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

@microthread.auto
def hello():
    print(pause(3), pause())
    return 32

#hello()
dresume(hello)
dresume(hello, 32)
dresume(hello, 31)

import utime

for i in range(1, 16 + 1):
    @microthread.auto
    def evil():
        "i am evil!"
        for k in range(1024 * 1024):
            pass
    
    limit = 1 + i * 1024 * 1024
    evil.cpu_hard_limit = limit
    #evil.cpu_soft_limit = limit
    
    a = utime.time()
    try:
        print(evil.resume())
    except:
        print("hard")
    else:
        print("soft")
    b = utime.time()
    
    print(i, "M =>", round((b - a) * 1000), "ms")

print("haha!")

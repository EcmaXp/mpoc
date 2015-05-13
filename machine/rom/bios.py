import sys
from sys import exit

__path__ = __file__.rpartition("/")[0]
print(sys.path)
sys.path.extend([
    ".",
    __path__,
    __path__ + "/oclib",
    __path__ + "/pylib",
])

import utime
import microthread

import mpoc
import utime

from taskmgr import *
import taskmgr

from opencom import syscall

def hello(t:int) -> int:
    pass

@taskmgr.auto()
def bios():
    def syscall_dbg(funcname, *args):
        result = syscall(funcname, *args)
        print('>', result)
        return result

    syscall_dbg("hello", 3)
    syscall_dbg("hello2", "world!")
    syscall_dbg("hello2", "world2!")

taskmgr.run(bios)

import gc
print(gc.collect())
print(gc.mem_alloc(), gc.mem_free(), '/', gc.mem_alloc() + gc.mem_free(), "KB")

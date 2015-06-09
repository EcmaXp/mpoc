import sys
from sys import exit
import jnupy

# TODO: move bios.py to micropython/opencom/main.py
__path__ = __file__.rpartition("/")[0]
sys.path.extend([
    ".",
    __path__,
    __path__ + "/oclib",
    __path__ + "/pylib",
    jnupy.getenv("MPOC_ROM"),
    jnupy.getenv("MICROPYTHON_BATTERY"),
])

import utime
import microthread

import jnupy

import utime

from taskmgr import *
import taskmgr

from opencom import syscall

def hello(t:int) -> int:
    pass

print(hello)

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
print(gc.mem_alloc(), '/', gc.mem_alloc() + gc.mem_free(), "KB")

def main():
    pass

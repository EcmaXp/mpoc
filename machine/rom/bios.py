import sys
from sys import exit

__path__ = __file__.rpartition("/")[0]
sys.path.extend([
    ".",
    __path__,
    __path__ + "/oclib",
    __path__ + "/pylib",
])

if len(sys.argv) == 1:
    from code import interact
    interact()
else:
    # ('<java>', '-X', 'emit=bytecode', 'basics/0prelim.py')
    if sys.argv[1:3] == ("-X", 'emit=bytecode'):
        sys.argv = (sys.argv[0],) + sys.argv[3:]
    import jnupy
    try:
        content = jnupy.readfile(sys.argv[1])
    except Exception as e:
        print('reading file {!r} failed'.format(sys.argv[1]))
        print(e)
        exit(1)
    sys.argv = sys.argv[1:]
    exec(content)
    exit()

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

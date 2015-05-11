import sys
from sys import exit
sys.path.append(".")
sys.path.append(__file__.rpartition("/")[0] + "/lib")

import mpoc
import utime

from taskmgr import *
import taskmgr

from opencom import syscall

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


__all__ = ["sysfunc", "syscall"]

import taskmgr
from taskmgr import call, pause

_System = {}
def sysfunc(func, funcname=None):
    if funcname is None:
        funcname = func.__name__
    
    _System[funcname] = func
    return func

def gen_sysfunc(apiname):
    return sysfunc

def syscall(funcname, *args):
    return call(system_thread, (funcname, args))

@taskmgr.ready
@taskmgr.auto()
def system_thread():
    result = None
    try:
        while True:
            call_info = pause(result)
            funcname, args = call_info
            
            func = _System.get(funcname)
            if func is None:
                result = None, NameError(funcname)
                continue
            
            try:
                result = func(*args), None
            except BaseException as e:
                result = None, e
    except:
        print("!?")
        raise

from . import world

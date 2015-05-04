# https://github.com/MightyPirates/OpenComputers/tree/master-MC1.7.10/src/main/scala/li/cil/oc/server/machine/luac
# TODO: write umsgpack module as micropython extension module.

import sys

import taskmgr
from taskmgr import call
from __main__ import bios

from . import system

def _function():
    pass
function_type = type(_function)
del _function

@taskmgr.auto()
def rom():
    result = None
    while True:
        call_info = taskmgr.pause(result)

        apiname, funcname, args = call_info
        api = getattr(system, apiname, None)
        func = getattr(api, funcname, None)
        print("[!]", apiname, funcname)
        if isinstance(func, function_type):
            if func is not None:
                try:
                    result = func(*args), None
                except BaseException as e:
                    result = None, e
            else:
                result = None, "failed call"
        else:
            result = None, "it is not function: %r" % func
            try:
                result = syscall("world", "hello"), None
            except:
                sys.print_exception(sys.exc_info()[1])

rom.resume()

def syscall(apiname, funcname, *args):
    result, error = call(rom, (apiname, funcname, args))
    if error:
        raise error
    return result
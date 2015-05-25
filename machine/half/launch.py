#!/usr/bin/env jython

if __name__ != "__main__":
    exit("error: this module must be running as main")

import sys
import os
import platform
import glob

if platform.system() != "Java":
    exit("error: not running from java")
print(sys.argv[1])

from java.lang import System

def get_absenv(name):
    res = os.environ.get(name)
    if not res:
        exit("error: {} is unset" .format(name))
    return os.path.abspath(res)

# should load first!
sys.path.insert(0, get_absenv("VIRTUAL_JAR"))

import java.lang.Exception

MPOC_ROM = get_absenv("MPOC_ROM")

try:
    import li.cil.oc
except ImportError:
    print("warn: import OpenCom is failed")

try:
    from kr.pe.ecmaxp.mpoc.virtual import JNLuaPreloader
    JNLuaPreloader().init()
except:
    print("warn: init JNLua are failed")

try:
    from li.cil.repack.com.naef.jnlua import LuaState
except:
    print("warn: init LuaState are failed")

try:
    from kr.pe.ecmaxp.micropython import PythonState
except:
    print("warn: init PythonState are failed")

try:
    lua = LuaState()
except:
    print('warn: make LuaState are failed')

try:
    _glob = globals()
    py = PythonState()
    for name in dir(py):
        if name.startswith("mp_"):
            _glob[name] = getattr(py, name)
    del _glob
except:
    print("warn: make PythonState are failed")

import code; code.interact(None, raw_input, globals())

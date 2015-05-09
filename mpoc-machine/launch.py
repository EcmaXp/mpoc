#!/usr/bin/env jython

if __name__ != "__main__":
    exit("error: this module must be running as main")

import sys
import os
import platform
import glob

if platform.system() != "Java":
    exit("error: not running from java")
    
from java.lang import System

def get_absenv(name):
    res = os.environ.get(name)
    if not res:
        exit("error: {} is unset" .format(res))
    return os.path.abspath(res)

MPOC_ROM = get_absenv("MPOC_ROM")

for path, _, files in os.walk(os.path.abspath(get_absenv("FORGE_LIB"))):
    for filename in files:
        filepath = os.path.join(path, filename)
        if filepath.endswith(".jar"):
            sys.path.append(filepath)

for name in "OPENCOM_JAR", "OPENCOM_JNLUA_JAR", "OPENCOM_LUAJ_JAR":
    sys.path.append(get_absenv(name))

import li.cil.repack.com.naef.jnlua.LuaState

System.load(get_absenv("OPENCOM_RAW_LIB"))

try:
    import li.cil.oc
except ImportError:
    exit("error: import OpenCom is failed")

from li.cil.oc.util import LuaStateFactory
#from li.cil.oc.server.machine.luac import NativeLuaArchitecture

import code
code.interact()

print(sys.argv[1])
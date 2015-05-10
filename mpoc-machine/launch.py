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
        exit("error: {} is unset" .format(name))
    return os.path.abspath(res)

# should load first!
sys.path.insert(0, get_absenv("VIRTUAL_JAR"))

import java.lang.Exception

MPOC_ROM = get_absenv("MPOC_ROM")

try:
    import li.cil.oc
except ImportError:
    exit("error: import OpenCom is failed")

try:
    from kr.pe.ecmaxp.mpoc.virtual import JNLuaPreloader
    JNLuaPreloader().init()
except:
    print("error: init JNLua are failed")
    raise

from li.cil.oc.util import LuaStateFactory
lua = LuaStateFactory.createState().x()

import code; code.interact(None, raw_input, globals())

print(sys.argv[1])

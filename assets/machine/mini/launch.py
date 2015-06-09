#!/usr/bin/env python3
import sys
import subprocess
import threading
import time
import os

def main():
    subprocess.check_call(["./build.py"])
    
    os.chdir("../../micropython/opencom")
    MPOC_BIOS = os.path.abspath("../../machine/rom/bios.py")

    cmdline = ["./micropython"]
    if len(sys.argv) == 1:
        cmdline += [MPOC_BIOS]
    elif len(sys.argv) >= 2:
        if sys.argv[1] == "build!":
            exit(0)
        
        cmdline += sys.argv[1:]
    else:
        exit("usage: ./r [file] [args ...]")
    
    proc = subprocess.Popen(cmdline,
        stdin=subprocess.PIPE,
    )
    
    try:
        proc.stdin.close()
        
        exitcode = proc.wait()
        if exitcode == -11:
            print("Segmentation fault")
        elif exitcode < 0:
            print("Exit Code:", exitcode)
            
        exit(exitcode)
    except KeyboardInterrupt:
        proc.kill()

if __name__ == "__main__":
    main()
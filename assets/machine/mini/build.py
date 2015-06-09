#!/usr/bin/env python3
import sys
import subprocess
import time
import os

os.chdir(__file__.rpartition("/")[0])
os.chdir("../../micropython/opencom")

if not os.environ.get("CROSS_COMPILE"):
    if subprocess.call(["ccache", "-V"], stdout=subprocess.PIPE) == 0:
        os.environ["CROSS_COMPILE"] = "ccache "

exit(os.system("make"))

import jnupy
import oc
import sys
import microthread
from microthread import pause

__all__ = ["kernel"]

class Component():
    def __init__(self, name=None, address=None):
        components = oc.component.getList()
        for key, value in components.items():
            if value == name:
                address = key
                break
            elif key == address:
                name = value
                break
        else:
            raise LookupError("there is no component (name={}, address={})".format(name, address))

        self.name = name
        self.address = address

    def __getattr__(self, name):
        def wrapper(*args):
            # TODO: detect direct and non-direct function
            #pause(oc.execution.SynchonizedCall())
            result = oc.component.invoke(self.address, name, args)
            #pause(oc.execution.Sleep(0))
            return result
        return wrapper

import micropython

class Components():
    def __getattr__(self, item):
        return Component(item)

def system():
    i = 0
    components = Components()
    gpu = components.gpu
    screen = components.screen
    gpu.bind(screen.address)
    gpu.setBackground(0x000000)
    gpu.setForeground(0xFFFFFF)
    gpu.fill(1, 1, 80, 25, " ")

    gpu.set(1, 1, "hello world in MicroPython")

    x = 1
    while True:
        signal = oc.computer.pullSignal()
        if not signal:
            pause(oc.execution.Sleep(0))
            continue

        print(signal)
        name, args = signal
        if name == "key_down":
            address, ch, limit, user = args
            ch = int(ch)
            char = chr(ch)
            gpu.set(x, 2, char)
            x += 1


class Kernel():
    def __init__(self):
        self.count = 0

    def __call__(self, command, *args):
        return getattr(self, command)(*args)
    
    def initialize(self):
        import microthread
        self.system = microthread.MicroThread("system-{}".format(self), system)
        self.system.cpu_safe_limit = 10000
        self.system.cpu_soft_limit = 100000
        self.system.cpu_hard_limit = 1000000
        return True

    def _execute(self):
        self.system.cpu_current_executed = 0
        status, result = self.system.resume()
        if status == microthread.STATUS_PAUSE:
            return result
        elif status == microthread.STATUS_FORCE_PAUSE:
            return oc.execution.Sleep(0)
        elif status == microthread.STATUS_EXCEPTION:
            raise result
        elif status == microthread.STATUS_NORMAL:
            return oc.execution.Shutdown(bool(result))
        elif status == microthread.STATUS_LIMIT:
            if result == microthread.LIMIT_SOFT:
                # didn't handled.
                return oc.execution.Error("system running too long")
            elif result == microthread.LIMIT_HARD:
                return oc.execution.Error("system running too long long")

        print(status, result)
        return oc.execution.Error("unknown state")

    def threaded(self, *_):
        return self._execute()

    def synchronized(self, *_):
        return self._execute()

    def close(self):
        return True

    def force_close(self):
        return True

rawkernel = Kernel()

def kernel(*args):
    try:
        result = rawkernel(*args)
        found = repr(result).partition("$")[2].partition("@")[0]
        # print("kernel", args, '->', found or result)
        return result
    except BaseException as e:
        # print("kernel", args)
        print("kernel-exception", e)
        sys.print_exception(e)
        return oc.execution.Error("exception: " + repr(e))

if oc.fake:
    def main():
        import sys
        try:
            kernel.initialize()
            kernel.threaded()
            kernel.close()
        except BaseException as e:
            sys.print_exception(e)
        
        import code
        code.interact(local=globals())

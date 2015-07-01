import jnupy
import oc

__all__ = ["kernel"]

# Sleep, Shutdown, SynchronizedCall, Error

class Kernel():
    def __init__(self):
        pass

    def __call__(self, command, *args):
        return getattr(self, command)(*args)
    
    def initialize(self):
        pass

    def threaded(self, is_synchronized):
        pass
    
    def synchronized(self):
        pass

    def close(self):
        pass

kernel = Kernel()

if oc.fake:
    def main():
        import sys
        try:
            kernel.initialize()
            kernel.threaded(False)
            kernel.close()
        except BaseException as e:
            sys.print_exception(e)
        
        import code
        code.interact(local=globals())

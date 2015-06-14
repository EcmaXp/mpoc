import sys

try:
    import jnupy
    import oc
    import sys
    
    __path__ = __file__.rpartition("/")[0]
    
    def _setup_fake():
        assert not hasattr(oc, "__file__")
        fake = __path__ + "/fake"
        oc.__file__ = fake + "/__init__.py"
        sys.path.append(fake)
    
    try:
        import oc.machine
    except ImportError:
        _setup_fake()
        import oc.machine
        
    # Sleep, Shutdown, SynchronizedCall, Error
    
    def kernel_body(command, *args):
        pass
    
    def kernel(command, *args):
        try:
            return kernel_body(command, *args)
        except:
            # DO FINAL HANDLE EXCEPTION...
            raise
    
    print("machine executed")
    #from oc.bios import kernel
except SystemExit:
    raise
except BaseException as e:
    sys.print_exception(e)
    raise

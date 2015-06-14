import sys

try:
    import jnupy
except ImportError:
    sys.exit("error: program must launch by jnupy")

try:
    __path__ = __file__.rpartition("/")[0]
    sys.path.append(__path__)
    
    try:
        import oc
        oc.fake = False
    except ImportError:
        sys.path.append(__path__ + "/__fake__")
        import oc
        oc.fake = True

    import bios
    from bios import kernel

    if oc.fake:
        bios.main()
except SystemExit:
    raise
except BaseException as e:
    sys.print_exception(e)
    raise

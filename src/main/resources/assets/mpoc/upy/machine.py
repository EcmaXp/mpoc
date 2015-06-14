import sys

try:
    import jnupy
except ImportError:
    sys.exit("error: program must launch by jnupy")

try:
    __path__ = __file__.rpartition("/")[0]
    sys.path.append(__path__)
    sys.path.append(__path__ + "/oclib")
    sys.path.append(__path__ + "/pylib")
    
    battery = jnupy.getenv("MICROPYTHON_BATTERY")
    assert battery
    sys.path.append(battery)
        
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

FORCE_DEV = True
if FORCE_DEV:
    __file__ = "C:\\Users\\EcmaXp\\Documents\\GitHub\\mpoc\\src\\main\\resources\\assets\\mpoc\\upy\\machine.py"
    MICROPYTHON_BATTERY = "C:\\Users\\EcmaXp\\Documents\\GitHub\\mpoc\\assets\\micropython\\opencom\\lib"
else:
    MICROPYTHON_BATTERY = None

def __system__():
    print("succes starting...")
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
        assert battery or MICROPYTHON_BATTERY
        sys.path.append(battery or MICROPYTHON_BATTERY)

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

        return kernel
    except SystemExit:
        raise
    except BaseException as e:
        sys.print_exception(e)
        raise

try:
    kernel = __system__()
except:
    kernel = None

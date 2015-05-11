
def Callback(**kwargs):
    def wrap(func):
        return func

    return warp
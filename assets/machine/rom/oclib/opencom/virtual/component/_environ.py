
class Component():
    def __init__(self):
        self.address = None

def Callback(**kwargs):
    def wrap(func):
        return func

    return warp
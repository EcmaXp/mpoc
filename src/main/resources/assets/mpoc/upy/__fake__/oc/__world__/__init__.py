
__all__ = ["components"]

component_info = {}

class Component():
    def __init__(self, address=None):
        self.address = address

def Callback(**kwargs):
    def wrap(func):
        component_info[func] = kwargs
        return func

    return wrap
    
import random
def uuid4():
    def gen_randchar():
        return "0123456789abcdef"[random.randrange(16)]
    
    def gen_randstr(length):
        return "".join(gen_randchar() for i in range(length))
    
    return "-".join((gen_randstr(length) for length in (8, 4, 4, 4, 12)))

from . import component
from .component import *

components = [
    EEPROM(uuid4(), "?"),
]


from . import gen_sysfunc
sysfunc = gen_sysfunc(__name__)

@sysfunc
def hello(ret):
    return ret
    
@sysfunc
def hello2(ret):
    return "?" + repr(ret)

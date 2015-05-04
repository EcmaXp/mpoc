
import microthread
from microthread import auto, pause as _pause
from microthread import *
import utime

stacks = []

def pause(value=None):
    result = _pause(value)
    return result

def run(start_thread):
    thread = start_thread
    value = None
    while True:
        last_thread = thread
        print('>', thread.name, value)
        kind, result = thread.resume(value)
        if kind == STATUS_PAUSE:
            if stacks:
                thread = stacks.pop()
                value = result
            else:
                thread = start_thread
                value = result
        elif kind == STATUS_FORCE_PAUSE:
            value = None
        else:
            value = None
        
        print('<', last_thread.name, kind, result)
        utime.sleep(0.25)
    
def call(thread, value=None):
    stacks.append(thread)
    result = _pause(value)
    return result

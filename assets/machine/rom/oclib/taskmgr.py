
__all__ = ["pause", "call"]

import sys
import microthread
from microthread import pause as _pause, auto, current_thread
from microthread import STATUS_NORMAL, STATUS_YIELD, STATUS_EXCEPTION, \
    STATUS_LIMIT, STATUS_PAUSE, STATUS_FORCE_PAUSE, STATUS_STOP, \
    LIMIT_SOFT, LIMIT_HARD
    
import utime

call_stack = []

def ready(thread):
    call_stack.append(None)
    call_stack.append(None)
    status, result = thread()
    if status == STATUS_EXCEPTION:
        raise result
    elif status != STATUS_PAUSE:
        raise RuntimeError("{} given {} state with {}".format(thread.name, status, result))
    call_stack.pop()
    return thread

def pause(value=None):
    call_stack.pop()
    return _pause((call_stack[-1], value))

def call(func, value=None):
    call_stack.append(func)
    result, error = _pause((func, value))
    if error:
        raise error
    return result

def run(bios):
    thread = bios
    send_value = None
    call_stack.append(bios)
    while call_stack:
        print('[%i] %s(%r)' % (len(call_stack), thread.name, send_value))
        status, result = thread(send_value)
        next_thread = None
        if status != STATUS_PAUSE:
            print('[+]', '%s -> %s: %s' % (thread.name, status, result))
        
        if status == STATUS_PAUSE:
            next_thread, send_value = result
            
        elif status == STATUS_EXCEPTION:
            print("=" * 5, "exception on", thread.name, "=" * 5)
            sys.print_exception(result)
            print("=" * 20)
            call_stack.pop()
            send_value = None
        elif status == STATUS_STOP:
            call_stack.pop()
            send_value = None
        else:
            send_value = None
        
        if next_thread is None:
            next_thread = bios
        
        thread = next_thread
        utime.sleep(0.05)

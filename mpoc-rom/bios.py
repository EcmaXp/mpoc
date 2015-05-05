import sys
from sys import exit
sys.path.append(".")
sys.path.append(__file__.rpartition("/")[0] + "/lib")

import utime

import microthread
from microthread import pause as _pause
from microthread import STATUS_NORMAL, STATUS_YIELD, STATUS_EXCEPTION, \
    STATUS_LIMIT, STATUS_PAUSE, STATUS_FORCE_PAUSE, STATUS_STOP, \
    LIMIT_SOFT, LIMIT_HARD

@microthread.auto()
def hello():
    try:
        import sys
        print(hex)
        while True:
            pass
    except:
        print("?")

hello.cpu_hard_limit = 256
print(hello())
print(hello())
exit()

call_stack = []

def pause(value=None):
    call_stack.pop()
    return _pause((call_stack[-1], value))

def call(func, value=None):
    call_stack.append(func)
    result, error = _pause((func, value))
    if error:
        raise error
    return result

def thread_ready_call(func):
    call_stack.append(None)
    call_stack.append(None)
    print(func())
    call_stack.pop()
    return func

System = {}
def system_func(func):
    System[func.__name__] = func
    return func

@system_func
def hello(a):
    return a + 1
    
@system_func
def hello2(b):
    return b + "hello"

@thread_ready_call
@microthread.auto()
def system():
    result = None
    while True:
        call_info = pause(result)
        funcname, args = call_info
        
        try:
            result = System.get(funcname)(*args), None
        except BaseException as e:
            result = None, e

def syscall(funcname, *args):
    return call(system, (funcname, args))

@microthread.auto()
def bios():
    class test():
        def world(self):
            _pause(self)
            return 32
        
    world = microthread.auto()(test().world)
    print(world())
    print(world())
    print(world())
    
    closure = None
    @microthread.auto()
    def closure_func():
        nonlocal closure
        closure = 32
        _pause()
        return closure
    print(closure_func())
    print(closure_func())
    print(closure_func())
    
    def syscall_dbg(funcname, *args):
        result = syscall(funcname, *args)
        print('>', result)
        return result

    syscall_dbg("hello", 3)
    syscall_dbg("hello2", "world!")
    syscall_dbg("hello2", "world2!")

def run():
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
        utime.sleep(0.25)

run()

"""
import taskmgr

@taskmgr.auto()
def bios():
    while True:
        syscall("world", "hello")
        syscall("world", "hello2")
        
from opencom import syscall

taskmgr.run(bios)
"""
oc_kernel = None
oc_machine = None
from pprint import pprint
import sys
import imp
from li.cil.oc.api.machine import ExecutionResult
oc_module = sys.modules["oc"] = imp.new_module("oc")

def kernel():
	call = None
	while True:
		value = (yield call)
		print(call, value)
		pprint(dir(oc_machine))
		components = {value: key for key, value in oc_machine.components().items()}
		oc_machine.invoke(components["computer"], "beep", [1000])
		call = ExecutionResult.Sleep(0)

oc_core = kernel()
next(oc_core)

def oc_invoke(*args):
	try:
		return oc_core.send(args)
	except BaseException as e:
		print("fail", e)
		print(args)

def oc_import(module):
	setattr(oc_module, module.__name__, module)

pass

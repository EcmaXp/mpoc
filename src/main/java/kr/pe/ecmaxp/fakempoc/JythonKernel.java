package kr.pe.ecmaxp.fakempoc;

import org.python.core.*;
import org.python.util.PythonInterpreter;

public class JythonKernel {
	private PythonInterpreter state;
	
	public JythonKernel() {
		state = new PythonInterpreter();
		state.execfile("D:\\Users\\EcmaXp\\Documents\\MCMods\\mpoc\\machine.py");
		state.set("oc_kernel", Py.java2py(this));
	}
	
	public PythonInterpreter getState() {
		return state;
	}

	public Object invoke(Object ... args) {
		PyObject[] pyargs = Py.javas2pys(args);
		PyObject invoke = state.get("oc_invoke");
		PyObject result = invoke.__call__(pyargs);
		return result.__tojava__(Object.class);
	}
	
	public static void main(String[] args) {
		JythonKernel kernel = new JythonKernel();
		kernel.invoke();
	}
}

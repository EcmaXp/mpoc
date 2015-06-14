package MPOC;
import org.micropython.jnupy.*;
import org.micropython.jnupy.JavaFunction.*;

public class OpenComPythonState extends PythonState {
    public static void main(String args[]) {
		System.gc(); // Remove incorrect reference.
		OpenComPythonState py;
	    
		try {
			py = new OpenComPythonState();
		} catch (PythonException e) {
			throw new RuntimeException("createing state are failed", e);
		}
		
		if (args.length == 0) {
			throw new RuntimeException("launch OpenComPythonState require the launcher are writtern in Python.");
		}
		
		try {
		    PythonModule mococ = py.newModule("oc");
		    // just place fake module.
		    
			PythonModule modsys = py.importModule("sys");

			PythonObject argv = py.getBuiltin("list").rawCall();
			for (String arg : args) {
				argv.attr("append").call(arg);
			}
			modsys.set("argv", argv);

			String launcher = args[0];
			PythonModule modmain = py.getMainModule();
			modmain.set("__file__", launcher);
			
			String code = py.readFile(launcher);
			py.execute(code);
		} catch (PythonException e) {
			String name = e.getName();
			if (name.equals("SystemExit")) {
				System.exit(0);
			}
			
			e.printStackTrace();
			System.exit(1);
		}
	}
	
	public OpenComPythonState() throws PythonException {
	    super();
	}
}

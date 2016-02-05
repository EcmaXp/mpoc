package kr.pe.ecmaxp.mpoc.api;

// import li.cil.oc.util.GameTimeFormatter;
import li.cil.oc.api.machine.Signal;

import org.micropython.jnupy.PythonState;
import org.micropython.jnupy.PythonModule;
import org.micropython.jnupy.PythonObject;
import org.micropython.jnupy.PythonArguments;
import org.micropython.jnupy.PythonException;

import org.micropython.jnupy.JavaFunction.*;

import kr.pe.ecmaxp.mpoc.MicroPythonArch;
import net.minecraft.nbt.NBTTagCompound;

public class ComputerAPI extends MicroPythonAPI {
    public ComputerAPI(MicroPythonArch owner) {
        super(owner);
    }
    
    public void initialize() throws PythonException {
        PythonModule module = owner.newOCModule("computer");
        
        module.set(new NamedJavaFun0("pullSignal") {
            @Override
			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
            	Signal signal = machine.popSignal();
            	if (signal == null) {
            		return null;
            	}
            	
            	PythonObject result = pythonState.getBuiltin("list").rawCall();
            	PythonObject append = result.attr("append");
            	append.rawCall(signal.name());
            	append.invoke((Object) signal.args());
            	
        		return pythonState.getBuiltin("tuple").rawCall(result);
			}
        });
        
        module.set(new NamedJavaFun2("pushSignal") {
            @Override
			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
            	String name = (String) args.get(0);
            	Object[] fargs = (Object[]) args.get(1);
            	
            	return new Boolean(machine.signal(name, fargs));
			}
        });
    }

    @Override
	public void load(NBTTagCompound nbt) {

	}

    @Override
	public void save(NBTTagCompound nbt) {

	}
}

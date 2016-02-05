package kr.pe.ecmaxp.mpoc.api;

import li.cil.oc.api.machine.ExecutionResult;
// import li.cil.oc.util.GameTimeFormatter;

import org.micropython.jnupy.PythonState;
import org.micropython.jnupy.PythonModule;
import org.micropython.jnupy.PythonArguments;
import org.micropython.jnupy.PythonException;
import org.micropython.jnupy.JavaFunction.*;
import org.micropython.jnupy.JavaObject;

import kr.pe.ecmaxp.mpoc.MicroPythonArch;
import net.minecraft.nbt.NBTTagCompound;

public class ExecutionAPI extends MicroPythonAPI {
    public ExecutionAPI(MicroPythonArch owner) {
        super(owner);
    }
    
    public void initialize() throws PythonException {
        PythonModule module = owner.newOCModule("execution");

        module.set(new NamedJavaFun1("Error") {
            @Override
			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
            	System.out.println("Error");
            	return new JavaObject(new ExecutionResult.Error((String)args.get(0)));
			}
        });
        
        module.set(new NamedJavaFun1("Shutdown") {
            @Override
			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
            	System.out.println("Shutdown");
				return new JavaObject(new ExecutionResult.Shutdown(((Boolean)args.get(0)).booleanValue()));
			}
        });
        
        module.set(new NamedJavaFun0("SynchonizedCall") {
            @Override
			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
            	System.out.println("SynchonizedCall");
            	return new JavaObject(new ExecutionResult.SynchronizedCall());
			}
        });

        module.set(new NamedJavaFun1("Sleep") {
            @Override
			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
            	System.out.println("Sleep");
            	return new JavaObject(new ExecutionResult.Sleep(((Integer)args.get(0)).intValue()));
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

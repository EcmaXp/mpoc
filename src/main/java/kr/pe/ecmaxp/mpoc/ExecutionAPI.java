package kr.pe.ecmaxp.mpoc;

import li.cil.oc.api.machine.ExecutionResult;
import li.cil.oc.api.machine.Machine;
// import li.cil.oc.util.GameTimeFormatter;

import org.micropython.jnupy.PythonState;
import org.micropython.jnupy.PythonModule;
import org.micropython.jnupy.PythonObject;
import org.micropython.jnupy.PythonArguments;
import org.micropython.jnupy.PythonException;
import org.micropython.jnupy.JavaFunction.*;

import net.minecraft.nbt.NBTTagCompound;

public class ExecutionAPI extends MicroPythonAPI {
    public ExecutionAPI(MicroPythonArch owner) {
        super(owner);
    }
    
    public void initialize() throws PythonException {
        PythonState pystate = owner.pystate;
        PythonModule module = owner.newOCModule("execution");
        
        module.set(new NamedJavaFun1("Error") {
            @Override
			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
				return new ExecutionResult.Error((String)args.get(0));
			}
        });
        
        module.set(new NamedJavaFun1("Shutdown") {
            @Override
			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
				return new ExecutionResult.Shutdown(((Boolean)args.get(0)).booleanValue());
			}
        });
        
        module.set(new NamedJavaFun0("SynchonizedCall") {
            @Override
			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
				return new ExecutionResult.SynchronizedCall();
			}
        });

        module.set(new NamedJavaFun1("Sleep") {
            @Override
			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
				return new ExecutionResult.Sleep(((Integer)args.get(0)).intValue());
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

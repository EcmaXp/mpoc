package kr.pe.ecmaxp.fakempoc;

import net.minecraft.item.ItemStack;
import net.minecraft.nbt.NBTTagCompound;
import li.cil.oc.api.machine.Architecture;
import li.cil.oc.api.machine.ExecutionResult;
import li.cil.oc.api.machine.Machine;


// import li.cil.oc.Settings;

import org.python.util.PythonInterpreter;
import org.python.core.*;

@Architecture.Name("Jython")
public class JythonArch implements Architecture {
    private boolean inited;
    
    private PythonInterpreter state;
    private JythonKernel kernel;
    private ExecutionResult lastSyncResult;
    Machine machine;

    public JythonArch(Machine machine) {
        this.machine = machine;
        this.inited = true;
    }

    @Override
    public boolean isInitialized() {
        return (inited && this.kernel != null);
    }

    @Override
    public boolean recomputeMemory(Iterable<ItemStack> components) {
        // TODO: if memory changed then crash? (or return false??)
        // NOTE: MicroPython can't limit memory with dynamic size
        return true;
    }
        
    public boolean initialize() {        
        this.kernel = new JythonKernel();
        this.state = kernel.getState();
        this.state.set("oc_machine", machine);
        return true;
    }

    ExecutionResult invoke(Object ...args) {
    	assert(args.length >= 1) && (args[0] instanceof String);
    	String command = (String)args[0];
    	
    	try {
            Object result = rawInvoke(args);
            if (result instanceof ExecutionResult) {
                return (ExecutionResult) result;
            } else if (result == null) {
                return new ExecutionResult.Error("kernel(" + command + ") return null");
            } else {
                return new ExecutionResult.Error("kernel(" + command + ") return unknown object : " + result.toString());
            }
        } catch (Exception e) {
            return new ExecutionResult.Error("kerenl has error: " + e.toString());
        }
    }

    Object rawInvoke(Object ...args) throws Exception {
    	return this.kernel.invoke(args);
    }
    
    public void close() {
        this.kernel = null;
    }

    public void runSynchronized() {
    	assert(this.lastSyncResult == null);
    	this.lastSyncResult = invoke("synchronized");
    }
    
    public ExecutionResult runThreaded(boolean isSynchronizedReturn) {
    	if (isSynchronizedReturn) {
    		assert(this.lastSyncResult != null);
    		ExecutionResult result = this.lastSyncResult;
    		this.lastSyncResult = null;

    		return result;
    	}
    	
        return invoke("threaded");
    }

    public void onConnect() {
    }

    @Override
    public void load(NBTTagCompound nbt) {
        // ?
    }

    @Override
    public void save(NBTTagCompound nbt) {
        // ?
    }

	public Machine getMachine() {
		return this.machine;
	}

	public PyModule newOCModule(String string) {
		PyModule module = new PyModule(string);
		state.get("oc_import").__call__(module);
		return module;
	}
}

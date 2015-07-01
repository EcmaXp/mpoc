package kr.pe.ecmaxp.mpoc;

import net.minecraft.item.ItemStack;
import net.minecraft.nbt.NBTTagCompound;

import li.cil.oc.api.machine.Architecture;
import li.cil.oc.api.machine.ExecutionResult;
import li.cil.oc.api.machine.Machine;
import li.cil.oc.api.machine.Signal;

import li.cil.oc.Settings;

import org.micropython.jnupy.PythonState;
import org.micropython.jnupy.PythonObject;
import org.micropython.jnupy.PythonModule;
import org.micropython.jnupy.PythonException;
import org.micropython.jnupy.PythonImportStat;

@Architecture.Name("MicroPython")
public class MicroPythonArch {
    private ArrayList<MicroPythonAPI> apis;
    private inited;
    
    private PythonModule ocmod;
    private PythonObject kernel;
    
    Machine machine;
    PythonState pystate;
    
    public MicroPythonArch(Machine machine) {
        this.apis = new ArrayList<MicroPythonAPI>();
        this.machine = machine;
        this.inited = false;
        
        this.apis.add(new MicroPythonAPI(this));
    }

    @Override
    public boolean isInitialized() {
        return (this.kernel != null);
    }

    @Override
    public boolean recomputeMemory(Iterable<ItemStack> components) {
        // TODO: if memory changed then crash? (or return false??)
        // NOTE: MicroPython can't limit memory with dynamic size
        return true;
    }

    private int computeMemory() {
        // TODO: compute memory from components
        
        // 512 KB
        return 512 * 1024;
    }

    @Override
    public boolean initialize() {
        close();
        
        int memorySize = computeMemory()
        PythonState pystate = new PythonState(memorySize) {
        	public PythonImportStat readStat(String path) {
        		return PythonImportStat.MP_IMPORT_STAT_NO_EXIST; 
        	}
        	
        	public String readFile(String filename) {
        		return "";
        	}
        };
        
        try {
            this.ocmod = pystate.newModule("oc");
            this.pystate = pystate;
            
            for (MicroPythonAPI api: this.apis) {
                api.initialize();
            }
            
            // Machine.getResourceAsStream(Settings.scriptPath + "machine.py")
            
            this.pystate.builtins.get("__import__");
            
            String code = this.pystate.readFile("machine.py");
            this.pystate.execute(code);
            
            PythonModule modmain = this.pystate.getMainModule();
            this.kernel = modmain.getattr("kernel");
            
            invoke("initialize");
        } catch (PythonException e) {
            // ?
            return false;
        }
        
        return true;
    }

    PythonModule newOCModule(String name) {
        PythonModule module = pystate.newModule("oc." + name);
        this.ocmod.setattr(name, module);
        
        return module;
    }

    Object invoke(Object ...args) {
        return this.kernel.invoke(args);
    }

    @Override
    public void close() {
        if (this.kernel != null) {
            // TODO: require this?
            try {
                invoke("force_close");
            } catch (PythonException e) {
                // ?
                e.printStackTrace();
            }
            this.kernel = null;
        }
        
        if (this.pystate != null) {
            try {
                this.pystate.close();
            } catch (PythonException e) {
                e.printStackTrace();
            }
            
            this.pystate = null;
        }
    }

    @Override
    public void runSynchronized() {
        invoke("synchronized");
    }
    
    @Override
    public ExecutionResult runThreaded(boolean isSynchronizedReturn) {
        try {
            Object result = invoke("threaded", new Boolean(isSynchronizedReturn));
            if (result instanceof ExecutionResult) {
                return result;
            } else if (result == null) {
                return new ExecutionResult.Error("kernel return null");
            } else {
                return new ExecutionResult.Error("kernel return unknown object: " + result.toString()));
            }
        } catch (PythonException e) {
            return new ExecutionResult.Error(e.toString());
        }
    }

    @Override
    public void onConnect() {
    }

    @Override
    public void load(NBTTagCompound nbt) {
        // ?
        for (MicroPythonAPI api: this.apis) {
            api.load(nbt);
        }
    }

    @Override
    public void save(NBTTagCompound nbt) {
        // ?
        for (MicroPythonAPI api: this.apis) {
            api.save(nbt);
        }
    }
}
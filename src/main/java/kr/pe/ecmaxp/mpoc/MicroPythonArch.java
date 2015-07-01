package kr.pe.ecmaxp.mpoc;

import net.minecraft.item.ItemStack;
import net.minecraft.nbt.NBTTagCompound;
import net.minecraftforge.event.CommandEvent;
import li.cil.oc.api.machine.Architecture;
import li.cil.oc.api.machine.ExecutionResult;
import li.cil.oc.api.machine.Machine;
import li.cil.oc.api.machine.Signal;

// import li.cil.oc.Settings;

import org.micropython.jnupy.PythonState;

import cpw.mods.fml.common.eventhandler.SubscribeEvent;

import org.micropython.jnupy.PythonObject;
import org.micropython.jnupy.PythonModule;

import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;

import javax.swing.JFrame;
import javax.swing.JOptionPane;

import org.micropython.jnupy.PythonArguments;
import org.micropython.jnupy.PythonException;
import org.micropython.jnupy.PythonImportStat;
import org.micropython.jnupy.JavaFunction.*;

@Architecture.Name("MicroPython")
public class MicroPythonArch implements Architecture {
    private ArrayList<MicroPythonAPI> apis;
    @SuppressWarnings("unused")
	private boolean inited;
    
    private PythonModule ocmod;
    private PythonObject kernel;
    
    Machine machine;
    PythonState pystate;
    
    public MicroPythonArch(Machine machine) {
        this.apis = new ArrayList<MicroPythonAPI>();
        this.machine = machine;
        this.inited = false;
        
        this.apis.add(new OSAPI(this));
    }

    public boolean isInitialized() {
        return (inited && this.kernel != null);
    }

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
    
    public boolean initialize() {
        close();
        
        int memorySize = computeMemory();
        PythonState pystate;
		try {
			pystate = new PythonState(memorySize) {
				private File resolvePath(String path) {
					return Paths.get("C:\\Users\\EcmaXp\\Documents\\GitHub\\mpoc\\src\\main\\resources\\assets\\mpoc\\upy\\").resolve(path).toFile();
				}
				
				public PythonImportStat readStat(String path) {
					// we need check '..' but this is dev version.
					File file = resolvePath(path);
					
					try {
						if (!file.exists()) {
							// ...
						} else if (file.isFile() && file.canRead()) {
							return PythonImportStat.MP_IMPORT_STAT_FILE;
						} else if (file.isDirectory()) {
							return PythonImportStat.MP_IMPORT_STAT_DIR;
						}
			 		} catch (SecurityException e) {
						// ...
					}
					
					return PythonImportStat.MP_IMPORT_STAT_NO_EXIST;
				}
				
				public String readFile(String filename) {
					File file = resolvePath(filename);
					byte[] encoded;
					
					try {
						encoded = Files.readAllBytes(file.toPath());
					} catch (IOException e) {
						// TODO: exception...
						throw new RuntimeException("?", e);			
					} catch (SecurityException e) {
						// TODO: exception...
						throw new RuntimeException("?", e);
					}
					
					return new String(encoded, StandardCharsets.UTF_8);
				}
			};

            this.ocmod = pystate.newModule("oc");
            this.pystate = pystate;
            
            for (MicroPythonAPI api: this.apis) {
                api.initialize();
            }
            
            // Machine.getResourceAsStream(Settings.scriptPath + "machine.py")
            // this.pystate.builtins.get("__import__");
            
            String code = this.pystate.readFile("machine.py");
            pystate.execute(code);
            
            PythonModule modmpoc = pystate.newModule("mpoc");
            modmpoc.set(new NamedJavaFun1("ginput") {
    			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
    				Object arg = args.get(0);
    				
    				JFrame frame = new JFrame("<jnupy-input>");
    				try {
    					String s = (String)JOptionPane.showInputDialog(frame, "prompt", "minecraft mpoc inputbox", JOptionPane.PLAIN_MESSAGE);
        				return s;
    				} finally {
    					frame.dispose();
    				}
    			}
            });
            
            PythonModule modmain = this.pystate.getMainModule();
            this.kernel = modmain.getattr("kernel");
            
            invoke("initialize");
            this.inited = true;
        } catch (PythonException e) {
        	// ?
        	e.printStackTrace();
            return false;
        }
        
        return true;
    }

    PythonModule newOCModule(String name) throws PythonException {
        PythonModule module = pystate.newModule("oc." + name);
        this.ocmod.setattr(name, module);
        
        return module;
    }

    Object invoke(Object ...args) throws PythonException {
        return this.kernel.invoke(args);
    }

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
            this.pystate.close();
            this.pystate = null;
        }
    }

    public void runSynchronized() {
        try {
			invoke("synchronized");
		} catch (PythonException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    }
    
    public ExecutionResult runThreaded(boolean isSynchronizedReturn) {
        try {
            Object result = invoke("threaded", new Boolean(isSynchronizedReturn));
            if (result instanceof ExecutionResult) {
                return (ExecutionResult) result;
            } else if (result == null) {
                return new ExecutionResult.Error("kernel return null");
            } else {
                return new ExecutionResult.Error("kernel return unknown object: " + result.toString());
            }
        } catch (PythonException e) {
            return new ExecutionResult.Error(e.toString());
        }
    }

    public void onConnect() {
    }

    public void load(NBTTagCompound nbt) {
        // ?
        for (MicroPythonAPI api: this.apis) {
            api.load(nbt);
        }
    }

    public void save(NBTTagCompound nbt) {
        // ?
        for (MicroPythonAPI api: this.apis) {
            api.save(nbt);
        }
    }
}

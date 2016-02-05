package kr.pe.ecmaxp.mpoc.api;

import org.micropython.jnupy.PythonState;
import org.micropython.jnupy.PythonModule;
import org.micropython.jnupy.PythonArguments;
import org.micropython.jnupy.PythonException;
import org.micropython.jnupy.JavaFunction.*;

import kr.pe.ecmaxp.mpoc.MicroPythonArch;
import net.minecraft.nbt.NBTTagCompound;

public class OSAPI extends MicroPythonAPI {
    public OSAPI(MicroPythonArch owner) {
        super(owner);
    }
    
    public void initialize() throws PythonException {
        PythonModule modos = owner.newOCModule("os");
        
        modos.set(new NamedJavaFun0("clock") {
            @Override
			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
				return machine.cpuTime();
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

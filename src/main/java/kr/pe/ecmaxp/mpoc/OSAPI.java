package kr.pe.ecmaxp.mpoc;

import li.cil.oc.api.machine.Machine;
import li.cil.oc.util.GameTimeFormatter;

import org.micropython.jnupy.PythonState;
import org.micropython.jnupy.PythonModule;
import org.micropython.jnupy.PythonObject;
import org.micropython.jnupy.PythonArguments;
import org.micropython.jnupy.JavaFunction.*;

import net.minecraft.nbt.NBTTagCompound;

public class OSAPI extends MicroPythonAPI {
    public OSAPI(MicroPythonArch owner) {
        super(owner);
    }
    
    public void initialize() {
        PythonState pystate = owner.pystate;
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

package kr.pe.ecmaxp.mpoc;

import li.cil.oc.api.machine.Architecture;
import li.cil.oc.api.machine.ExecutionResult;
import li.cil.oc.api.machine.Machine;
import li.cil.oc.api.machine.Signal;
import net.minecraft.nbt.NBTTagCompound;

@Architecture.Name("MicroPython")
public class MicroPythonArch {
    public MicroPythonArch(Machine machine) {
		this.machine = machine;
	}
	
	@Override
	public boolean isInitialized() {
	    // ?
		return false;
	}

	@Override
	public void recomputeMemory() {
	    // ?
	}

	@Override
	public boolean initialize() {
		// ?
		return false;
	}

	@Override
	public void close() {
		// ?
	}

	@Override
	public void runSynchronized() {
	    // ?	
	}
	
	@Override
	public ExecutionResult runThreaded(boolean isSynchronizedReturn) {
	    // ?
		return new ExecutionResult.Sleep(0);
	}

	@Override
	public void onConnect() {
	    // ?
	}

	@Override
	public void load(NBTTagCompound nbt) {
	    // ?
	}

	@Override
	public void save(NBTTagCompound nbt) {
	    // ?
	}
}
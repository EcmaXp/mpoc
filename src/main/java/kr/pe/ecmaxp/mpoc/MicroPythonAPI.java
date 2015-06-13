package kr.pe.ecmaxp.mpoc;

// TODO: check li.cil.oc.server.machine.ArchitectureAPI

import li.cil.oc.api.machine.Machine;
import net.minecraft.nbt.NBTTagCompound;

public class MicroPythonAPI {
    MicroPythonArch owner;
    Machine machine;

    MicroPythonAPI(MicroPythonArch owner) {
        this.owner = owner;
        this.machine = owner.machine;
    }
    
    // scala version.
    // protected def node = machine.node
    // protected def components = machine.components

    abstract public void initialize();

	public void load(NBTTagCompound nbt) {
        // stub; only override when require loading from nbt;
	}

	public void save(NBTTagCompound nbt) {
        // stub; only override when require loading from nbt;
	}
}

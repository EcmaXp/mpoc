// TODO: check li.cil.oc.server.machine.ArchitectureAPI

import li.cil.oc.api.machine.Machine;

public class MicroPythonAPI {
    // ?
    MicroPythonArch owner;
    Machine machine;
    
    MicroPythonAPI(MicroPythonArch owner) {
        owner = owner;
        machine = owner.getMachine();
    }
}

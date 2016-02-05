package kr.pe.ecmaxp.mpoc.api;

import org.micropython.jnupy.PythonState;
import org.micropython.jnupy.PythonModule;
import org.micropython.jnupy.PythonObject;
import org.micropython.jnupy.PythonArguments;
import org.micropython.jnupy.PythonException;

import java.util.Map;

import org.micropython.jnupy.JavaFunction.*;

import kr.pe.ecmaxp.mpoc.MicroPythonArch;
import net.minecraft.nbt.NBTTagCompound;

public class ComponentAPI extends MicroPythonAPI {
    public ComponentAPI(MicroPythonArch owner) {
        super(owner);
    }
    
    public void initialize() throws PythonException {
        PythonModule module = owner.newOCModule("component");
        
        module.set(new NamedJavaFun0("getList") {
            @Override
			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
            	Map<String, String> components = owner.getMachine().components();
            	PythonObject result = pythonState.getBuiltin("dict").rawCall();
            	PythonObject set = result.attr("__setitem__");

            	synchronized (components) {
                	for (Map.Entry<String, String> entry : components.entrySet()) {
                		set.invoke(entry.getKey(), entry.getValue());
                	}			
				}
            	
        		return result;
			}
        });
        
        module.set(new NamedJavaFun1("getType") {
            @Override
			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
            	Map<String, String> components = owner.getMachine().components();
            	String address = (String)args.get(0);
            	
            	synchronized (components) {
                	return components.get(address);
				}
			}
        });
        
        module.set(new NamedJavaFun1("getSlot") {
            @Override
			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
            	Map<String, String> components = owner.getMachine().components();
            	String address = (String)args.get(0);
            	
            	synchronized (components) {
                	if (components.containsKey(address)) {
                		return new Integer(owner.getMachine().host().componentSlot(address));
                	}
				}
            	
				return null;
			}
        });
        
        /*
        module.set(new NamedJavaFun1("getMethods") {
            @Override
			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
            	Map<String, String> components = owner.machine.components();
            	String address = (String)args.get(0);
            	
            	synchronized (components) {
                	return components.get(address);
				}
			}
        });
        */
        
        module.set(new NamedJavaFun3("invoke") {
            @Override
			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
            	String address = (String)args.get(0);
            	String method = (String)args.get(1);
            	Object[] fargs = (Object[])args.get(2);
            	
            	try {
					return owner.getMachine().invoke(address, method, fargs);
				} catch (Exception e) {
					// how to raise error?
					
					e.printStackTrace();
					return e; // well, currently just given error object;
				}
			}
        });

        module.set(new NamedJavaFun1("isException") {
            @Override
			public Object invoke(PythonState pythonState, PythonArguments args) throws PythonException {
            	Object object = args.get(0);
            	return new Boolean(object instanceof Exception);
			}
        });
        
    /* private boolean withComponent(String address) {
    	Object node = owner.machine.node().network().node(address);
    	if (node instanceof Component) {
    		Component component = (Component)component;
    		return component.canBeSeenFrom(arg0)
    	} else {
    		return false;
    	}
       */
    }

    
    @Override
	public void load(NBTTagCompound nbt) {

	}

    @Override
	public void save(NBTTagCompound nbt) {

	}
}

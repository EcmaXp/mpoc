package kr.pe.ecmaxp.fakempoc;

import cpw.mods.fml.common.Mod;
import cpw.mods.fml.common.Mod.EventHandler;
import cpw.mods.fml.common.Mod.Instance;
import cpw.mods.fml.common.event.FMLInitializationEvent;
import cpw.mods.fml.common.event.FMLServerStartingEvent;

@Mod(modid = FakeMPOC.MODID, name = FakeMPOC.MODNAME,
    version = FakeMPOC.VERSION, useMetadata = true)
public class FakeMPOC
{
    public static final String MODID = "fakempoc";
    public static final String MODNAME = "fakempoc";
    public static final String VERSION = "0.1";

	@Instance(MODID)
    public static FakeMPOC INSTANCE;	
    
	@EventHandler
    public void init(FMLInitializationEvent event)
    {
        li.cil.oc.api.Machine.add(JythonArch.class);
        li.cil.oc.api.Items.registerEEPROM("Jython BIOS", "".getBytes(), "".getBytes(), false);
    }
	
    @EventHandler
    public void serverLoad(FMLServerStartingEvent event) {
    	event.registerServerCommand(new FakeMPOCCommand());
    }
}

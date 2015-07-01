package kr.pe.ecmaxp.mpoc;

import cpw.mods.fml.common.Mod;
import cpw.mods.fml.common.Mod.EventHandler;
import cpw.mods.fml.common.event.FMLInitializationEvent;

@Mod(modid = MPOC.MODID, name = MPOC.MODNAME,
    version = MPOC.VERSION, useMetadata = true)
public class MPOC
{
    public static final String MODID = "mpoc";
    public static final String MODNAME = "mpoc";
    public static final String VERSION = "0.1";
    
	@EventHandler
    public void init(FMLInitializationEvent event)
    {
        li.cil.oc.api.Machine.add(MicroPythonArch.class);
    }
}

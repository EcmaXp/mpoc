package kr.pe.ecmaxp.mpoc.virtual;

import li.cil.repack.com.naef.jnlua.NativeSupport;
import li.cil.repack.com.naef.jnlua.NativeSupport.Loader;
import li.cil.repack.com.naef.jnlua.LuaState;

public class JNLuaPreloader {
    public static LuaState state;

    private class NativeLoader implements Loader {
        @Override
        public void load() {
            System.load(System.getenv("OPENCOM_NATIVE_LIB"));
        }
    }
	
   public boolean init() {
        NativeSupport.getInstance().setLoader(new NativeLoader());
        
        // it will raise error if library are not ready.
        new LuaState().close();
        
        return true;
    }
}
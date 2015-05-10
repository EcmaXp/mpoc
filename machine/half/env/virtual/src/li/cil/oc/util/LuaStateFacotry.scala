package li.cil.oc.util

import java.io.File
import java.io.FileInputStream
import java.io.FileOutputStream
import java.nio.channels.Channels

import com.google.common.base.Strings
import li.cil.oc.OpenComputers
import li.cil.oc.Settings
import li.cil.oc.server.machine.Machine
import li.cil.oc.util.ExtendedLuaState._
import li.cil.repack.com.naef.jnlua
import li.cil.repack.com.naef.jnlua.LuaState
import li.cil.repack.com.naef.jnlua.NativeSupport.Loader
import org.apache.commons.lang3.SystemUtils

import scala.util.Random

/**
 * Factory singleton used to spawn new LuaState instances.
 *
 * This is realized as a singleton so that we only have to resolve shared
 * library references once during initialization and can then re-use the
 * already loaded ones.
 */
object LuaStateFactory {
  // ----------------------------------------------------------------------- //
  // Initialization
  // ----------------------------------------------------------------------- //

  /** Set to true in initialization code below if available. */
  private var haveNativeLibrary = true

  def isAvailable = haveNativeLibrary

  val is64Bit = true

  def init() {
    return
  }

  init()

  // ----------------------------------------------------------------------- //
  // Factory
  // ----------------------------------------------------------------------- //

  def createState(): Option[LuaState] = {
    if (!haveNativeLibrary) return None

    
      val state = new jnlua.LuaState(Int.MaxValue)
        // Load all libraries.
        state.openLib(jnlua.LuaState.Library.BASE)
        state.openLib(jnlua.LuaState.Library.BIT32)
        state.openLib(jnlua.LuaState.Library.COROUTINE)
        state.openLib(jnlua.LuaState.Library.DEBUG)
        state.openLib(jnlua.LuaState.Library.ERIS)
        state.openLib(jnlua.LuaState.Library.MATH)
        state.openLib(jnlua.LuaState.Library.STRING)
        state.openLib(jnlua.LuaState.Library.TABLE)
        state.pop(8)

        if (true) { // !Settings.get.disableLocaleChanging
          state.openLib(jnlua.LuaState.Library.OS)
          state.getField(-1, "setlocale")
          state.pushString("C")
          state.call(1, 0)
          state.pop(1)
        }

        // Prepare table for os stuff.
        state.newTable()
        state.setGlobal("os")

        // Kill compat entries.
        state.pushNil()
        state.setGlobal("unpack")
        state.pushNil()
        state.setGlobal("loadstring")
        state.getGlobal("math")
        state.pushNil()
        state.setField(-2, "log10")
        state.pop(1)
        state.getGlobal("table")
        state.pushNil()
        state.setField(-2, "maxn")
        state.pop(1)

        // Remove some other functions we don't need and are dangerous.
        state.pushNil()
        state.setGlobal("dofile")
        state.pushNil()
        state.setGlobal("loadfile")

        state.getGlobal("math")

        // We give each Lua state it's own randomizer, since otherwise they'd
        // use the good old rand() from C. Which can be terrible, and isn't
        // necessarily thread-safe.
        val random = new Random
        state.pushScalaFunction(lua => {
          val r = random.nextDouble()
          lua.getTop match {
            case 0 => lua.pushNumber(r)
            case 1 =>
              val u = lua.checkNumber(1)
              lua.checkArg(1, 1 <= u, "interval is empty")
              lua.pushNumber(math.floor(r * u) + 1)
            case 2 =>
              val l = lua.checkNumber(1)
              val u = lua.checkNumber(2)
              lua.checkArg(2, l <= u, "interval is empty")
              lua.pushNumber(math.floor(r * (u - l + 1)) + l)
            case _ => throw new IllegalArgumentException("wrong number of arguments")
          }
          1
        })
        state.setField(-2, "random")

        state.pushScalaFunction(lua => {
          random.setSeed(lua.checkNumber(1).toLong)
          0
        })
        state.setField(-2, "randomseed")

        // Pop the math table.
        state.pop(1)

        return Some(state)
  }
}
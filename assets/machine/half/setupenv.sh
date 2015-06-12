#!/bin/bash

export PROJECT_HOME="$HOME/workspace/assets"

export LAUNCHER_HOME="$PROJECT_HOME/machine/half" # "$( dirname ${BASH_SOURCE[0]})"
export LAUNCHER_ENV="$LAUNCHER_HOME/env"

export VIRTUAL_HOME="$LAUNCHER_HOME/virtual"
export VIRTUAL_SRC="$VIRTUAL_HOME/src"
export VIRTUAL_SRC_BUILD="$VIRTUAL_HOME/src_build"
export VIRTUAL_BUILD="$VIRTUAL_HOME/build"
export VIRTUAL_MANIFEST="$VIRTUAL_HOME/manifest"
export VIRTUAL_JAR="$VIRTUAL_HOME/virtual.jar"

export JYTHON_HOME="$LAUNCHER_ENV/jython2.7"
export JAVA_HOME="$LAUNCHER_ENV/jdk1.8.0_45"
export SCALA_HOME="$LAUNCHER_ENV/scala-2.11.6"

export FORGE_HOME="$LAUNCHER_ENV/forge-1.7.10"
export FORGE_LIB="$FORGE_HOME/libraries"
export FORGE_JAR="$FORGE_HOME/forge-1.7.10-10.13.3.1403-1.7.10-universal.jar"
export MC_SERVER_JAR="$FORGE_HOME/minecraft_server.1.7.10.jar"

export OPENCOM_HOME="$LAUNCHER_ENV/opencom"
export OPENCOM_JAR="$OPENCOM_HOME/OpenComputers-MC1.7.10-1.5.9.21-universal.jar"
export OPENCOM_JNLUA_JAR="$OPENCOM_HOME/OpenComputers-JNLua.jar"
export OPENCOM_LUAJ_JAR="$OPENCOM_HOME/OpenComputers-LuaJ.jar"
export OPENCOM_NATIVE_LIB="$OPENCOM_HOME/lib/native.64.so"

export MSGPACK_HOME="$LAUNCHER_ENV/msgpack-java"
export MSGPACK_JAR="$MSGPACK_HOME/msgpack-0.6.12.jar"

export MICROPYTHON_HOME="$PROJECT_HOME/micropython"
export MICROPYTHON_PORT="opencom"
export MICROPYTHON_PORT_HOME="$MICROPYTHON_HOME/$MICROPYTHON_PORT"
export MICROPYTHON_PORT_EXE_NAME="micropython"
export MICROPYTHON_PORT_EXE="$MICROPYTHON_PORT_HOME/$MICROPYTHON_PORT_EXE_NAME"
export MICROPYTHON_PORT_LIB_NAME="libmicropython.so"
export MICROPYTHON_PORT_LIB="$MICROPYTHON_PORT_HOME/$MICROPYTHON_PORT_LIB_NAME"
export MICROPYTHON_BATTERY="$MICROPYTHON_PORT_HOME/lib"
export MICROPYTHON_LIB="$LAUNCHER_HOME/$MICROPYTHON_PORT_LIB_NAME"
export MICROPYTHON_JAR="$MICROPYTHON_PORT_HOME/micropython.jar"

export MPOC_ROM="$PROJECT_HOME/machine/rom"

export JAVACMD=$JAVA_HOME/bin/java
export JAVA_MEM="-Xmx128m -Xms32m"
export JAVA_OPTS='-Dscala.home="$SCALA_HOME" -Djava.library.path=$PROJECT_HOME'

export MPOC_LAUNCH="$JAVACMD org.micropython.jnupy.PythonState"

export CLASSPATH="$VIRTUAL_JAR"

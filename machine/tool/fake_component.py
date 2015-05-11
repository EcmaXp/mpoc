
# Robot.scala
class Robot:
    @Callback()
    def getLightColor() -> int:
        "Get the current color of the activity light as an integer encoded RGB value (0xRRGGBB)."
        pass

    @Callback()
    def setLightColor(value:int) -> int:
        "Set the color of the activity light to the specified integer encoded RGB value (0xRRGGBB)."
        pass

    @Callback()
    def durability() -> int:
        "Get the durability of the currently equipped tool."
        pass

    @Callback()
    def move(direction:int) -> bool:
        "Move in the specified direction."
        pass

    @Callback()
    def turn(clockwise:bool) -> bool:
        "Rotate in the specified direction."
        pass


# Drone.scala
class Drone:
    @Callback()
    def getStatusText() -> str:
        "Get the status text currently being displayed in the GUI."
        pass

    @Callback()
    def setStatusText(value:str) -> str:
        "Set the status text to display in the GUI, returns new value."
        pass

    @Callback()
    def getLightColor() -> int:
        "Get the current color of the flap lights as an integer encoded RGB value (0xRRGGBB)."
        pass

    @Callback()
    def setLightColor(value:int) -> int:
        "Set the color of the flap lights to the specified integer encoded RGB value (0xRRGGBB)."
        pass

    @Callback()
    def move(dx:int, dy:int, dz:int):
        "Change the target position by the specified offset."
        pass

    @Callback()
    def getOffset() -> int:
        "Get the current distance to the target position."
        pass

    @Callback()
    def getVelocity() -> int:
        "Get the current velocity in m/s."
        pass

    @Callback()
    def getMaxVelocity() -> int:
        "Get the maximum velocity, in m/s."
        pass

    @Callback()
    def getAcceleration() -> int:
        "Get the currently set acceleration."
        pass

    @Callback()
    def setAcceleration(value:int) -> int:
        "Try to set the acceleration to the specified value and return the new acceleration."
        pass


# UpgradeCrafting.scala
class UpgradeCrafting:
    @Callback()
    def craft(count=0:int) -> int:
        "Tries to craft the specified number of items in the top left area of the inventory."
        pass


# NetworkCard.scala
class NetworkCard:
    @Callback()
    def open(port:int) -> bool:
        "Opens the specified port. Returns true if the port was opened."
        pass

    @Callback()
    def close(port=0:int) -> bool:
        "Closes the specified port (default: all ports). Returns true if ports were closed."
        pass

    @Callback(direct = true)
    def isOpen(port:int) -> bool:
        "Whether the specified port is open."
        pass

    @Callback(direct = true)
    def isWireless() -> bool:
        "Whether this is a wireless network card."
        pass

    @Callback()
    def send(address:str, port:int, data...):
        "Sends the specified data to the specified target."
        pass

    @Callback()
    def broadcast(port:int, data...):
        "Broadcasts the specified data on the specified port."
        pass

    @Callback(direct = true)
    def maxPacketSize() -> int:
        "Gets the maximum packet size (config setting)."
        pass

    @Callback(direct = true)
    def getWakeMessage() -> str:
        "Get the current wake-up message."
        pass

    @Callback()
    def setWakeMessage(message:str) -> str:
        "Set the wake-up message."
        pass


# GraphicsCard.scala
class GraphicsCard:
    @Callback()
    def bind(address:str) -> bool:
        "Binds the GPU to the screen with the specified address."
        pass

    @Callback(direct = true)
    def getScreen() -> str:
        "Get the address of the screen the GPU is currently bound to."
        pass

    @Callback(direct = true)
    def getBackground() -> (int, bool):
        """Get the current background color and whether it's from the palette or not."""
        pass

    @Callback(direct = true)
    def getForeground() -> (int, bool):
        """Get the current foreground color and whether it's from the palette or not."""
        pass

    @Callback(direct = true)
    def getPaletteColor(index:int) -> int:
        "Get the palette color at the specified palette index."
        pass

    @Callback(direct = true)
    def getDepth() -> int:
        "Returns the currently set color depth."
        pass

    @Callback()
    def setDepth(depth:int) -> int:
        "Set the color depth. Returns the previous value."
        pass

    @Callback(direct = true)
    def maxDepth() -> int:
        "Get the maximum supported color depth."
        pass

    @Callback(direct = true)
    def getResolution() -> (int, int):
        "Get the current screen resolution."
        pass

    @Callback()
    def setResolution(width:int, height:int) -> bool:
        "Set the screen resolution. Returns true if the resolution changed."
        pass

    @Callback(direct = true)
    def maxResolution() -> (int, int):
        "Get the maximum screen resolution."
        pass

    @Callback(direct = true)
    def get(x:int, y:int) -> (str, int, int, int or None, int or None):
        "Get the value displayed on the screen at the specified index, as well as the foreground and background color. If the foreground or background is from the palette, returns the palette indices as fourth and fifth results, else nil, respectively."
        pass

    @Callback(direct = true, limit = 16)
    @Override
    def copy(x:int, y:int, width:int, height:int, tx:int, ty:int) = super.copy(context, args)) -> bool:
        "Copies a portion of the screen from the specified location with the specified size by the specified translation."
        pass

    @Callback(direct = true, limit = 32)
    @Override
    def fill(x:int, y:int, width:int, height:int, char:str) = super.fill(context, args)) -> bool:
        "Fills a portion of the screen at the specified position with the specified size with the specified character."
        pass

    @Callback(direct = true, limit = 64)
    @Override
    def set(x:int, y:int, value:str, vertical=None:bool) = super.set(context, args)) -> bool:
        "Plots a string value to the screen at the specified position. Optionally writes the string vertically."
        pass

    @Callback(direct = true, limit = 32)
    @Override
    def setBackground(value:int, palette=None:bool) = super.setBackground(context, args)) -> (int, int or None):
        "Sets the background color to the specified value. Optionally takes an explicit palette index. Returns the old value and if it was from the palette its palette index."
        pass

    @Callback(direct = true, limit = 32)
    @Override
    def setForeground(value:int, palette=None:bool) = super.setForeground(context, args)) -> (int, int or None):
        "Sets the foreground color to the specified value. Optionally takes an explicit palette index. Returns the old value and if it was from the palette its palette index."
        pass

    @Callback(direct = true, limit = 2)
    @Override
    def setPaletteColor(index:int, color:int) -> int:
        "Set the palette color at the specified palette index. Returns the previous value."
        pass

    @Callback(direct = true, limit = 32)
    @Override
    def copy(x:int, y:int, width:int, height:int, tx:int, ty:int) = super.copy(context, args)) -> bool:
        "Copies a portion of the screen from the specified location with the specified size by the specified translation."
        pass

    @Callback(direct = true, limit = 64)
    @Override
    def fill(x:int, y:int, width:int, height:int, char:str) = super.fill(context, args)) -> bool:
        "Fills a portion of the screen at the specified position with the specified size with the specified character."
        pass

    @Callback(direct = true, limit = 128)
    @Override
    def set(x:int, y:int, value:str, vertical=None:bool) = super.set(context, args)) -> bool:
        "Plots a string value to the screen at the specified position. Optionally writes the string vertically."
        pass

    @Callback(direct = true, limit = 64)
    @Override
    def setBackground(value:int, palette=None:bool) = super.setBackground(context, args)) -> (int, int or None):
        "Sets the background color to the specified value. Optionally takes an explicit palette index. Returns the old value and if it was from the palette its palette index."
        pass

    @Callback(direct = true, limit = 64)
    @Override
    def setForeground(value:int, palette=None:bool) = super.setForeground(context, args)) -> (int, int or None):
        "Sets the foreground color to the specified value. Optionally takes an explicit palette index. Returns the old value and if it was from the palette its palette index."
        pass

    @Callback(direct = true, limit = 8)
    @Override
    def setPaletteColor(index:int, color:int) -> int:
        "Set the palette color at the specified palette index. Returns the previous value."
        pass

    @Callback(direct = true, limit = 64)
    @Override
    def copy(x:int, y:int, width:int, height:int, tx:int, ty:int) = super.copy(context, args)) -> bool:
        "Copies a portion of the screen from the specified location with the specified size by the specified translation."
        pass

    @Callback(direct = true, limit = 128)
    @Override
    def fill(x:int, y:int, width:int, height:int, char:str) = super.fill(context, args)) -> bool:
        "Fills a portion of the screen at the specified position with the specified size with the specified character."
        pass

    @Callback(direct = true, limit = 256)
    @Override
    def set(x:int, y:int, value:str, vertical=None:bool) = super.set(context, args)) -> bool:
        "Plots a string value to the screen at the specified position. Optionally writes the string vertically."
        pass

    @Callback(direct = true, limit = 128)
    @Override
    def setBackground(value:int, palette=None:bool) = super.setBackground(context, args)) -> (int, int or None):
        "Sets the background color to the specified value. Optionally takes an explicit palette index. Returns the old value and if it was from the palette its palette index."
        pass

    @Callback(direct = true, limit = 128)
    @Override
    def setForeground(value:int, palette=None:bool) = super.setForeground(context, args)) -> (int, int or None):
        "Sets the foreground color to the specified value. Optionally takes an explicit palette index. Returns the old value and if it was from the palette its palette index."
        pass

    @Callback(direct = true, limit = 16)
    @Override
    def setPaletteColor(index:int, color:int) -> int:
        "Set the palette color at the specified palette index. Returns the previous value."
        pass



# Agent.scala
class Agent:
    @Callback()
    def name() -> str:
        "Get the name of the agent."
        pass

    @Callback
    def swing():
        pass

    @Callback
    def use():
        pass

    @Callback
    def place():
        pass


# FileSystem.scala
class FileSystem:
    @Callback(direct = true)
    def getLabel() -> str:
        "Get the current label of the file system."
        pass

    @Callback()
    def setLabel(value:str) -> str:
        "Sets the label of the file system. Returns the new value, which may be truncated."
        pass

    @Callback(direct = true)
    def isReadOnly() -> bool:
        "Returns whether the file system is read-only."
        pass

    @Callback(direct = true)
    def spaceTotal() -> int:
        "The overall capacity of the file system, in bytes."
        pass

    @Callback(direct = true)
    def spaceUsed() -> int:
        "The currently used capacity of the file system, in bytes."
        pass

    @Callback(direct = true)
    def exists(path:str) -> bool:
        "Returns whether an object exists at the specified absolute path in the file system."
        pass

    @Callback(direct = true)
    def size(path:str) -> int:
        "Returns the size of the object at the specified absolute path in the file system."
        pass

    @Callback(direct = true)
    def isDirectory(path:str) -> bool:
        "Returns whether the object at the specified absolute path in the file system is a directory."
        pass

    @Callback(direct = true)
    def lastModified(path:str) -> int:
        "Returns the (real world) timestamp of when the object at the specified absolute path in the file system was modified."
        pass

    @Callback()
    def list(path:str) -> table:
        "Returns a list of names of objects in the directory at the specified absolute path in the file system."
        pass

    @Callback()
    def makeDirectory(path:str) -> bool:
        "Creates a directory at the specified absolute path in the file system. Creates parent directories, if necessary."
        pass

    @Callback()
    def remove(path:str) -> bool:
        "Removes the object at the specified absolute path in the file system."
        pass

    @Callback()
    def rename(from:str, to:str) -> bool:
        "Renames/moves an object from the first specified absolute path in the file system to the second."
        pass

    @Callback(direct = true)
    def close(handle:int):
        "Closes an open file descriptor with the specified handle."
        pass

    @Callback(direct = true, limit = 4)
    def open(path:str, mode=str='r'():str='r') -> int:
        "Opens a new file descriptor and returns its handle."
        pass

    @Callback(direct = true, limit = 15)
    @Override
    def read(handle:int, count:int) -> str or None:
        "Reads up to the specified amount of data from an open file descriptor with the specified handle. Returns nil when EOF is reached."
        pass

    @Callback(direct = true, limit = 15)
    @Override
    def seek(handle:int, whence:str, offset:int) -> int:
        "Seeks in an open file descriptor with the specified handle. Returns the new pointer position."
        pass

    @Callback(direct = true, limit = 6)
    @Override
    def write(handle:int, value:str) -> bool:
        "Writes the specified data to an open file descriptor with the specified handle."
        pass

    @Callback(direct = true, limit = 13)
    @Override
    def read(handle:int, count:int) -> str or None:
        "Reads up to the specified amount of data from an open file descriptor with the specified handle. Returns nil when EOF is reached."
        pass

    @Callback(direct = true, limit = 13)
    @Override
    def seek(handle:int, whence:str, offset:int) -> int:
        "Seeks in an open file descriptor with the specified handle. Returns the new pointer position."
        pass

    @Callback(direct = true, limit = 5)
    @Override
    def write(handle:int, value:str) -> bool:
        "Writes the specified data to an open file descriptor with the specified handle."
        pass

    @Callback(direct = true, limit = 10)
    @Override
    def read(handle:int, count:int) -> str or None:
        "Reads up to the specified amount of data from an open file descriptor with the specified handle. Returns nil when EOF is reached."
        pass

    @Callback(direct = true, limit = 10)
    @Override
    def seek(handle:int, whence:str, offset:int) -> int:
        "Seeks in an open file descriptor with the specified handle. Returns the new pointer position."
        pass

    @Callback(direct = true, limit = 4)
    @Override
    def write(handle:int, value:str) -> bool:
        "Writes the specified data to an open file descriptor with the specified handle."
        pass

    @Callback(direct = true, limit = 7)
    @Override
    def read(handle:int, count:int) -> str or None:
        "Reads up to the specified amount of data from an open file descriptor with the specified handle. Returns nil when EOF is reached."
        pass

    @Callback(direct = true, limit = 7)
    @Override
    def seek(handle:int, whence:str, offset:int) -> int:
        "Seeks in an open file descriptor with the specified handle. Returns the new pointer position."
        pass

    @Callback(direct = true, limit = 3)
    @Override
    def write(handle:int, value:str) -> bool:
        "Writes the specified data to an open file descriptor with the specified handle."
        pass

    @Callback(direct = true, limit = 4)
    @Override
    def read(handle:int, count:int) -> str or None:
        "Reads up to the specified amount of data from an open file descriptor with the specified handle. Returns nil when EOF is reached."
        pass

    @Callback(direct = true, limit = 4)
    @Override
    def seek(handle:int, whence:str, offset:int) -> int:
        "Seeks in an open file descriptor with the specified handle. Returns the new pointer position."
        pass

    @Callback(direct = true, limit = 2)
    @Override
    def write(handle:int, value:str) -> bool:
        "Writes the specified data to an open file descriptor with the specified handle."
        pass

    @Callback(direct = true, limit = 1)
    @Override
    def read(handle:int, count:int) -> str or None:
        "Reads up to the specified amount of data from an open file descriptor with the specified handle. Returns nil when EOF is reached."
        pass

    @Callback(direct = true, limit = 1)
    @Override
    def seek(handle:int, whence:str, offset:int) -> int:
        "Seeks in an open file descriptor with the specified handle. Returns the new pointer position."
        pass

    @Callback(direct = true, limit = 1)
    @Override
    def write(handle:int, value:str) -> bool:
        "Writes the specified data to an open file descriptor with the specified handle."
        pass


# EEPROM.scala
class EEPROM:
    @Callback(direct = true)
    def get() -> str:
        "Get the currently stored byte array."
        pass

    @Callback()
    def set(data:str):
        "Overwrite the currently stored byte array."
        pass

    @Callback(direct = true)
    def getLabel() -> str:
        "Get the label of the EEPROM."
        pass

    @Callback()
    def setLabel(data:str) -> str:
        "Set the label of the EEPROM."
        pass

    @Callback(direct = true)
    def getSize() -> str:
        "Get the storage capacity of this EEPROM."
        pass

    @Callback(direct = true)
    def getChecksum() -> str:
        "Get the checksum of the data on this EEPROM."
        pass

    @Callback(direct = true)
    def makeReadonly(checksum:str) -> bool:
        """Make this EEPROM readonly if it isn't already. This process cannot be reversed!"""
        pass

    @Callback(direct = true)
    def getDataSize() -> str:
        "Get the storage capacity of this EEPROM."
        pass

    @Callback(direct = true)
    def getData() -> str:
        "Get the currently stored byte array."
        pass

    @Callback()
    def setData(data:str):
        "Overwrite the currently stored byte array."
        pass


# UpgradeLeash.scala
class UpgradeLeash:
    @Callback()
    def leash(side:int) -> bool:
        "Tries to put an entity on the specified side of the device onto a leash."
        pass

    @Callback()
    def unleash():
        "Unleashes all currently leashed entities."
        pass


# RedstoneVanilla.scala
class RedstoneVanilla:
    @Callback(direct = true)
    def getInput(side:int) -> int:
        "Get the redstone input on the specified side."
        pass

    @Callback(direct = true)
    def getOutput(side:int) -> int:
        "Get the redstone output on the specified side."
        pass

    @Callback()
    def setOutput(side:int, value:int) -> int:
        "Set the redstone output on the specified side."
        pass


# RedstoneBundled.scala
class RedstoneBundled:
    @Callback(direct = true)
    def getBundledInput(side:int, color=0:int) -> int or table:
        "Get the bundled redstone input on the specified side and with the specified color."
        pass

    @Callback(direct = true)
    def getBundledOutput(side:int, color=0:int) -> int or table:
        "Get the bundled redstone output on the specified side and with the specified color."
        pass

    @Callback()
    def setBundledOutput(side:int, color:int, value:int) -> int:
        "Set the bundled redstone output on the specified side and with the specified color."
        pass


# WirelessNetworkCard.scala
class WirelessNetworkCard:
    @Callback(direct = true)
    def getStrength() -> int:
        "Get the signal strength (range) used when sending messages."
        pass

    @Callback()
    def setStrength(strength:int) -> int:
        "Set the signal strength (range) used when sending messages."
        pass


# UpgradeChunkloader.scala
class UpgradeChunkloader:
    @Callback()
    def isActive() -> bool:
        "Gets whether the chunkloader is currently active."
        pass

    @Callback()
    def setActive(enabled:bool) -> bool:
        "Enables or disables the chunkloader."
        pass


# UpgradePiston.scala
class UpgradePiston:
    @Callback()
    def push() -> bool:
        "Tries to push the block in front of the container of the upgrade."
        pass


# InternetCard.scala
class InternetCard:
    @Callback(direct = true)
    def isHttpEnabled() -> bool:
        "Returns whether HTTP requests can be made (config setting)."
        pass

    @Callback()
    def request(url:str, postData='':str) -> userdata:
        "Starts an HTTP request. If this returns true, further results will be pushed using `http_response` signals."
        pass

    @Callback(direct = true)
    def isTcpEnabled() -> bool:
        "Returns whether TCP connections can be made (config setting)."
        pass

    @Callback()
    def connect(address:str, port=0:int) -> userdata:
        "Opens a new TCP connection. Returns the handle of the connection."
        pass

    @Callback()
    def finishConnect() -> bool:
        "Ensures a socket is connected. Errors if the connection failed."
        pass

    @Callback()
    def read(n=0:int) -> str:
        "Tries to read data from the socket stream. Returns the read byte array."
        pass

    @Callback()
    def write(data:str) -> int:
        "Tries to write data to the socket stream. Returns the number of bytes written."
        pass

    @Callback(direct = true)
    def close():
        "Closes an open socket stream."
        pass

    @Callback()
    def finishConnect() -> bool:
        "Ensures a response is available. Errors if the connection failed."
        pass

    @Callback(direct = true)
    def response() -> (int, str, table):
        "Get response code, message and headers."
        pass

    @Callback()
    def read(n=0:int) -> str:
        "Tries to read data from the response. Returns the read byte array."
        pass

    @Callback(direct = true)
    def close():
        "Closes an open socket stream."
        pass


# UpgradeDatabase.scala
class UpgradeDatabase:
    @Callback()
    def get(slot:int) -> table:
        "Get the representation of the item stack stored in the specified slot."
        pass

    @Callback()
    def computeHash(slot:int) -> str:
        "Computes a hash value for the item stack in the specified slot."
        pass

    @Callback()
    def indexOf(hash:str) -> int:
        "Get the index of an item stack with the specified hash. Returns a negative value if no such stack was found."
        pass

    @Callback()
    def clear(slot:int) -> bool:
        "Clears the specified slot. Returns true if there was something in the slot before."
        pass

    @Callback()
    def copy(fromSlot:int, toSlot:int, address='':str) -> bool:
        "Copies an entry to another slot, optionally to another database. Returns true if something was overwritten."
        pass

    @Callback()
    def clone(address:str) -> int:
        "Copies the data stored in this database to another database with the specified address."
        pass


# Geolyzer.scala
class Geolyzer:
    @Callback()
    def scan(computer: Context, args: Arguments):
        "function(x:number, z:number[, ignoreReplaceable:boolean|options:table]):table"
        "Analyzes the density of the column at the specified relative coordinates."
        pass

    @Callback()
    def analyze(computer: Context, args: Arguments):
        "function(side:number[,options:table]):table"
        "Get some information on a directly adjacent block."
        pass

    @Callback()
    def store(computer: Context, args: Arguments):
        "function(side:number, dbAddress:string, dbSlot:number):boolean"
        "Store an item stack representation of the block on the specified side in a database component."
        pass


# RedstoneWireless.scala
class RedstoneWireless:
    @Callback()
    def getWirelessInput() -> int:
        "Get the wireless redstone input."
        pass

    @Callback(direct = true)
    def getWirelessOutput() -> bool:
        "Get the wireless redstone output."
        pass

    @Callback()
    def setWirelessOutput(value:bool) -> bool:
        "Set the wireless redstone output."
        pass

    @Callback(direct = true)
    def getWirelessFrequency() -> int:
        "Get the currently set wireless redstone frequency."
        pass

    @Callback()
    def setWirelessFrequency(frequency:int) -> int:
        "Set the wireless redstone frequency to use."
        pass


# UpgradeInventoryController.scala
class UpgradeInventoryController:
    @Callback()
    def equip() -> bool:
        "Swaps the equipped tool with the content of the currently selected inventory slot."
        pass


# UpgradeTractorBeam.scala
class UpgradeTractorBeam:
    @Callback()
    def suck() -> bool:
        """Tries to pick up a random item in the robots' vicinity."""
        pass


# UpgradeSignInRotatable.scala
class UpgradeSignInRotatable:
    @Callback()
    def getValue() -> str:
        "Get the text on the sign in front of the host."
        pass

    @Callback()
    def setValue(value:str) -> str:
        "Set the text on the sign in front of the host."
        pass


# RedstoneSignaller.scala
class RedstoneSignaller:
    @Callback(direct = true)
    def getWakeThreshold() -> int:
        "Get the current wake-up threshold."
        pass

    @Callback()
    def setWakeThreshold(threshold:int) -> int:
        "Set the wake-up threshold."
        pass


# LinkedCard.scala
class LinkedCard:
    @Callback()
    def send(data...):
        "Sends the specified data to the card this one is linked to."
        pass

    @Callback(direct = true)
    def maxPacketSize() -> int:
        "Gets the maximum packet size (config setting)."
        pass


# UpgradeNavigation.scala
class UpgradeNavigation:
    @Callback()
    def getPosition() -> (int, int, int):
        "Get the current relative position of the robot."
        pass

    @Callback()
    def getFacing() -> int:
        "Get the current orientation of the robot."
        pass

    @Callback()
    def getRange() -> int:
        "Get the operational range of the navigation upgrade."
        pass

    @Callback()
    def findWaypoints(range:int) -> table:
        "Find waypoints in the specified range."
        pass


# UpgradeGenerator.scala
class UpgradeGenerator:
    @Callback()
    def insert(count=0:int) -> bool:
        """Tries to insert fuel from the selected slot into the generator's queue."""
        pass

    @Callback()
    def count() -> int:
        """Get the size of the item stack in the generator's queue."""
        pass

    @Callback()
    def remove(count=0:int) -> bool:
        """Tries to remove items from the generator's queue."""
        pass


# UpgradeExperience.scala
class UpgradeExperience:
    @Callback(direct = true)
    def level() -> int:
        "The current level of experience stored in this experience upgrade."
        pass

    @Callback()
    def consume() -> bool:
        "Tries to consume an enchanted item to add experience to the upgrade."
        pass


# DebugCard.scala
class DebugCard:
    @Callback()
    def changeBuffer(value:int) -> int:
        """Changes the component network's energy buffer by the specified delta."""
        pass

    @Callback()
    def getX() -> int:
        """Get the container's X position in the world."""
        pass

    @Callback()
    def getY() -> int:
        """Get the container's Y position in the world."""
        pass

    @Callback()
    def getZ() -> int:
        """Get the container's Z position in the world."""
        pass

    @Callback()
    def getWorld() -> userdata:
        """Get the container's world object."""
        pass

    @Callback()
    def getPlayer(name:str) -> userdata:
        "Get the entity of a player."
        pass

    @Callback()
    def isModLoaded(name:str) -> bool:
        "Get whether a mod or API is loaded."
        pass

    @Callback()
    def runCommand(command:str) -> int:
        "Runs an arbitrary command using a fake player."
        pass

    @Callback()
    def connectToBlock(x:int, y:int, z:int) -> bool:
        "Connect the debug card to the block at the specified coordinates."
        pass

    @Callback()
    def test() -> userdata:
        "Test method for user-data and general value conversion."
        pass

    @Callback()
    def getWorld() -> userdata:
        """Get the player's world object."""
        pass

    @Callback()
    def getGameType() -> str:
        """Get the player's game type."""
        pass

    @Callback()
    def setGameType(gametype:str):
        """Set the player's game type (survival, creative, adventure)."""
        pass

    @Callback()
    def getPosition() -> (int, int, int):
        """Get the player's position."""
        pass

    @Callback()
    def setPosition(x:int, y:int, z:int):
        """Set the player's position."""
        pass

    @Callback()
    def getHealth() -> int:
        """Get the player's health."""
        pass

    @Callback()
    def getMaxHealth() -> int:
        """Get the player's max health."""
        pass

    @Callback()
    def setHealth(health:int):
        """Set the player's health."""
        pass

    @Callback()
    def getDimensionId() -> int:
        "Gets the numeric id of the current dimension."
        pass

    @Callback()
    def getDimensionName() -> str:
        "Gets the name of the current dimension."
        pass

    @Callback()
    def getSeed() -> int:
        "Gets the seed of the world."
        pass

    @Callback()
    def isRaining() -> bool:
        "Returns whether it is currently raining."
        pass

    @Callback()
    def setRaining(value:bool):
        "Sets whether it is currently raining."
        pass

    @Callback()
    def isThundering() -> bool:
        "Returns whether it is currently thundering."
        pass

    @Callback()
    def setThundering(value:bool):
        "Sets whether it is currently thundering."
        pass

    @Callback()
    def getTime() -> int:
        "Get the current world time."
        pass

    @Callback()
    def setTime(value:int):
        "Set the current world time."
        pass

    @Callback()
    def getSpawnPoint() -> (int, int, int):
        "Get the current spawn point coordinates."
        pass

    @Callback()
    def setSpawnPoint(x:int, y:int, z:int):
        "Set the spawn point coordinates."
        pass

    @Callback()
    def getBlockId(x:int, y:int, z:int) -> int:
        "Get the ID of the block at the specified coordinates."
        pass

    @Callback()
    def getMetadata(x:int, y:int, z:int) -> int:
        "Get the metadata of the block at the specified coordinates."
        pass

    @Callback()
    def isLoaded(x:int, y:int, z:int) -> int:
        "Check whether the block at the specified coordinates is loaded."
        pass

    @Callback()
    def hasTileEntity(x:int, y:int, z:int) -> int:
        "Check whether the block at the specified coordinates has a tile entity."
        pass

    @Callback()
    def getLightOpacity(x:int, y:int, z:int) -> int:
        "Get the light opacity of the block at the specified coordinates."
        pass

    @Callback()
    def getLightValue(x:int, y:int, z:int) -> int:
        "Get the light value (emission) of the block at the specified coordinates."
        pass

    @Callback()
    def canSeeSky(x:int, y:int, z:int) -> int:
        "Get whether the block at the specified coordinates is directly under the sky."
        pass

    @Callback()
    def setBlock(x:int, y:int, z:int, id:int or string, meta:int) -> int:
        "Set the block at the specified coordinates."
        pass

    @Callback()
    def setBlocks(x1:int, y1:int, z1:int, x2:int, y2:int, z2:int, id:int or string, meta:int) -> int:
        "Set all blocks in the area defined by the two corner points (x1, y1, z1) and (x2, y2, z2)."
        pass

    @Callback()
    def insertItem(id:str, count:int, damage:int, nbt:str, x:int, y:int, z:int, side:int) -> bool - Insert an item stack into the inventory at the specified location. NBT tag is expected in JSON format.:
        pass

    @Callback()
    def removeItem(x:int, y:int, z:int, slot:int, count=0:int) -> int - Reduce the size of an item stack in the inventory at the specified location.:
        pass

    @Callback()
    def insertFluid(id:str, amount:int, x:int, y:int, z:int, side:int) -> bool - Insert some fluid into the tank at the specified location.:
        pass

    @Callback()
    def removeFluid(amount:int, x:int, y:int, z:int, side:int) -> bool - Remove some fluid from a tank at the specified location.:
        pass


# Tablet.scala
class Tablet:
    @Callback()
    def getPitch() -> int:
        "Gets the pitch of the player holding the tablet."
        pass


# UpgradeSignInAdapter.scala
class UpgradeSignInAdapter:
    @Callback()
    def getValue(side:int) -> str:
        "Get the text on the sign on the specified side of the adapter."
        pass

    @Callback()
    def setValue(side:int, value:str) -> str:
        "Set the text on the sign on the specified side of the adapter."
        pass


# InventoryControl.scala
class InventoryControl:
    @Callback()
    def inventorySize() -> int:
        """The size of this device's internal inventory."""
        pass

    @Callback()
    def select(slot=0:int) -> int:
        "Get the currently selected slot; set the selected slot if specified."
        pass

    @Callback(direct = true)
    def count(slot=0:int) -> int:
        "Get the number of items in the specified slot, otherwise in the selected slot."
        pass

    @Callback(direct = true)
    def space(slot=0:int) -> int:
        "Get the remaining space in the specified slot, otherwise in the selected slot."
        pass

    @Callback()
    def compareTo(otherSlot:int) -> bool:
        "Compare the contents of the selected slot to the contents of the specified slot."
        pass

    @Callback()
    def transferTo(toSlot:int, amount=0:int) -> bool:
        "Move up to the specified amount of items from the selected slot into the specified slot."
        pass


# WorldInventoryAnalytics.scala
class WorldInventoryAnalytics:
    @Callback()
    def getInventorySize(side:int) -> int:
        "Get the number of slots in the inventory on the specified side of the device."
        pass

    @Callback()
    def getSlotStackSize(side:int, slot:int) -> int:
        "Get number of items in the specified slot of the inventory on the specified side of the device."
        pass

    @Callback()
    def getSlotMaxStackSize(side:int, slot:int) -> int:
        "Get the maximum number of items in the specified slot of the inventory on the specified side of the device."
        pass

    @Callback()
    def compareStacks(side:int, slotA:int, slotB:int) -> bool:
        "Get whether the items in the two specified slots of the inventory on the specified side of the device are of the same type."
        pass

    @Callback()
    def getStackInSlot(side:int, slot:int) -> table:
        "Get a description of the stack in the inventory on the specified side of the device."
        pass

    @Callback()
    def store(side:int, slot:int, dbAddress:str, dbSlot:int) -> bool:
        "Store an item stack description in the specified slot of the database with the specified address."
        pass


# InventoryWorldControl.scala
class InventoryWorldControl:
    @Callback
    def compare():
        pass

    @Callback
    def drop():
        pass

    @Callback
    def suck():
        pass


# TankControl.scala
class TankControl:
    @Callback
    def tankCount():
        pass

    @Callback
    def selectTank():
        pass

    @Callback(direct = true)
    def tankLevel():
        pass

    @Callback(direct = true)
    def tankSpace():
        pass

    @Callback
    def compareFluidTo():
        pass

    @Callback
    def transferFluidTo():
        pass


# TankWorldControl.scala
class TankWorldControl:
    @Callback
    def compareFluid():
        pass

    @Callback
    def drain():
        pass

    @Callback
    def fill():
        pass


# TankInventoryControl.scala
class TankInventoryControl:
    @Callback()
    def getTankLevelInSlot(slot=0:int) -> int:
        "Get the amount of fluid in the tank item in the specified slot or the selected slot."
        pass

    @Callback()
    def getTankCapacityInSlot(slot=0:int) -> int:
        "Get the capacity of the tank item in the specified slot of the robot or the selected slot."
        pass

    @Callback()
    def getFluidInTankInSlot(slot=0:int) -> table:
        "Get a description of the fluid in the tank item in the specified slot or the selected slot."
        pass

    @Callback()
    def getFluidInInternalTank(tank=0:int) -> table:
        "Get a description of the fluid in the tank in the specified slot or the selected slot."
        pass

    @Callback()
    def drain(amount=0:int) -> bool:
        "Transfers fluid from a tank in the selected inventory slot to the selected tank."
        pass

    @Callback()
    def fill(amount=0:int) -> bool:
        "Transfers fluid from the selected tank to a tank in the selected inventory slot."
        pass


# WorldTankAnalytics.scala
class WorldTankAnalytics:
    @Callback()
    def getTankLevel(side:int) -> int:
        "Get the amount of fluid in the tank on the specified side."
        pass

    @Callback()
    def getTankCapacity(side:int) -> int:
        "Get the capacity of the tank on the specified side."
        pass

    @Callback()
    def getFluidInTank(side:int) -> table:
        "Get a description of the fluid in the the tank on the specified side."
        pass


# WorldControl.scala
class WorldControl:
    @Callback
    def detect():
        pass


# InventoryAnalytics.scala
class InventoryAnalytics:
    @Callback()
    def getStackInInternalSlot(slot=0:int) -> table:
        "Get a description of the stack in the specified slot or the selected slot."
        pass

    @Callback()
    def storeInternal(slot:int, dbAddress:str, dbSlot:int) -> bool:
        "Store an item stack description in the specified slot of the database with the specified address."
        pass

    @Callback()
    def compareToDatabase(slot:int, dbAddress:str, dbSlot:int) -> bool:
        "Compare an item in the specified slot with one in the database with the specified address."
        pass


# InventoryWorldControlMk2.scala
class InventoryWorldControlMk2:
    @Callback()
    def dropIntoSlot(facing:int, slot:int, count=0:int) -> bool:
        "Drops the selected item stack into the specified slot of an inventory."
        pass

    @Callback()
    def suckFromSlot(facing:int, slot:int, count=0:int) -> bool:
        "Sucks items from the specified slot of an inventory."
        pass


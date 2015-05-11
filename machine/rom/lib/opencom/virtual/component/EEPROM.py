from ._environ import *

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
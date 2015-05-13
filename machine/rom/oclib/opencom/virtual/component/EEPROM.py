from ._environ import *

class EEPROM:
    def __init__(self, address, code="", label="", readonly=False, data=""):
        super().__init__(address)
        self.code = code
        self.label = label
        self.readonly = False
        self.data = data
    
    # TODO: common persist function for registered object?
    #       [!] will be move to persist module.
    def __persist__(self):
        return EEPROM, self.address
    
    @classmethod
    def __unpersist__(cls, *args):
        return cls(*args)
    
    @Callback(direct = true)
    def get(self) -> str:
        "Get the currently stored byte array."
        return self.code

    @Callback()
    def set(self, data:str):
        "Overwrite the currently stored byte array."
        self.code = code

    @Callback(direct = true)
    def getLabel(self) -> str:
        "Get the label of the EEPROM."
        return self.label

    @Callback()
    def setLabel(self, data:str) -> str:
        "Set the label of the EEPROM."
        self.label = data

    @Callback(direct = true)
    def getSize(self) -> str:
        "Get the storage capacity of this EEPROM."
        return 4096 # settings.eepromSize

    @Callback(direct = true)
    def getChecksum(self) -> str:
        "Get the checksum of the data on this EEPROM."
        return 0 # crc32(self.code)

    @Callback(direct = true)
    def makeReadonly(self, checksum:str) -> bool:
        """Make this EEPROM readonly if it isn't already. This process cannot be reversed!"""
        assert checksum == 0
        self.readonly = True

    @Callback(direct = true)
    def getDataSize(self) -> str:
        "Get the storage capacity of this EEPROM."
        return 256 # settings.eepromDataSize

    @Callback(direct = true)
    def getData(self) -> str:
        "Get the currently stored byte array."
        return self.data

    @Callback()
    def setData(self, data:str):
        "Overwrite the currently stored byte array."
        assert not self.readonly
        self.data = data


class ComponentManager:
    def __init__(self):
        pass
    
    def register(self, component):
        pass
    
    def get(self, component):
        pass
    
    def get_by_address(self, address):
        pass

components = ComponentManager()

def register(component):
    components.register(component)
    return component
    
from .component import EEPROM

# EEPROM()
# register()
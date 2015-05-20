
class ComponentManager:
    def __init__(self):
        self.components = {}
        self.component_by_type
    
    def register(self, component):
        self.components[component.address] = component
        self.component_by_type[type(component).__name__] = component
    
    def get(self, component, default=None):
        return self.component_by_type.get(component, default)
    
    def get_by_address(self, address, default=None):
        return self.components.get(address, default)

components = ComponentManager()

def register(component):
    components.register(component)
    return component
    
from .component import EEPROM

register(EEPROM())
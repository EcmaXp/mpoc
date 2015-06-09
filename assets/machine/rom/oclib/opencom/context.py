from .node import Node

class Context():
    def __init__(self):
        pass
    
    def node(self) -> Node:
        pass
    
    def canInteract(self) -> bool:
        pass

    def isRunning(self) -> bool:
        pass

    def isPaused(self) -> bool:
        pass

    def start(self) -> bool:
        pass

    def pause(self, seconds:float) -> bool:
        pass

    def stop(self) -> bool:
        pass

    def signal(self, name:str, *args) -> bool:
        pass
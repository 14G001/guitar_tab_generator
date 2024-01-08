class ConfigData:
    def __init__(self, windowElement, name):
        self.windowElement = windowElement
        self.name = name
    def set(self, value):
        self.windowElement.set(value)
    def get(self):
        return self.windowElement.get()
    def getType(self):
        return "TEXT"
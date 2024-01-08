from window.gui.event.click import clickElement
from configs.windowElement import updateConfig
from configs.database.configData.configData import ConfigData


class InputElement:
    def __init__(self, configName, elements, actionSetter, valueGetter, valueSetter):
        self.configData = self.getConfigData(configName)
        self.elements = elements
        self.getter = valueGetter
        self.setter = valueSetter
        self.value = self.get()
        if actionSetter != None:
            for element in self.elements:
                actionSetter(element, lambda: self.setNewValue())
    def set(self, value):
        self.value = value
        for element in self.elements:
            self.setter(element, value)
        updateConfig(self)
    def setNewValue(self):
        self.updateElementValueInWindows()
    def get(self):
        return self.getter(self.elements[0])
    def getConfigData(self, configName):
        return ConfigData(self, configName)

    def newValueConditions(self, newValue) -> bool:
        return True
    def getElementNewValue(self, previousValue):
        for element in self.elements:
            elementValue = self.getter(element)
            if elementValue != previousValue:
                if self.newValueConditions(elementValue):
                    return elementValue
                else:
                    return previousValue
        return previousValue
    def updateElementValueInWindows(self):
        self.set(self.getElementNewValue(self.value))

    def click(self):
        for element in self.elements:
            clickElement(element)
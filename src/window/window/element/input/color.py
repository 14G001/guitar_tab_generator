from window.gui.element.button import setButtonAction
from window.gui.element.input.colorInput import requestColor
from window.gui.style.color import getElementColor, setElementColor
from window.window.element.input.inputElement import InputElement
from configs.database.configData.colorConfigData import ColorConfigData


class ColorInput(InputElement):
    def __init__(self, configName, elements):
        super().__init__(configName, elements, setButtonAction, getElementColor, setElementColor)
    def setNewValue(self):
        selectedColor = requestColor()
        if selectedColor == None:
            return
        self.set(selectedColor)
    def getConfigData(self, configName):
        return ColorConfigData(self, configName)
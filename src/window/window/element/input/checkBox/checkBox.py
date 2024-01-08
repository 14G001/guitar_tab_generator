from window.gui.element.button import setButtonAction
from window.gui.style.color import setElementColor
from window.gui.element.input.checkBox import getChecked, setChecked
from window.window.element.input.inputElement import InputElement
from utils.colors import BLACK
from configs.database.configData.checkBoxConfigData import CheckBoxConfigData


CB_NO_COLOR = BLACK

CB_TRUE =  False
CB_FALSE = True


class CheckBox(InputElement):
    def __init__(self, configName, elements, elementsToUncheck = []):
        super().__init__(configName, elements, setButtonAction, getChecked, setChecked)
        self.elementsToUncheck = elementsToUncheck
    def setNewValue(self):
        self.switch()
    def getConfigData(self, configName):
        return CheckBoxConfigData(self, configName)
    def getColorChecked(self):
        return CB_NO_COLOR
    def getColorNotChecked(self):
        return CB_NO_COLOR
    # Remember: checking can be unchecking on final results; should make tests for this cases; probably should config .ui file:
    def switch(self):
        if getChecked(self.elements[0]):
            self.forEach(CB_FALSE)
            return
        self.forEach(CB_TRUE)
    def forEachElement(self, actionSelf, colorSelf, actionEToUncheck, colorToUncheck):
        for element in self.elements:
            actionSelf(element, colorSelf())
        for element in self.elementsToUncheck:
            actionEToUncheck(element, colorToUncheck())
    def forEach(self, setChecked):
        if setChecked:
            self.forEachElement(self.check, self.getColorChecked, self.uncheck, self.getColorNotChecked)
            return
        self.forEachElement(self.uncheck, self.getColorNotChecked, self.check, self.getColorChecked)
    def uncheck(self, element, color):
        setChecked(element, CB_TRUE)
        setElementColor(element, color)
    def check(self, element, color):
        setChecked(element, CB_FALSE)
        setElementColor(element, color)
from window.window.element.input.checkBox.checkBox import CheckBox
from window.gui.style.border import setElementBorder
from utils.colors import WHITE, MEDIUM_GREY


COLOR_CHECKED =     WHITE
COLOR_NOT_CHECKED = MEDIUM_GREY
BORDER_CHECKED = (8, COLOR_NOT_CHECKED)


class DefaultCheckBox(CheckBox):
    def __init__(self, configName, elements, elementsToUncheck = []):
        for element in elements:
            setElementBorder(element, BORDER_CHECKED[0], BORDER_CHECKED[1])
        super().__init__(configName, elements, elementsToUncheck)
    def getColorChecked(self):
        return COLOR_CHECKED
    def getColorNotChecked(self):
        return COLOR_NOT_CHECKED
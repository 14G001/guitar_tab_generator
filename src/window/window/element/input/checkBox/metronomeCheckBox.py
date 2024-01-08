from window.window.element.input.checkBox.checkBox import CheckBox
from window.gui.style.text import setElementText
from utils.colors import GREEN, LIGHT_GREEN


COLOR_CHECKED =     GREEN
COLOR_NOT_CHECKED = LIGHT_GREEN


class MetronomeCheckBox(CheckBox):
    def __init__(self, elements):
        super().__init__(None, elements)
        self.click()
    def getColorChecked(self):
        return COLOR_CHECKED
    def getColorNotChecked(self):
        return COLOR_NOT_CHECKED
    def uncheck(self, element, color):
        super().uncheck(element, color)
        setElementText(element, "Start")
    def check(self, element, color):
        super().check(element, color)
        setElementText(element, "Stop")
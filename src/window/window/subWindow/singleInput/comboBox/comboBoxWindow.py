from window.window.subWindow.singleInput.singleInputWindow import SingleInputWindow
from window.gui.window.type.comboBoxWin import Ui_ComboBoxWindow
from window.gui.element.input.comboBox import addComboBoxOptions
from window.gui.element.input.comboBox import getCurrOptTxt
from abc import abstractmethod


class ComboBoxWindow(SingleInputWindow):
    def __init__(self, message, comboBoxOptions, errorWindow = None):
        super().__init__(message, Ui_ComboBoxWindow(), getCurrOptTxt, errorWindow)
        if errorWindow != None:
            return
        addComboBoxOptions([self.getInputElement()], comboBoxOptions)
    @abstractmethod
    def acceptAction(self):
        pass
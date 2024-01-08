from window.window.subWindow.singleInput.singleInputWindow import SingleInputWindow
from window.gui.window.type.textLineInputWin import Ui_TextLineInputWindow
from window.gui.style.text import getElementText
from abc import abstractmethod


class TextLineInputWindow(SingleInputWindow):
    def __init__(self, message):
        super().__init__(message, Ui_TextLineInputWindow(), getElementText)
    @abstractmethod
    def acceptAction(self):
        pass
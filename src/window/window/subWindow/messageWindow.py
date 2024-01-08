from window.gui.window.type.messageWin import Ui_MessageWindow
from window.gui.window.window import GUIWindow
from window.gui.style.color import setElementColor
from window.gui.style.text import setElementText
from window.gui.event.window import showWindow
from window.gui.element.button import setButtonAction
from utils.colors import LIGHT_BLUE, RED


class MessageWindow(GUIWindow):
    def __init__(self, message):
        super().__init__(Ui_MessageWindow())
        setElementColor(self.window.symbol, self.getSymbolColor())
        setElementText(self.window.message, message)
        setButtonAction(self.window.acceptButton, self.close)
        showWindow(self)
    def getSymbolColor(self):
        return LIGHT_BLUE

class ErrorWindow(MessageWindow):
    def __init__(self, message):
        super().__init__(message)
    def getSymbolColor(self):
        return RED
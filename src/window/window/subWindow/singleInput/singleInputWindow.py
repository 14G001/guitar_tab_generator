from window.gui.event.window import closeWindow
from window.gui.window.window import GUIWindow
from window.gui.style.text import setElementText
from window.gui.element.button import setButtonAction
from window.gui.event.window import showWindow
from window.window.subWindow.messageWindow import MessageWindow, ErrorWindow
from abc import ABC, abstractmethod


class SingleInputWindow(ABC, GUIWindow):
    def __init__(self, message, window, valueGetter, errorWindow = None):
        super().__init__(window, errorWindow)
        if errorWindow != None:
            return
        self.valueGetter = valueGetter
        setElementText(self.window.message, message)
        setButtonAction(self.window.leftButton, self.acceptAction)
        setElementText(self.window.leftButton, self.getLeftButtonText())
        setButtonAction(self.window.rightButton, self.close)
        self.extraWindow = None
        showWindow(self)
    def get(self):
        return self.valueGetter(self.getInputElement())
    def getInputElement(self):
        return self.window.input
    @abstractmethod
    def acceptAction(self):
        pass

    def getLeftButtonText(self):
        return "Save"
    
    def setExtraWindow(self, window):
        if self.extraWindow != None:
            closeWindow(self.extraWindow)
        self.extraWindow = window
    def showMessage(self, message):
        self.setExtraWindow(MessageWindow(message))
    def showError(self, message):
        self.setExtraWindow(ErrorWindow(message))

    def setNewWindow(self, window):
        self.window = window
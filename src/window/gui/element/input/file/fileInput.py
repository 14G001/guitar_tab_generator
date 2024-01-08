from PyQt5.QtWidgets import QPushButton
from window.gui.style.style import getElementStyle, setElementStyle
from window.gui.style.cursor import setCursor, CURSOR_POINTER
from window.gui.style.size import copyElementSize
from window.gui.style.text import getElementText, setElementText
from window.gui.event.dragAndDrop import setAcceptDrops

class GUIFileInput(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        copyElementSize(self, parent)
        setElementStyle(self, getElementStyle(parent))
        setElementText(self, getElementText(parent))
        setAcceptDrops(self, True)
        setCursor(self, CURSOR_POINTER)
    def setEvents(self, clickAction, dropCondition, dropAction):
        self.onClick = clickAction
        self.dropCondition = dropCondition
        self.onDrop = dropAction
    def mousePressEvent(self, event):
        self.onClick()
    def dragEnterEvent(self, event):
        if self.dropCondition(event):
            event.accept()
            return
        event.ignore()
    def dropEvent(self, event):
        if self.dropCondition(event):
            self.onDrop(event)
            event.accept()
            return
        event.ignore()
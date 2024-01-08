from PyQt5.QtWidgets import QMainWindow
from window.gui.event.window import closeWindow


class GUIWindow():
    def __init__(self, window, errorWindow = None):
        self.gui = QMainWindow()
        if errorWindow != None:
            self.window = errorWindow
            return
        self.window = window;
        self.window.setupUi(self.gui)
    def close(self):
        closeWindow(self)
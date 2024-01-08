import sys
from PyQt5.QtWidgets import QApplication
from window.gui.window.type.mainWin import Ui_MainWindow
from window.gui.window.window import GUIWindow
from window.gui.event.window import showWindow
from window.window.mainWindow.mainWindow import setWindow
from window.window.mainWindow.elements import MainWindow
from configs.configs import Configs


def mainLoop():
    app = QApplication(sys.argv)
    mainWin = GUIWindow(Ui_MainWindow())
    setWindow(MainWindow(mainWin.window))
    Configs().init()
    showWindow(mainWin)
    sys.exit(app.exec_())

mainLoop()
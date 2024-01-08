from window.gui.element.button import setButtonAction
from window.gui.style.color import setElementColor
from window.gui.element.input.checkBox import getChecked, setChecked
from window.gui.style.size import setElementSize
from window.window.element.input.inputElement import InputElement
from utils.colors import DARK_GREY, WHITE_GREY


class SndMainWinMenuButton(InputElement):
    def __init__(self, window, button, menuBG):
        self.window = window
        self.button = button
        self.menuBG = menuBG
        setButtonAction(self.button, lambda: self.switch())
        self.uncheck()

    def uncheck(self):
        setChecked(self.button, True)
        setElementColor(self.menuBG, DARK_GREY)
        self.uncheckResizeWindow()

    def check(self):
        setChecked(self.button, False)
        setElementColor(self.menuBG, WHITE_GREY)

    def switch(self):
        if getChecked(self.button):
            self.uncheck()
        else:
            self.check()

    def uncheckResizeWindow(self):
        # TODO: Check why is not resizing window height at minimum
        setElementSize(self.window, (self.window.size().width(), 0))
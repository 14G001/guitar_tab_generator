from window.gui.element.input.textLineInput import setTextLineInputAction
from window.gui.style.text import getElementText, setElementText
from window.window.element.input.inputElement import InputElement


class TextLineInput(InputElement):
    def __init__(self, configName, elements):
        super().__init__(configName, elements, setTextLineInputAction, getElementText, setElementText) 

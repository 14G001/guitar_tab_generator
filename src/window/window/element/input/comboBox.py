from window.window.element.input.inputElement import InputElement
from window.gui.element.input.comboBox import setComboBoxAction, getCurrOptTxt, setCurrOptTxt, addComboBoxOptions

class ComboBox(InputElement):
    def __init__(self, configName, elements, options):
        super().__init__(configName, elements, setComboBoxAction, getCurrOptTxt, setCurrOptTxt)
        addComboBoxOptions(elements, options)
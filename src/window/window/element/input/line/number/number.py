from window.window.element.input.line.text import TextLineInput


class NumberInput(TextLineInput):
    def __init__(self, configName, elements):
        super().__init__(configName, elements)
    def newValueConditions(self, newValue):
        if newValue.isdecimal() or newValue == "":
            return True
        return False

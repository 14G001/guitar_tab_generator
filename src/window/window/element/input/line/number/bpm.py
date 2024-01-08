from window.window.element.input.line.number.number import NumberInput


class BPMInput(NumberInput):
    def __init__(self, configName, elements):
        super().__init__(configName, elements)
    def newValueConditions(self, newValue):
        if super().newValueConditions(newValue) and len(newValue) < 4:
            return True
        return False
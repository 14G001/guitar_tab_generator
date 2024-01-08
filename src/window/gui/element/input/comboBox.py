def setComboBoxAction(comboBox, action):
    comboBox.currentIndexChanged.connect(action)
def getCurrOptTxt(comboBox):
    return comboBox.currentText()
def setCurrOptTxt(comboBox, value):
    comboBox.setCurrentText(value)
    
def addComboBoxOptions(comboBoxes, comboBoxElements):
    for comboBox in comboBoxes:
        for comboBoxElement in comboBoxElements:
            comboBox.addItem(comboBoxElement)

def removeComboBoxOption(comboBoxes, option):
    for comboBox in comboBoxes:
        comboBox.removeItem(comboBox.findText(option))
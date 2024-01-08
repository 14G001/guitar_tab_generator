from window.window.subWindow.singleInput.comboBox.comboBoxWindow import ComboBoxWindow
from configs.configs import Configs
from window.gui.element.input.comboBox import removeComboBoxOption
from window.window.subWindow.messageWindow import MessageWindow


class RemoveConfigWindow(ComboBoxWindow):
    def __init__(self):
        message = "Select the config to delete:"
        configNames = Configs().getConfigNames()
        if len(configNames) < 1:
            super().__init__(message, configNames, errorWindow = MessageWindow("There are no saved configs."))
            return
        super().__init__(message, configNames)
    def acceptAction(self):
        Configs().deleteConfig(self.get())
        removeComboBoxOption([self.getInputElement()], self.get())
        self.showMessage("Configuration deleted successfully.")
        if self.get() == "":
            self.close()
    def getLeftButtonText(self):
        return "Delete"
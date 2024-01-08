from window.window.subWindow.singleInput.comboBox.comboBoxWindow import ComboBoxWindow
from configs.configs import Configs
from window.gui.element.input.comboBox import removeComboBoxOption
from window.window.subWindow.messageWindow import MessageWindow


class RestoreConfigWindow(ComboBoxWindow):
    def __init__(self):
        message = "Select the config to restore:"
        configNames = Configs().getConfigNames()
        if len(configNames) < 1:
            super().__init__(message, configNames, errorWindow = MessageWindow("There are no saved configs."))
            return
        super().__init__(message, configNames)
    def acceptAction(self):
        Configs().restoreConfig(cfgName = self.get())
        self.showMessage("Configuration restored successfully.")
        self.close()
    def getLeftButtonText(self):
        return "Restore"
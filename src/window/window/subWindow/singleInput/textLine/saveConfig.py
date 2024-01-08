from window.window.subWindow.singleInput.textLine.textLineInputWindow import TextLineInputWindow
from configs.configs import Configs


class SaveConfigWindow(TextLineInputWindow):
    def __init__(self):
        super().__init__("Enter current configuration name:")
    def acceptAction(self):
        if self.get() == "":
            return self.showError("Configuration name can't be empty.")
        if Configs().addNewConfig(self.get()):
            self.showMessage("Configuration saved successfully.")
        else:
            self.showError("A configuration with that name already exist.")
        return self.close()
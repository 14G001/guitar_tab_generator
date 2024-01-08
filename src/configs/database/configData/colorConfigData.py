from configs.database.configData.configData import ConfigData
from utils.color import strColorToRGB

class ColorConfigData(ConfigData):
    def set(self, value):
        super().set(strColorToRGB(value))
    def get(self):
        return str(super().get()).replace("(", "").replace(")", "")
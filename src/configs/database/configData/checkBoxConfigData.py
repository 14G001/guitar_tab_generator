from configs.database.configData.configData import ConfigData

class CheckBoxConfigData(ConfigData):
    def set(self, value):
        return super().set(bool(value))
    def get(self):
        return int(super().get())
    def getType(self):
        return "INT"
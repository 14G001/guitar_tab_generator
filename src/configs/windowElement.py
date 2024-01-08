from configs.configs import Configs


def updateConfig(windowElement):
    if windowElement.configData.name == None:
        return
    Configs().updateConfig(
        cfgName = windowElement.configData.name,
        value = windowElement.configData.get()
    )
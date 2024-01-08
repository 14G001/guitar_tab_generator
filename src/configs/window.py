from window.window.mainWindow.mainWindow import getWindowInputs

def setWindowConfigs(configs):
    configCounter = 0
    for winCfg in getWindowInputs():
        winCfg.configData.set(configs[configCounter])
        configCounter += 1

def getWindowConfigs():
    windowConfigs = []
    for winCfg in getWindowInputs():
        windowConfigs.append(winCfg.configData.get())
    return tuple(windowConfigs)

def getWindowConfigsColumnData():
    windowConfigsColumnData = ""
    for winCfg in getWindowInputs():
        windowConfigsColumnData += winCfg.configData.name + winCfg.configData.getType() + ", "
    return windowConfigsColumnData[:-2]
from file.file import createFolder, fileExist
from configs.database.database.configsDatabase import ConfigsDatabase as Database
from configs.default import DEFAULT_CFGS
from configs.database.references import CONFIGS_FOLDER, USR_CHOICE_FILE, ID_CURR_CFG, ID_DEF_CFG
from configs.window import getWindowConfigs, setWindowConfigs, getWindowConfigsColumnData


class Configs():
    def setDefault(self):
        self.restoreConfig(ID_DEF_CFG)

    def init(self):
        createFolder(CONFIGS_FOLDER)
        if not fileExist(USR_CHOICE_FILE):
            Database().createTable("ID INT, Name TEXT, " + getWindowConfigsColumnData())
            for cfgID, cfgName in ((ID_CURR_CFG, "Current Cfg"), (ID_DEF_CFG, "Default Cfg")):
                Database().addRow((cfgID, cfgName) + DEFAULT_CFGS)
            print("User cfgs database creted successfully.")
            return
        print("User cfgs database already creted.")
        self.restoreConfig(ID_CURR_CFG)
    
    def deleteConfig(self, configName):
        Database().deleteRow(configName)
    
    def addNewConfig(self, configName):
        newID = Database().getNewID()
        if configName in self.getConfigNames():
            return False
        Database().addRow((newID + 1, configName) + getWindowConfigs())
        return True
    
    def getConfigNames(self):
        cfgNames = Database().getColumn("name")
        finalCfgNames = []
        for name in cfgNames:
            finalCfgNames.append(name[0])
        del finalCfgNames[0]
        del finalCfgNames[0]
        return finalCfgNames
    
    def updateConfig(self, cfgName = str, value = None):
        Database().update(cfgName, ID_CURR_CFG, value)

    def restoreConfig(self, identifier):
        setWindowConfigs(Database().getRowElements(identifier)[0][2:])

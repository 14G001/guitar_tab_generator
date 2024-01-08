CONFIGS_FOLDER =     "cfgs"
USR_CHOICE_FILE =    CONFIGS_FOLDER + "\\\\" + "usr_choices.db"
DB_TABLENAME_CFGS = "UserCfgs"

ID_CURR_CFG = 0
ID_DEF_CFG = 1


def getSearchWay(identifier):
    if str(type(identifier)) == str(int):
        return "id", str(identifier)
    return "name", "'" + identifier + "'"
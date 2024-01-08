from configs.database.database.database import Database
from configs.database.references import DB_TABLENAME_CFGS

class ConfigsDatabase(Database):
    def __init__(self):
        super().__init__(DB_TABLENAME_CFGS)
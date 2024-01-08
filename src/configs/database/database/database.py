import sqlite3
from configs.database.syntax import getQuestionMarks
from configs.database.references import USR_CHOICE_FILE, getSearchWay


class Database:
    def __init__(self, tableName):
        self.tableName = tableName
        self.database = sqlite3.connect(USR_CHOICE_FILE)
        self.cursor = self.database.cursor()
    def commitAndClose(self, retValue = None):
        self.database.commit()
        self.cursor.close()
        return retValue
    def execute(self, command, params = None):
        if params == None:
            self.cursor.execute(command)
        else:
            self.cursor.execute(command, params)
        self.commitAndClose()
    def get(self, command, params = None):
        elements = None
        if params == None:
            elements = self.cursor.execute(command).fetchall()
        else:
            elements = self.cursor.execute(command, params).fetchall()
        self.commitAndClose()
        return elements
    def createTable(self, columns):
        self.execute("CREATE TABLE " + self.tableName + "(" + columns + ")")
    def addRow(self, rowElements):
        self.execute("INSERT INTO " + self.tableName + " VALUES " + getQuestionMarks(len(rowElements)), rowElements)
    def deleteRow(self, rowName):
        self.execute("DELETE FROM " + self.tableName + " WHERE name = '" + rowName + "'")
    def getNewID(self):
        lastElement = self.get("SELECT id FROM " + self.tableName + " ORDER BY id DESC LIMIT 1")
        print("LAST ELEMENT: " + str(lastElement))
        return lastElement[0][0]
    def getColumn(self, columnName):
        return self.get("SELECT " + columnName + " FROM " + self.tableName)
    def update(self, columnName, rowID, value):
        self.execute("UPDATE " + self.tableName + " SET " + columnName + " = ? WHERE id = " + str(rowID), [value])
    def getRowElements(self, rowID):
        columnName, rowID = getSearchWay(rowID)
        return self.get("SELECT * FROM " + self.tableName + " WHERE " + columnName + " = " + rowID)
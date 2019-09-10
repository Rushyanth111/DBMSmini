from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QTableView

## Simple Table View.
class Table(QTableView):
    def __init__(self, databaseName, TableName, parent=None):
        super().__init__(parent=parent)
        self.dbName = databaseName
        self.table = TableName
        self.createTable()

    def createTable(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.dbName)
        self.db.open()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable(self.table)
        self.model.setEditStrategy(self.model.OnFieldChange)
        self.model.select()
        self.setModel(self.model)
    def Remove(self):
        self.db.removeDatabase("QSQLITE");
        
    def refresh(self):
        self.model.select();
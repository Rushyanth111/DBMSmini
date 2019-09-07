from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QTableView

## Simple Table View.
class Table(QTableView):
    def __init__(self, databaseName, TableName, parent=None):
        super().__init__(parent=parent)
        self.setEditTriggers(self.NoEditTriggers);
        self.dbName = databaseName
        self.table = TableName
        self.createTable()

    def createTable(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(self.dbName)
        db.open()

        model = QSqlTableModel(self, db)
        model.setTable(self.table)
        model.select()
        self.setModel(model)

from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QTableView

## Simple Table View.
class Table(QTableView):
    def __init__(self, databaseName, TableName, database, parent=None):
        super().__init__(parent=parent)
        self.setEditTriggers(self.NoEditTriggers);
        self.dbName = databaseName
        self.table = TableName
        self.db = database
        self.createTable()

    def createTable(self):

        model = QSqlTableModel(self, self.db)
        model.setTable(self.table)
        model.select()
        self.setModel(model)

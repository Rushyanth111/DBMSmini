from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QTableView

# Simple Table View.


class Table(QTableView):
    def __init__(self, databaseName, TableName, database: QSqlDatabase, parent=None):
        super().__init__(parent=parent)
        self.dbName = databaseName
        self.table = TableName
        self.db = database
        self.createTable()

    def createTable(self):
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable(self.table)
        self.model.select()
        self.setModel(self.model)

    def refresh(self):
        self.model.select()

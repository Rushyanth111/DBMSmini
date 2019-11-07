from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5.QtWidgets import QTableView

# Simple Table View.


class Table(QTableView):
    def __init__(
        self, databaseName: str, TableName: str, database: QSqlDatabase, parent=None
    ):
        super().__init__(parent=parent)
        self.InsertStatement = ""
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

    def InsertGenerate(self):
        print("called")
        q = QSqlQuery()
        q.exec_("PRAGMA table_info({})".format(self.table))
        dataTypes = []
        pk = []
        # Values Required: Datatype is value(2)
        # pk value is present in value(5)
        while q.next():
            dataTypes.append(q.value(2))
            pk.append(5)

        InsertQuery = "INSERT INTO " + self.table + " VALUES ("
        for x in range(len(dataTypes)):
            if (
                dataTypes[x] == "Integer"
                or dataTypes[x] == "Real"
                or dataTypes[x] == "Float"
            ):
                InsertQuery += "{}"
            if dataTypes[x] == "Text" or dataTypes[x] == "Date":
                InsertQuery += '"{}"'
            if len(dataTypes) != x + 1:
                InsertQuery += ","

        InsertQuery += ")"

        print(InsertQuery)

    def Insert(self, *args):
        self.InsertStatement = self.InsertStatement.format(*args)
        self.db.exec_(self.InsertStatement)
        self.refresh()


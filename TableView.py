"""Holds QWidget Table and it's assorted Functions.
"""
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5.QtWidgets import QTableView

# Simple Table View.


class Table(QTableView):
    """[summary]

    """

    def __init__(
        self, database_name: str, table_name: str, database: QSqlDatabase, parent=None
    ):
        super().__init__(parent=parent)

        # Set Some variables.
        self.__insert_statement__ = ""
        self.__data_types__ = []
        self.__primary_keys__ = []
        self.__db_name__ = database_name
        self.__table__ = table_name
        self.__db__ = database
        # Generate the Insert Statement
        self.InsertGenerate()

        # Set the table Outlook.
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable(self.table)
        self.model.select()

        # Set the model
        self.setModel(self.model)

    def refresh(self):
        """ Refershes the Table Upon an Insert Operation.
        """
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
            else:
                InsertQuery += '"{}"'
            if len(dataTypes) != x + 1:
                InsertQuery += ","

        InsertQuery += ");"
        self.insert_statement = InsertQuery

    def Insert(self, *args):
        arr = [*args]
        for x in range(len(arr)):
            if not str(arr[x]):  # Catches Empty String.
                arr[x] = "NULL"

        CompleteInsertQuery = self.insert_statement.format(*arr)
        self.db.exec_(CompleteInsertQuery)
        self.refresh()

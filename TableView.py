"""Holds QWidget Table and it's assorted Functions.
"""
from typing import List
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import Qt

from QSqlCustomQuery import QCustomQuery


class Table(QTableView):
    """Custom Implementation of QTableView

    Arguments:
        table_name {str} -- Name of the table in the database.
        database {QSqlDatabase} -- The Database Object from QSqlDatabase.

    Keyword Arguments:
        parent {Any} -- Parent to the Table (default: {None})
    """

    def __init__(self, table_name: str, database: QSqlDatabase, parent=None) -> None:
        super().__init__(parent=parent)

        # Set Some variables.
        self.__insert_statement__ = ""
        self.__data_types__ = []
        self.__primary_keys__ = []
        self.__table__ = table_name
        self.__db__ = database
        # Generate the Insert Statement
        self.__insert_generate__()

        # Set the table Outlook.
        self.setGridStyle(Qt.DashLine)
        self.__model__ = QSqlTableModel(self, self.__db__)
        self.__model__.setTable(self.__table__)
        self.__model__.select()

        # Set the model
        self.setModel(self.__model__)

    def refresh(self) -> None:
        """ Refershes the Table Upon an Insert Operation.
        """
        self.__model__.select()

    def __insert_generate__(self) -> None:
        """Generates the insert Query for the current table.
        """
        print("called")
        query = QSqlQuery()
        query.exec_("PRAGMA table_info({})".format(self.__table__))
        # Values Required: Datatype is value(2)
        # pk value is present in value(5)
        while query.next():
            self.__data_types__.append(query.value(2))
            self.__primary_keys__.append(5)

        tempquery = "INSERT INTO " + self.__table__ + " VALUES ("
        for value in self.__data_types__:
            if value in ("Integer", "Real", "Float"):
                tempquery += "{},"
            else:
                tempquery += '"{}",'

        tempquery = tempquery.rstrip(",") + ");"
        self.insert_statement = tempquery

    def insert_into_table(self, *args) -> None:
        """Inserts args into table.
        """
        arr = [*args]
        for itr, item in enumerate(arr):
            if not str(item):  # Catches Empty String.
                arr[itr] = "NULL"

        formattedquery = self.insert_statement.format(*arr)
        query = QSqlQuery()
        if query.exec_(formattedquery) is False:
            # TODO: Ensure that the Exception is properly handled
            # and displayed to the user.
            raise Exception('Inputted Format is not correct!')
        self.refresh()

    def get_col_names(self, fmt: bool = False) -> List[str]:
        """Obtains the column Names for the table.

        Optionally Formats them replacing underscores with whitespaces.

        Arguments:

            fmt {bool} -- Set to true if need to format.

        Returns:
            List[str] -- Returns a List of Strings containing Column Names.
        """
        query = QCustomQuery("pragma table_info({})".format(self.__table__))
        cols = query.get_column(1)

        if fmt is True:
            cols = [x.replace("_", " ") for x in cols]

        return cols

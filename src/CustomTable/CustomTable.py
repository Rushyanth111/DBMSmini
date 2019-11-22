"""Holds QWidget Table and it's assorted Functions.
"""
from typing import List
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import Qt

from Query import QCustomQuery


class Table(QTableView):
    """Custom Implementation of QTableView

    Arguments:
        table_name {str} -- Name of the table in the database.

    Keyword Arguments:
        parent {Any} -- Parent to the Table (default: {None})
    """

    def __init__(self, table_name: str, parent=None) -> None:
        super().__init__(parent=parent)

        # Set Some variables.
        self.__insert_statement__ = ""
        self.__update_statement__ = ""
        self.__data_types__ = []
        self.__primary_keys__ = []
        self.__table__ = table_name
        self.__db__ = QSqlDatabase()

        # Set some Definition Variables
        self.__last__error__ = ""

        # Generate the Insert Statement
        self.__insert_generate__()
        self.__update_generate__()

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
            self.__primary_keys__.append(query.value(5))

        tempquery = "INSERT INTO " + self.__table__ + " VALUES ("
        for value in self.__data_types__:
            if value in ("Integer", "Real", "Float"):
                tempquery += "{},"
            else:
                tempquery += '"{}",'

        tempquery = tempquery.rstrip(",") + ");"
        self.insert_statement = tempquery

    def insert_into_table(self, *args) -> bool:
        """Inserts args into table.
        """
        arr = [*args]
        for itr, item in enumerate(arr):
            if not str(item):  # Catches Empty String.
                arr[itr] = "NULL"

        formattedquery = self.insert_statement.format(*arr)
        query = QSqlQuery()
        if query.exec_(formattedquery) is False:
            self.__last__error__ = query.lastError().text()
            return False
        self.refresh()

        return True

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

    def get_last_error(self):
        error = self.__last__error__.split(" ")[3]
        return error.replace("_", " ")

    def get_col_types(self, fmt: bool = False) -> List[str]:
        query = QCustomQuery("pragma table_info({})".format(self.__table__))
        cols = query.get_column(2)

        if fmt is True:
            cols = [x.replace("_", " ") for x in cols]

        return cols

    def get_col_prim(self) -> List[str]:
        query = QCustomQuery("pragma table_info({})".format(self.__table__))
        cols = query.get_column(5)
        return cols

    def get_row_selected(self) -> List[str]:
        index = self.selectionModel().currentIndex()
        row = index.row()
        if row == -1:
            return []
        row_data = []
        for itr in range(self.__model__.record(row).count()):
            row_data.append(self.__model__.record(row).field(itr).value())

        return row_data

    def __update_generate__(self):
        ustring = "UPDATE " + self.__table__ + " Set "
        for val, typs in zip(self.get_col_names(), self.__data_types__):
            if typs == "Float" or typs == "Integer":
                ustring += str(val) + "={}, "
            else:
                ustring += str(val) + """='{}',"""
        ustring = ustring.rstrip(",")

        ustring += " WHERE "
        for prim, val, typs in zip(
            self.__primary_keys__, self.get_col_names(), self.__data_types__
        ):
            if prim == 1:
                if typs == "Float" or typs == "Integer":
                    ustring += str(val) + "={} AND "
                else:
                    ustring += str(val) + """='{}' AND """

        ustring = ustring.rstrip("AND ")
        ustring += ";"
        self.__update_statement__ = ustring

        return ustring

    def update(self, *args):
        ulist = []

        for x in args:
            ulist.append(x)
        
        for prim, val in zip(self.__primary_keys__, args):
            if prim == 1:
                ulist.append(val)
        ustring = self.__update_statement__.format(*ulist)
        print(ustring)
        query = QSqlQuery()
        if query.exec_(ustring) is False:
            self.__last__error__ = query.lastError().text()
            return False
        self.refresh()

        return True


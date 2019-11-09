"""Holds QCustomQuery -- A replacement for the QSqlQuery Class Internally with convience
"""

from PyQt5.QtSql import QSqlQuery, QSqlDatabase


class QCustomQuery(QSqlQuery):
    """Custom Query Class with Convience.

    Keyword Arguments:

        query {str} -- [Query String to be executed] (default: {""})

        db {QSqlDatabase} -- [Database for the Query to be executed on] (default: {QSqlDatabase()})
    """

    def __init__(self, query: str = "", db=QSqlDatabase()):
        super().__init__(query=query, db=db)
        self.__result__ = []
        self.exec_(query)
        self.GetAllRecords()

    def GetAllRecords(self):
        while self.next():
            inner_res = []
            for x in range(self.record().count()):
                inner_res.append(self.value(x))
            self.__result__.append(inner_res)
        return self.__result__

    def get_row(self, row_num):
        pass

    def get_column(self, col_num):
        pass

    def check_empty_result(self):
        pass


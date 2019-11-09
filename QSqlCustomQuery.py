"""Holds QCustomQuery -- A replacement for the QSqlQuery Class Internally with convience
"""

from typing import List, Any
from PyQt5.QtSql import QSqlQuery, QSqlDatabase


class QCustomQuery(QSqlQuery):
    """Custom Query Class with Convience.

    Keyword Arguments:

        query {str} -- [Query String to be executed] (default: {""})
        database {QSqlDatabase} -- [Database to be executed on] (default: {QSqlDatabase()})
    """

    def __init__(self, query: str = "", database=QSqlDatabase()):
        super().__init__(query=query, db=database)
        self.__result__ = []
        self.exec_(query)
        self.get_all_records()

    def get_all_records(self) -> List[List[Any]]:
        """Obtains all Records of the Query Exectued.

        Returns:

            [list] -- [list of list of all rows.]
        """
        while self.next():
            inner_res = []
            for itr in range(self.record().count()):
                inner_res.append(self.value(itr))
            self.__result__.append(inner_res)
        return self.__result__

    def get_row(self, row_num: int) -> List[Any]:
        """[summary]

        Arguments:

            row_num {int} -- [description]

        Returns:

            list -- [description]
        """
        return self.__result__[row_num]

    def get_column(self, col_num) -> List[Any]:
        """[summary]

        Arguments:
            col_num {[type]} -- [description]

        Returns:
            list -- [description]
        """
        return list(map(list, zip(*self.__result__)))[col_num]

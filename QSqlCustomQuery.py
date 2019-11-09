from PyQt5.QtSql import QSqlQuery, QSqlDatabase


class QCustomQuery(QSqlQuery):
    def __init__(self, query="", db=QSqlDatabase()):
        super().__init__(query=query, db=db)
        self.exec_(query)

    def GetAllRecords(Query: QSqlQuery):
        Res = []
        while Query.next():
            InRes = []
            for x in range(Query.record().count()):
                InRes.append(Query.value(x))
            Res.append(InRes)
        return Res

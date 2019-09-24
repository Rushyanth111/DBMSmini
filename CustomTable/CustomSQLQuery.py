from PyQt5.QtSql import QSqlQuery, QSqlDatabase


class QCustomQuery(QSqlQuery):
    def __init__(self, db=QSqlDatabase()):
        super().__init__(db=db)

    def executeQuery(self, Query) -> list:
        self.exec_(Query)
        Res = []
        while self.next():
            InRes = []
            for x in range(self.record().count()):
                InRes.append(self.value(x))
            Res.append(InRes)
        return Res

    def ObtainColoumnTypes(self, TableName: str) -> list:
        PragmaString = """PRAGMA table_info({})""".format(TableName)
        Types = [x[2] for x in self.executeQuery(PragmaString)]
        return Types

    def GenerateInsertStatement(self, TableName: str):
        pass

    def Insert(self, InsertArguments: str):
        pass

    def SelectionCritera(self, SelectionQuery: str):
        pass


A = QSqlDatabase.addDatabase("QSQLITE")
A.setDatabaseName("projects.db")
A.open()
B = QCustomQuery("", A)
B.ObtainColoumnTypes("Admission")

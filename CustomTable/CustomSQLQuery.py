from PyQt5.QtSql import QSqlQuery, QSqlDatabase


class QCustomQuery(QSqlQuery):
    def __init__(self, db=QSqlDatabase()):
        super().__init__(db=db)

    def ExecuteQuery(self, Query) -> list:
        self.exec_(Query)
        Result = []
        while self.next():
            CurrentRow = []
            for x in range(self.record().count()):
                CurrentRow.append(self.value(x))
            Result.append(CurrentRow)
        return Result

    def ObtainColoumnTypes(self, TableName: str) -> list:
        PragmaString = """PRAGMA table_info({})""".format(TableName)
        Result = [x[2] for x in self.ExecuteQuery(PragmaString)]
        return Result

    def GenerateInsertStatement(self, TableName: str) -> str:
        pass

    def Insert(self, InsertArguments: str) -> bool:
        pass


A = QSqlDatabase.addDatabase("QSQLITE")
A.setDatabaseName("projects.db")
A.open()
B = QCustomQuery()
B.ObtainColoumnTypes("Admission")

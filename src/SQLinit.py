from PyQt5.QtSql import QSqlDatabase

import pathlib


def SQLinit(db: QSqlDatabase):
    query = ""
    with open(str(pathlib.Path(__file__).parent) + "/SQL/Village.sql", "r") as filea:
        query = filea.read()
    for x in query.split(";"):
        db.exec_(x)

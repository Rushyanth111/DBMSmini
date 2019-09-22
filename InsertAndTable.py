from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtSql import QSqlDatabase

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape, letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table as rTable
from reportlab.platypus.tables import TableStyle

from CustomSQLQuery import QCustomQuery
from FormDialog import FormDialog
from TableView import Table


class InsertAndTable(QWidget):
    def __init__(
        self,
        Tablename: str,
        FeildForm: dict,
        database: QSqlDatabase,
        InsertQuery: str,
        parent=None,
    ):
        super().__init__(parent=parent)
        self.Tablename = Tablename
        self.database = database
        self.FeildForm = FeildForm
        self.setInsertAndLayout()
        self.InsertQuery = InsertQuery

    def setInsertAndLayout(self):
        layout = QVBoxLayout(self)

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        button = QPushButton("Input Data", self)
        button2 = QPushButton("Delete")
        button3 = QPushButton("Printer!")

        button.clicked.connect(self.InsertShow)
        button2.clicked.connect(self.DeleteRow)
        button3.clicked.connect(self.Print)
        self.table = Table("projects.db", self.Tablename, self.database, self)

        layout1.addWidget(button)
        layout1.addWidget(button2)
        layout1.addWidget(button3)
        layout2.addWidget(self.table)
        layout.addLayout(layout1)
        layout.addLayout(layout2)

    def InsertShow(self):
        FormButton = FormDialog(self.Tablename, self.FeildForm, self)
        result = FormButton.exec_()
        if result == True:
            if self.InsertQuery != "":
                CorrectedResponses = []
                for x in FormButton.GetAllFeildResponses():
                    if x == '':
                        CorrectedResponses.append('NULL')
                    else:
                        CorrectedResponses.append(x)
                ExecQuery = self.InsertQuery.format(*CorrectedResponses)
                print(self.InsertQuery.format(*CorrectedResponses))
                result = self.database.exec_(ExecQuery)
                print(self.database.lastError().text())
                self.table.refresh()

    def DeleteRow(self):
        self.table.model.removeRow(self.table.currentIndex().row())
        self.table.refresh()

    def Print(self):
        Records = QCustomQuery(
            "Select * FROM " + self.Tablename, self.database
        ).GetAllRecords()
        AllCols = [
            [
                x[1]
                for x in QCustomQuery(
                    "PRAGMA table_info({})".format(self.Tablename), self.database
                ).GetAllRecords()
            ]
        ]

        NewList = []

        for x in AllCols:
            NewList.append(x)
        for x in Records:
            NewList.append(x)
        print(NewList)
        cm = 2.54
        elements = []
        doc = SimpleDocTemplate(
            "Out.pdf",
            rightMargin=0,
            leftMargin=6 * cm,
            topMargin=3 * cm,
            bottomMargin=0,
            hAlign="LEFT",
            pagesize=landscape(A4),
        )
        table = rTable(NewList, hAlign="LEFT")
        table.setStyle(
            TableStyle(
                [
                    ("ALIGN", (0, 0), (-1, -1), "RIGHT"),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                    ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
                ]
            )
        )
        elements.append(table)
        doc.build(elements)

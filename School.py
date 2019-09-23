from PyQt5.QtWidgets import (
    QVBoxLayout,
    QTabWidget,
    QWidget,
    QTableView,
    QDialog,
    QMainWindow,
    QPushButton,
    QGroupBox,
    QFormLayout,
    QLabel,
    QLineEdit,
    QDialogButtonBox,
    QHBoxLayout,
)
from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtPrintSupport import QPrintDialog
from FormDialog import FormDialog, Feilds, FeildSpecify
from TableView import Table


class School(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setInternalCategory()

    def setInternalCategory(self):
        layout = QVBoxLayout(self)
        tabs = self.makeInternalTabs()
        layout.addWidget(tabs)

        self.setLayout(layout)

    def makeInternalTabs(self):
        tabs1 = QTabWidget(self)
        tabs2 = QTabWidget(self)
        tabs = QTabWidget(self)

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("projects.db")
        db.open()

        tab_Attendance = InsertAndTable(
            "Attendance", {
                "AdmissionNo.": FieldSpecify(Fields.Int, True),
                "Name": FeildSpecify(Feilds.Text),
                "English": FeildSpecify(Feilds.Text),
                "Kannada": FeildSpecify(Feilds.Text),
                "Mathematics": FeildSpecify(Feilds.Text),
                "EVS": FeildSpecify(Feilds.Text),
                "Science": FeildSpecify(Feilds.Text),
                "Social Science": FeildSpecify(Feilds.Text),

            },
            db,
            """INSERT INTO Stationary VALUES({},'{}','{}','{}','{}','{}','{}','{}')""",
            self,
        )
        tabs.addTab(tab_Admission, "Attendance")

        tab_MidDay = InsertAndTable(
            "MidDay", {
                "AdmissionNo.": FieldSpecify(Fields.Int, True),
                "Name": FeildSpecify(Feilds.Text),
                "Quantity": FieldSpecify(Fields.Int, True),

            },
            db,
            """INSERT INTO Stationary VALUES({},'{}',{})""",
            self,
        )
        tabs.addTab(tab_Admission, "MidDay")


        tab_Stationary = InsertAndTable(
            "Stationary", {
                "AdmissionNo.": FieldSpecify(Fields.Int, True),
                "Name": FeildSpecify(Feilds.Text),
                "Books": FeildSpecify(Feilds.Text),
                "Uniform": FeildSpecify(Feilds.Text),
                "Stationary": FeildSpecify(Feilds.Text),
                "Remarks": FeildSpecify(Feilds.Text),
            },
            db,
            """INSERT INTO Stationary VALUES({},'{}','{}','{}','{}','{}')""",
            self,
        )
        tabs.addTab(tab_Admission, "Stationary")

        tab_FA1 = InsertAndTable(
            "FA1", {
                "AdmissionNo.": FieldSpecify(Fields.Int, True),
                "Name": FeildSpecify(Feilds.Text),
                "English": FeildSpecify(Feilds.Int,True),
                "Kannada": FeildSpecify(Feilds.Int,True),
                "Mathematics": FeildSpecify(Feilds.Int,True),
                "EVS": FeildSpecify(Feilds.Int,True),
                "Science": FeildSpecify(Feilds.Int,True),
                "Social Science": FeildSpecify(Feilds.Int,True),

            },
            db,
            """INSERT INTO FA2 VALUES({},'{}',{},{},{},{},{},{},{})""",
            self,
        )
        tabs.addTab(tab_FA1, "FA1")

        tab_FA2 = InsertAndTable(
            "FA2", {
                "AdmissionNo.": FieldSpecify(Fields.Int, True),
                "Name": FeildSpecify(Feilds.Text),
                "Class": FeildSpecify(Feilds.Int, True),
                "English": FeildSpecify(Feilds.Int, True),
                "Kannada": FeildSpecify(Feilds.Int, True),
                "Mathematics": FeildSpecify(Feilds.Int, True),
                "EVS": FeildSpecify(Feilds.Int, True),
                "Science": FeildSpecify(Feilds.Int, True),
                "Social Science": FeildSpecify(Feilds.Int, True),

            },
            db,
            """INSERT INTO FA2 VALUES({},'{}',{},{},{},{},{},{},{})""",
            self,
        )
        tabs.addTab(tab_FA2, "FA2")

        tab_FA3 = InsertAndTable(
            "FA3", {
                "AdmissionNo.": FieldSpecify(Fields.Int, True),
                "Name": FeildSpecify(Feilds.Text),
                "Class": FeildSpecify(Feilds.Int, True),
                "English": FeildSpecify(Feilds.Int, True),
                "Kannada": FeildSpecify(Feilds.Int, True),
                "Mathematics": FeildSpecify(Feilds.Int, True),
                "EVS": FeildSpecify(Feilds.Int, True),
                "Science": FeildSpecify(Feilds.Int, True),
                "Social Science": FeildSpecify(Feilds.Int, True),

            },
            db,
            """INSERT INTO FA3 VALUES({},'{}',{},{},{},{},{},{},{})""",
            self,
        )
        tabs.addTab(tab_FA3, "FA3")

        tab_FA4 = InsertAndTable(
            "FA4", {
                "AdmissionNo.": FieldSpecify(Fields.Int, True),
                "Name": FeildSpecify(Feilds.Text),
                "Class": FeildSpecify(Feilds.Int, True),
                "English": FeildSpecify(Feilds.Int, True),
                "Kannada": FeildSpecify(Feilds.Int, True),
                "Mathematics": FeildSpecify(Feilds.Int, True),
                "EVS": FeildSpecify(Feilds.Int, True),
                "Science": FeildSpecify(Feilds.Int, True),
                "Social Science": FeildSpecify(Feilds.Int, True),

            },
            db,
            """INSERT INTO FA4 VALUES({},'{}',{},{},{},{},{},{},{})""",
            self,
        )
        tabs.addTab(tab_FA4, "FA4")

        tab_SA1 = InsertAndTable(
            "SA1", {
                "AdmissionNo.": FieldSpecify(Fields.Int, True),
                "Name": FeildSpecify(Feilds.Text),
                "Class": FeildSpecify(Feilds.Int, True),
                "English": FeildSpecify(Feilds.Int, True),
                "Kannada": FeildSpecify(Feilds.Int, True),
                "Mathematics": FeildSpecify(Feilds.Int, True),
                "EVS": FeildSpecify(Feilds.Int, True),
                "Science": FeildSpecify(Feilds.Int, True),
                "Social Science": FeildSpecify(Feilds.Int, True),

            },
            db,
            """INSERT INTO SA1 VALUES({},'{}',{},{},{},{},{},{},{})""",
            self,
        )
        tabs.addTab(tab_SA1, "SA1")

        tab_SA2 = InsertAndTable(
            "SA2", {
                "AdmissionNo.": FieldSpecify(Fields.Int, True),
                "Name": FeildSpecify(Feilds.Text),
                "Class": FeildSpecify(Feilds.Int, True),
                "English": FeildSpecify(Feilds.Int, True),
                "Kannada": FeildSpecify(Feilds.Int, True),
                "Mathematics": FeildSpecify(Feilds.Int, True),
                "EVS": FeildSpecify(Feilds.Int, True),
                "Science": FeildSpecify(Feilds.Int, True),
                "Social Science": FeildSpecify(Feilds.Int, True),

            },
            db,
            """INSERT INTO SA2 VALUES({},'{}',{},{},{},{},{},{},{})""",
            self,
        )
        tabs.addTab(tab_SA2, "SA2")

        tabs1.addTab(tab_Attendance, "Attendance")
        tabs1.addTab(tab_MidDay, "MidDay")
        tabs1.addTab(tab_Stationary, "Stationary")
        tabs2.addTab(tab_FA1, "FA1")
        tabs2.addTab(tab_FA2, "FA2")
        tabs2.addTab(tab_FA3, "FA3")
        tabs2.addTab(tab_FA4, "FA4")
        tabs2.addTab(tab_SA1, "SA1")
        tabs2.addTab(tab_SA1, "SA2")

        tabs.addTab(tabs1, "Part 1");
        tabs.addTab(tabs2, "Part 2");
        return tabs


class InsertAndTable(QWidget):
    def __init__(self, Tablename, FeildForm, database, InsertQuery, parent=None):
        super().__init__(parent=parent)
        self.Tablename = Tablename
        self.database = database
        self.FeildForm = FeildForm
        self.setInsertAndLayout()
        self.InsertQuery = InsertQuery

    def setInsertAndLayout(self):
        layout = QVBoxLayout(self)

        layout1 = QHBoxLayout();
        layout2 = QVBoxLayout();
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
        layout.addLayout(layout1);
        layout.addLayout(layout2);

    def InsertShow(self):
        FormButton = FormDialog(self.Tablename, self.FeildForm, self)
        result = FormButton.exec_()
        if result == True:
            if self.InsertQuery != "":
                ExecQuery = self.InsertQuery.format(*FormButton.GetAllFeildResponses())
                result = self.database.exec_(ExecQuery)
                self.table.refresh()

    def DeleteRow(self):
        self.table.model.removeRow(self.table.currentIndex().row())
        self.table.refresh()

    def Print(self):
        Page = QPrintDialog(self)
        Page.exec_();
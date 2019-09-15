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
)
from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

from FormDialog import FormDialog, Feilds, FeildSpecify
from TableView import Table


class Anganwadi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setInternalCategory()

    def setInternalCategory(self):
        layout = QVBoxLayout(self)
        tabs = self.makeInternalTabs()
        layout.addWidget(tabs)

        self.setLayout(layout)

    def makeInternalTabs(self):
        tabs = QTabWidget(self)

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("projects.db")
        db.open()
        tab_child = InsertAndTable(
            "Child",
            {
                "ID": FeildSpecify(Feilds.Text, True),
                "Aadhar_Number": FeildSpecify(Feilds.Integer),
                "Name": FeildSpecify(Feilds.Text),
                "DOB": FeildSpecify(Feilds.Date),
                "Mother's Name": FeildSpecify(Feilds.Text),
                "Mother_ID": FeildSpecify(Feilds.Real),
                "Father_Name": FeildSpecify(Feilds.Text),
                "Father_ID": FeildSpecify(Feilds.Text),
                "Address": FeildSpecify(Feilds.Range, Range=["1", "2", "3", "4", "5"]),
            },
            db,
            self,
        )

        tab_Vaccination = InsertAndTable(
            "Vaccination", 
            {
                 "Child's Name" : FeildSpecify(Feilds.Text),
                 "Gender" : FeildSpecify(Fields.Range, Range=["Male", "Female"]),
                 "DOB" : FeildSpecify(Feilds.Date),
                 "Registration Date" : FeildSpecify(Feilds.Date),
                 "Polio" : FeildSpecify(Feilds.Date),
                 "Hepatitis-0" : FeildSpecify(Feilds.Date),
                 "BCG" : FeildSpecify(Feilds.Date),
                 "DPT-1" : FeildSpecify(Feilds.Date),
                 "Hepatitis-1" : FeildSpecify(Feilds.Date),
                 "OPV" : FeildSpecify(Feilds.Date),
                 "DPT-2" : FeildSpecify(Feilds.Date),
                 "Hepatitis-2" : FeildSpecify(Feilds.Date),
                 "OPV-2" : FeildSpecify(Feilds.Date),
                 "DPT-3" : FeildSpecify(Feilds.Date),
                 "Hepatitis-3" : FeildSpecify(Feilds.Date),
                 "OPV-3" : FeildSpecify(Feilds.Date), 
                 "++MMR-1" : FeildSpecify(Feilds.Date),
                 "+ life dose 1 " : FeildSpecify(Feilds.Date),
                 "DPT Booster" : FeildSpecify(Feilds.Date),
                 "++MMR-2" : FeildSpecify(Feilds.Date),
                 "Survived first Birth" : FeildSpecify(Feilds.Date)
                }
        )

        tab_Child_Health = InsertAndTable(
            "Child's Health",
            {
                "No." : FeildSpecify(Feilds.Real),
                "Child's Name" : FeildSpecify(Feilds.Text),
                "Father's Name" : FeildSpecify(Feilds.Text),
                "Mother's Name" : FeildSpecify(Feilds.Text),
                "DOB" : FeildSpecify(Feilds.Date),
                "Weight" : FeildSpecify(Feilds.Range, Range["N","M","S"]),
            }
        )

        tab_Pregnant_Ladies = InsertAndTable(
            "Pregnant Ladies",
            {
                "Sl. No." : FeildSpecify(Feilds.Integer),
                "Survey No." : FeildSpecify(Feilds.Integer),
                "Name" : FeildSpecify(Feilds.Text),
                "Pregnant/Post-Delivery ?" : FeildSpecify(Feilds.Range, Range=["Pregnant", "Post-Delivery"]),
                "Date" : FeildSpecify(Feilds.Date),
                "Signature" :FeildSpecify(Feilds.Text),
            }
        )


        tabs.addTab(tab_child, "Child")

        tab_Admission = InsertAndTable(
            "Admission",
            {
                "No.": FeildSpecify(Feilds.Integer, True),
                "SurveyNo": FeildSpecify(Feilds.Integer, True),
                "Name": FeildSpecify(Feilds.Text),
                "FatherName": FeildSpecify(Feilds.Text),
                "MotherName": FeildSpecify(Feilds.Text),
                "DOB": FeildSpecify(Feilds.Text),
                "Caste": FeildSpecify(Feilds.Text),
                "RegisterDate": FeildSpecify(Feilds.Text),
                "Weight": FeildSpecify(Feilds.Text),
                "DateOfSomething": FeildSpecify(Feilds.Text),
                "Doctor'sName": FeildSpecify(Feilds.Text),
                "Officer": FeildSpecify(Feilds.Text),
                "Signature": FeildSpecify(Feilds.Text),
                "Address": FeildSpecify(Feilds.Text),
            },
            db,
            self,
        )
        tabs.addTab(tab_Admission, "Admission")

        tab_BirthRegister = InsertAndTable(
            "BirthRegister",
            {
                "SNo.": FeildSpecify(Feilds.Integer, True),
                "Name": FeildSpecify(Feilds.Text),
                "FatherName": FeildSpecify(Feilds.Text),
                "NoOfSiblings": FeildSpecify(Feilds.Integer),
                "DeliveryDate": FeildSpecify(Feilds.Text),
                "PlaceOfBirth": FeildSpecify(Feilds.Text),
                "MethodOfBirth": FeildSpecify(Feilds.Text),
                "Weight": FeildSpecify(Feilds.Text),

            },
            db,
            self,
        )
        tabs.addTab(tab_BirthRegister, "BirthRegister")


        tab_PTM = InsertAndTable(
            "PTM",
            {
                "SNo.": FeildSpecify(Feilds.Integer, True),
                "Name": FeildSpecify(Feilds.Text),
                "Guardian'sName": FeildSpecify(Feilds.Text),
                "Discussion": FeildSpecify(Feilds.Text),
            },
            db,
            self,
        )
        tabs.addTab(tab_PTM, "PTM")


        return tabs


class InsertAndTable(QWidget):
    def __init__(self, Tablename, FeildForm, database, parent=None):
        super().__init__(parent=parent)
        self.Tablename = Tablename
        self.database = database
        self.FeildForm = FeildForm
        self.setInsertAndLayout()

    def setInsertAndLayout(self):
        layout = QVBoxLayout(self)
        button = QPushButton("Start", self)
        button.clicked.connect(self.InsertShow)

        table = Table("projects.db", self.Tablename, self.database, self)


        layout.addWidget(button)
        layout.addWidget(table)

    def InsertShow(self):
        FormButton = FormDialog(self.Tablename, self.FeildForm, self)
        result = FormButton.exec_()
        if result == True:
            print("Accepted")
            print(FormButton.GetAllFeildResponses())
        else:
            print("Rejected")


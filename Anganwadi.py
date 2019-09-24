from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtGui import QPainter
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QTabWidget, QVBoxLayout, QWidget

from FormDialog import Feilds, FeildSpecify
from InsertAndTable import InsertAndTable
from SQLinit import SQLinit
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table as rTable,TableStyle
from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors


from FormDialog import FormDialog, Feilds, FeildSpecify
from TableView import Table
from CustomSQLQuery import QCustomQuery

#from import DataFrame



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
        tabs1 = QTabWidget(self)
        tabs2 = QTabWidget(self)
        tabs = QTabWidget(self)

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("projects.db")
        db.open()
        SQLinit(db)
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
            """INSERT INTO CHILD VALUES('{}',{},'{}','{}','{}','{}','{}','{}','{}')""",
            self,
        )
        tab_daily = InsertAndTable(
            "DailyFood",
            {
                "Sl.No": FeildSpecify(Feilds.Integer, True),
                "Name(Child)": FeildSpecify(Feilds.Text),
                "Wheat(Kgs)": FeildSpecify(Feilds.Real),
                "Sugar(gms)": FeildSpecify(Feilds.Integer),
                "Jaggery(gms)": FeildSpecify(Feilds.Integer),
                "Milk(gms)": FeildSpecify(Feilds.Integer),
                "Nutrient Mix(gms)": FeildSpecify(Feilds.Integer),
                "Pulses(gms)": FeildSpecify(Feilds.Integer),
                "Height": FeildSpecify(Feilds.Integer),
                "Weight": FeildSpecify(Feilds.Integer),
                "Signature": FeildSpecify(Feilds.Text),
            },
            db,
            """INSERT INTO DailyFood VALUES({},'{}',{},{},{},{},{},{},{},{},'{}')""",
            self,
        )
        tab_family = InsertAndTable(
            "Family",
            {
                "Sl No.": FeildSpecify(Feilds.Integer, True),
                "Survey No": FeildSpecify(Feilds.Integer),
                "Name": FeildSpecify(Feilds.Text),
                "Relation With Head": FeildSpecify(Feilds.Text),
                "Gender": FeildSpecify(Feilds.Range, Range=["Male", "Female"]),
                "Marital Status": FeildSpecify(Feilds.Range, Range=["Yes", "No"]),
                "Date of Birth": FeildSpecify(Feilds.Date),
                "Age": FeildSpecify(Feilds.Integer),
                "Mothers Name(If child les than 6 Years)": FeildSpecify(Feilds.Text),
                "Physical Disabilities": FeildSpecify(
                    Feilds.Range, Range=["","Blind"]
                ),
                "Residence of Anganwadi?": FeildSpecify(
                    Feilds.Range, Range=["Yes", "No"]
                ),
                "Native of Marsandra?": FeildSpecify(Feilds.Range, Range=["Yes", "No"]),
                "Date of Arrival": FeildSpecify(Feilds.Date),
                "Date of Death": FeildSpecify(Feilds.Date),
                "If Child, Has Lunch in School ": FeildSpecify(
                    Feilds.Range, Range=["Yes", "No"]
                ),
            },
            db,
            """INSERT INTO Family VALUES({},{},'{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','')""",
            self,
        )
        tab_Vaccination = InsertAndTable(
            "Vaccination",
            {
                "Child's Name": FeildSpecify(Feilds.Text),
                "Gender": FeildSpecify(Feilds.Range, Range=["Male", "Female"]),
                "DOB": FeildSpecify(Feilds.Date),
                "Registration Date": FeildSpecify(Feilds.Date),
                "Polio": FeildSpecify(Feilds.Date),
                "Hepatitis-0": FeildSpecify(Feilds.Date),
                "BCG": FeildSpecify(Feilds.Date),
                "DPT-1": FeildSpecify(Feilds.Date),
                "Hepatitis-1": FeildSpecify(Feilds.Date),
                "OPV": FeildSpecify(Feilds.Date),
                "DPT-2": FeildSpecify(Feilds.Date),
                "Hepatitis-2": FeildSpecify(Feilds.Date),
                "OPV-2": FeildSpecify(Feilds.Date),
                "DPT-3": FeildSpecify(Feilds.Date),
                "Hepatitis-3": FeildSpecify(Feilds.Date),
                "OPV-3": FeildSpecify(Feilds.Date),
                "++MMR-1": FeildSpecify(Feilds.Date),
                "+ life dose 1 ": FeildSpecify(Feilds.Date),
                "DPT Booster": FeildSpecify(Feilds.Date),
                "++MMR-2": FeildSpecify(Feilds.Date),
                "Survived first Birth": FeildSpecify(Feilds.Date),
            },
            db,
            """INSERT INTO VACCINATION VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""",
            self,
        )

        tab_Child_Health = InsertAndTable(
            "CHILD_HEALTH",
            {
                "No.": FeildSpecify(Feilds.Real),
                "Child's Name": FeildSpecify(Feilds.Text),
                "Father's Name": FeildSpecify(Feilds.Text),
                "Mother's Name": FeildSpecify(Feilds.Text),
                "DOB": FeildSpecify(Feilds.Date),
                "Weight": FeildSpecify(Feilds.Range, Range=["N", "M", "S"]),
            },
            db,
            """INSERT INTO CHILD_HEALTH VALUES({},{},'{}','{}','{}','{}')""",
            self,
        )

        tab_Pregnant_Ladies = InsertAndTable(
            "PREGNANT_LADIES",
            {
                "Sl. No.": FeildSpecify(Feilds.Integer),
                "Survey No.": FeildSpecify(Feilds.Integer),
                "Name": FeildSpecify(Feilds.Text),
                "Pregnant/Post-Delivery ?": FeildSpecify(
                    Feilds.Range, Range=["Pregnant", "Post-Delivery"]
                ),
                "Date": FeildSpecify(Feilds.Date),
                "Signature": FeildSpecify(Feilds.Text),
            },
            db,
            """INSERT INTO PREGNANT_LADIES VALUES({},{},'{}','{}','{}','{}')""",
            self,
        )

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
                "Weight": FeildSpecify(Feilds.Real),
                "DateOfArrival": FeildSpecify(Feilds.Text),
                "Doctor'sName": FeildSpecify(Feilds.Text),
                "OfficerSignature": FeildSpecify(Feilds.Text),
                "Signature": FeildSpecify(Feilds.Text),
                "Address": FeildSpecify(Feilds.Text),
            },
            db,
            """INSERT INTO Admission VALUES({},{},'{}','{}','{}','{}','{}','{}',{}.,'{}','{}','{}','{}','{}')""",
            self,
        )

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
            """INSERT INTO BirthRegister VALUES({},'{}','{}',{},'{}','{}','{}',{})""",
            self,
        )

        tab_PTM = InsertAndTable(
            "PTM",
            {
                "SNo.": FeildSpecify(Feilds.Integer, True),
                "Name": FeildSpecify(Feilds.Text),
                "Guardian'sName": FeildSpecify(Feilds.Text),
                "Discussion": FeildSpecify(Feilds.Text),
            },
            db,
            """INSERT INTO PTM VALUES({},'{}','{}','{}')""",
            self,
        )

        tabs1.addTab(tab_PTM, "PTM")
        tabs1.addTab(tab_BirthRegister, "Birth Register")
        tabs1.addTab(tab_Admission, "Admission")
        tabs1.addTab(tab_child, "Child")
        tabs1.addTab(tab_daily, "Daily Food")
        tabs2.addTab(tab_family, "Family Census")
        tabs2.addTab(tab_Vaccination, "Vaccination")
        tabs2.addTab(tab_Child_Health, "Child Health")
        tabs2.addTab(tab_Pregnant_Ladies, "Pregnant Ladies.")
        tabs.addTab(tabs1,"Part 1")
        tabs.addTab(tabs2, "Part 2")
        return tabs

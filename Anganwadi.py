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
                "ID": FeildSpecify(Feilds.Text),
                "Aadhar_Number": FeildSpecify(Feilds.Text),
                "Name": FeildSpecify(Feilds.Text),
                "DOB": FeildSpecify(Feilds.Text),
                "Mother's Name": FeildSpecify(Feilds.Text),
                "Mother_ID": FeildSpecify(Feilds.Text),
                "Father_Name": FeildSpecify(Feilds.Text),
                "Father_ID": FeildSpecify(Feilds.Text),
                "Address": FeildSpecify(Feilds.Text),
            },
            db,
            self,
        )
        tab_mother = InsertAndTable(
            "Mother",
            {
                "ID": FeildSpecify(Feilds.Text),
                "Aadhar_Number": FeildSpecify(Feilds.Text),
                "Name": FeildSpecify(Feilds.Text),
                "DOB": FeildSpecify(Feilds.Text),
                "Height": FeildSpecify(Feilds.Text),
                "Weight": FeildSpecify(Feilds.Text),
                "Date_of_registration": FeildSpecify(Feilds.Text),
                "Address": FeildSpecify(Feilds.Text),
            },
            db,
            self,
        )
        tab_father = InsertAndTable(
            "Father",
            {
                "ID": FeildSpecify(Feilds.Text),
                "Aadhar_Number": FeildSpecify(Feilds.Text),
                "Name": FeildSpecify(Feilds.Text),
                "DOB": FeildSpecify(Feilds.Text),
                "Height": FeildSpecify(Feilds.Text),
                "Weight": FeildSpecify(Feilds.Text),
                "Date_of_registration": FeildSpecify(Feilds.Text),
                "Address": FeildSpecify(Feilds.Text),
            },
            db,
            self,
        )
        tab_vaccine = InsertAndTable(
            "Vacccine",
            {
                "Vaccine_ID": FeildSpecify(Feilds.Text),
                "Vaccine_Name": FeildSpecify(Feilds.Text),
                "Stock_available": FeildSpecify(Feilds.Text),
                "Date_of_Supply": FeildSpecify(Feilds.Text),
                "Expiry_Date": FeildSpecify(Feilds.Text),
                "Additional_Details": FeildSpecify(Feilds.Text),
            },
            db,
            self,
        )
        tab_vaccination = InsertAndTable(
            "Vaccination",
            {
                "Name": FeildSpecify(Feilds.Text),
                "Recipient_ID": FeildSpecify(Feilds.Text),
                "Vaccine_ID": FeildSpecify(Feilds.Text),
                "Date_of_Vaccination": FeildSpecify(Feilds.Text),
            },
            db,
            self,
        )
        tab_childHealth = InsertAndTable(
            "Child_Health",
            {
                "ID": FeildSpecify(Feilds.Text),
                "Name": FeildSpecify(Feilds.Text),
                "Date_of_checkup": FeildSpecify(Feilds.Text),
                "Height": FeildSpecify(Feilds.Text),
                "Weight": FeildSpecify(Feilds.Text),
                "Remarks": FeildSpecify(Feilds.Text),
            },
            db,
            self,
        )
        tab_motherHealth = InsertAndTable(
            "Mother_Health",
            {
                "ID": FeildSpecify(Feilds.Text),
                "Name": FeildSpecify(Feilds.Text),
                "Date_of_checkup": FeildSpecify(Feilds.Text),
                "Height": FeildSpecify(Feilds.Text),
                "Weight": FeildSpecify(Feilds.Text),
                "Remarks": FeildSpecify(Feilds.Text),
            },
            db,
            self,
        )

        tabs.addTab(tab_child, "Child")
        tabs.addTab(tab_mother, "Mother")
        tabs.addTab(tab_father, "Father")
        tabs.addTab(tab_vaccine, "Vaccine")
        tabs.addTab(tab_vaccination, "Vaccination")
        tabs.addTab(tab_childHealth, "Child_Health")
        tabs.addTab(tab_motherHealth, "Mother_Health")

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
        FormButton.exec_()
        print(FormButton.GetAllFeildResponses())


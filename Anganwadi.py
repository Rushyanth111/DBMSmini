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

from FormDialog import FormDialog
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
        tab_child = InsertAndTable("Child",["ID", "Aadhar_Number","Name","DOB","Mother's Name", "Mother_ID","Father_Name","Father_ID","Address"],db,self)
        tab_mother = InsertAndTable("Mother",["ID","Aadhar_Number","Name","DOB","Height","Weight","Date_of_registration", "Address"],db,self)
        tab_father = InsertAndTable("Father",["ID","Aadhar_Number","Name","DOB","Height","Weight","Date_of_registration", "Address"],db,self)
        tab_vaccine = InsertAndTable("Vacccine",["Vaccine_ID","Vaccine_Name","Stock_available", "Date_of_Supply","Expiry_Date", "Additional_Details"],db,self)
        tab_vaccination = InsertAndTable("Vaccination",["Name","Recipient_ID","Vaccine_ID", "Date_of_Vaccination"],db,self)
        tab_childHealth = InsertAndTable("Child Health",["ID", "Name","Date_of_checkup","Height", "Weight","Remarks"],db,self)
        tab_motherHealth = InsertAndTable("Mother Health", ["ID","Name","Date_of_checkup", "Height", "Weight","Remarks"],db,self)
        
        tabs.addTab(tab_child, "Child")
        tabs.addTab(tab_mother, "Mother")
        tabs.addTab(tab_father, "Father")
        tabs.addTab(tab_vaccine, "Vaccine")
        tabs.addTab(tab_vaccination, "Vaccination")
        tabs.addTab(tab_childHealth, "Child_Health")
        tabs.addTab(tab_motherHealth, "Mother_Health")

        return tabs


class InsertAndTable(QWidget):
    def __init__(self, db_name, db_arr, database, parent=None):
        super().__init__(parent=parent)
        self.db_name = db_name
        self.db_arr = db_arr
        self.database = database
        self.setInsertAndLayout()


    def setInsertAndLayout(self):
        layout = QVBoxLayout(self)
        button = QPushButton("Start", self)
        button.clicked.connect(self.InsertShow)

        table = Table("projects.db","Sample",self.database,self)

        layout.addWidget(button)
        layout.addWidget(table)

    def InsertShow(self):
        FormButton = FormDialog(self.db_name,self.db_arr, self)
        FormButton.exec_()
        print(FormButton.GetAllFeildResponses())


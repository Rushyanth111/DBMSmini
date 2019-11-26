"""[summary]
"""
import pathlib

from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QTabWidget, QVBoxLayout, QWidget

from CentralDisplay import Central
from SQLinit import SQLinit

from Tabs import PTM


class Anganwadi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        layout = QVBoxLayout(self)
        tabs = self.__set_tabs__()
        layout.addWidget(tabs)

        self.setLayout(layout)

    def __set_tabs__(self):
        tabs = QTabWidget(self)

        # Initalizing SQL Database:
        database = QSqlDatabase.addDatabase("QSQLITE")
        database.setDatabaseName(
            pathlib.Path(__file__).parent.__str__() + "/DB/data.db"
        )
        database.open()
        SQLinit(database)

        # Tabs
        tab_person = Central("person", "name", "Text", self)
        tab_family = Central("family", "family_id", "Integer", self)
        tab_survey = Central("survey", "survey_id", "Integer", self)
        tab_student = Central("student", "person_id", "Integer", self)
        tab_hospital = Central("hospital", "name", "Text", self)
        tab_doctor = Central("doctor", "name", "Text", self)
        tab_person_birth = Central("person_birth", "place", "Text", self)
        tab_vacc = Central("vaccination", "person_id", "Integer")

        tabs.addTab(tab_person, "PTM")
        tabs.addTab(tab_family, "Family")
        tabs.addTab(tab_survey, "Survey")
        tabs.addTab(tab_student, "Student")
        tabs.addTab(tab_hospital, "Hospital")
        tabs.addTab(tab_doctor, "Doctor")
        tabs.addTab(tab_hospital, "Hospitals")
        tabs.addTab(tab_person_birth, "Birth")
        tabs.addTab(tab_vacc, "Vaccianation")
        return tabs

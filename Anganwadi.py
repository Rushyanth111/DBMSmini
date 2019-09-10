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

        tab1 = InsertAndTable(self)
        tab2 = QWidget()

        tabs.addTab(tab1, "Category")
        tabs.addTab(tab2, "Category")

        return tabs


class InsertAndTable(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setInsertAndLayout()

    def setInsertAndLayout(self):
        layout = QVBoxLayout(self)
        button = QPushButton("Start", self)
        button.clicked.connect(self.InsertShow)

        table = Table("projects.db","Sample",self)

        layout.addWidget(button)
        layout.addWidget(table)

    def InsertShow(self):
        FormButton = FormDialog("Input FOOOORM", ["A", "B", "C"], self)
        FormButton.exec_()
        print(FormButton.GetAllFeildResponses())


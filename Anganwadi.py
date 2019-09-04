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
    QDialogButtonBox
)
from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


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

        table = Table(self)

        layout.addWidget(button)
        layout.addWidget(table)

    def InsertShow(self):
        FormButton = InsertFormButton(self)
        FormButton.exec_();
        print(FormButton.QL1.text())
        print(FormButton.QL2.text())
        print(FormButton.QL3.text())

class InsertFormButton(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        self.setWindowTitle("InputForm!")
        form = self.CreateForm();

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout();
        layout.addWidget(form);
        layout.addWidget(buttonBox);

        self.setLayout(layout);

    def CreateForm(self):
        formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        self.QL1 = QLineEdit();
        self.QL2 = QLineEdit();
        self.QL3 = QLineEdit();
        layout.addRow(QLabel("Name:"), self.QL1)
        layout.addRow(QLabel("Country:"), self.QL2)
        layout.addRow(QLabel("Age:"), self.QL3)
        formGroupBox.setLayout(layout)

        return formGroupBox


class Table(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.createTable()

    def createTable(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("projects.db")
        db.open()

        model = QSqlTableModel(self, db)
        model.setTable("Sample")
        model.select()
        self.setModel(model)

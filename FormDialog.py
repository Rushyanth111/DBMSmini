from PyQt5.QtWidgets import (
    QDialog,
    QFormLayout,
    QLabel,
    QLineEdit,
    QDialogButtonBox,
    QVBoxLayout,
    QGroupBox,
    QMessageBox,
    QDateEdit,
    QComboBox,
)

from PyQt5.QtGui import QIntValidator, QDoubleValidator

from enum import Enum


class Feilds(Enum):
    Integer = 0
    Text = 1
    Date = 2
    Real = 3
    Range = 4


def FeildSpecify(Feild: Feilds, NotNull: bool = False, Range: list = []):
    return [Feild, NotNull, Range]


def YNRange():
    return ["Y", "N"]


class FormDialog(QDialog):
    def __init__(self, formName, FeildDict=None, parent=None):
        super().__init__(parent=parent)

        self.FeildDict = FeildDict
        self.Responses = []

        form = self.CreateForm()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # Connect the ButtonBoxes to Various Things.
        buttonBox.accepted.connect(self.Accept)
        buttonBox.rejected.connect(self.reject)

        # Set the Widgets to the layouts.
        layout = QVBoxLayout()
        layout.addWidget(form)
        layout.addWidget(buttonBox)

        self.setWindowTitle(formName)
        self.setLayout(layout)

    def CreateForm(self):
        formGroupBox = QGroupBox("Form layout")

        layout = QFormLayout()

        self.LineEditArray = []

        keys = list(self.FeildDict.keys())

        for x in range(len(keys)):
            if self.FeildDict[keys[x]][0] == Feilds.Text:
                Box = QLineEdit(self)
                Box.textChanged.connect(self.NoteText)

            elif self.FeildDict[keys[x]][0] == Feilds.Date:
                Box = QDateEdit(self)
                Box.dateChanged.connect(self.NoteText)

            elif self.FeildDict[keys[x]][0] == Feilds.Integer:
                Box = QLineEdit(self)
                Box.setValidator(QIntValidator(0, 999999, self))
                Box.textChanged.connect(self.NoteText)

            elif self.FeildDict[keys[x]][0] == Feilds.Real:
                Box = QLineEdit(self)
                Box.setValidator(QDoubleValidator(0.0, 999999.0, 2, self))
                Box.textChanged.connect(self.NoteText)

            else:
                Box = QComboBox(self)
                RangeFeilds = self.FeildDict[keys[x]][2]
                Box.addItems(RangeFeilds)
                Box.activated.connect(self.NoteText)

            self.LineEditArray.append(Box)
            self.Responses.append("")

        for x in range(len(keys)):
            layout.addRow(QLabel(keys[x]), self.LineEditArray[x])

        formGroupBox.setLayout(layout)
        return formGroupBox

    def GetAllFeildResponses(self):
        return self.Responses

    def NoteText(self):
        keys = list(self.FeildDict.keys())
        for x in range(len(self.Responses)):
            if (
                self.FeildDict[keys[x]][0] == Feilds.Integer
                or self.FeildDict[keys[x]][0] == Feilds.Real
                or self.FeildDict[keys[x]][0] == Feilds.Text
            ):
                self.Responses[x] = self.LineEditArray[x].text()
            elif self.FeildDict[keys[x]][0] == Feilds.Range:
                self.Responses[x] = self.LineEditArray[x].currentText()
            else:
                self.Responses[x] = (
                    self.LineEditArray[x].date().toPyDate().strftime("%Y-%m-%d")
                )

    # Custom Accept Function.
    # Validate All Input Chosen.
    def Accept(self):
        self.NoteText()
        AllTestsPass = True
        keys = list(self.FeildDict.keys())
        for x in range(len(self.Responses)):
            if self.FeildDict[keys[x]][1] is True and self.Responses[x] == "":
                Q = QMessageBox()
                Q.setIcon(QMessageBox.Critical)
                Q.setStandardButtons(QMessageBox.Ok)
                Q.setWindowTitle("Bad Value!")
                Q.setText("The Value Left out was: " + keys[x])
                Q.setDetailedText(
                    "You need to fill in the information else this cannot be accepted."
                )
                Q.exec_()
                AllTestsPass = False
                break
        if AllTestsPass is True:
            self.accept()

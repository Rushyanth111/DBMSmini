from PyQt5.QtWidgets import (
    QDialog,
    QFormLayout,
    QLabel,
    QLineEdit,
    QDialogButtonBox,
    QVBoxLayout,
    QGroupBox,
)

from enum import Enum


class Feilds(Enum):
    Integer = 0
    Text = 1
    Date = 2
    Real = 3
    Nill = 4
    Blob = 5


def FeildSpecify(Feild: Feilds, NotNull: bool = False, Range: list = []):
    return [Feild, NotNull, Range]


class FormDialog(QDialog):
    def __init__(self, formName, FeildDict=None, parent=None):
        super().__init__(parent=parent)

        ###self.Feilds = FeildNames
        ##Set the FormName.
        self.setWindowTitle(formName)

        self.FeildDict = FeildDict

        form = self.CreateForm()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        ##Connect the ButtonBoxes to Various Things.
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        ##Set the Widgets to the layouts.
        layout = QVBoxLayout()
        layout.addWidget(form)
        layout.addWidget(buttonBox)

        self.setLayout(layout)

    def CreateForm(self):
        formGroupBox = QGroupBox("Form layout")
        if self.FeildDict is None:
            layout = QFormLayout()

            self.LineEditArray = []

            for x in self.Feilds:
                self.LineEditArray.append(QLineEdit())

            for x in range(len(self.LineEditArray)):
                layout.addRow(QLabel(self.Feilds[x]), self.LineEditArray[x])

            formGroupBox.setLayout(layout)
        else:
            print("Using Feild Dict")
            layout = QFormLayout()

            self.LineEditArray = []

            keys = list(self.FeildDict.keys())
            print(keys)

            for x in range(len(keys)):
                self.LineEditArray.append(QLineEdit())

            for x in range(len(keys)):
                layout.addRow(QLabel(keys[x]), self.LineEditArray[x])

            formGroupBox.setLayout(layout)
        return formGroupBox

    def GetAllFeildResponses(self):
        Responses = []
        for x in self.LineEditArray:
            Responses.append(x.text())

        return Responses

    # Custom Accept Function.
    def Accept(self):
        Q = QDialog(self)
        Q.setWindowTitle("Something Else!")
        Q.exec_()
        self.accept()

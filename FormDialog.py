from PyQt5.QtWidgets import (
    QDialog,
    QFormLayout,
    QLabel,
    QLineEdit,
    QDialogButtonBox,
    QVBoxLayout,
    QGroupBox,
    QPushButton,
    QMessageBox
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

        self.FeildDict = FeildDict
        self.Responses = []; 

        form = self.CreateForm()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        ##Connect the ButtonBoxes to Various Things.
        buttonBox.accepted.connect(self.Accept)
        buttonBox.rejected.connect(self.reject)

        ##Set the Widgets to the layouts.
        layout = QVBoxLayout()
        layout.addWidget(form)
        layout.addWidget(buttonBox)

        self.setWindowTitle(formName)
        self.setLayout(layout)

    def CreateForm(self):
        formGroupBox = QGroupBox("Form layout")

        print("Using Feild Dict")
        layout = QFormLayout()

        self.LineEditArray = []

        keys = list(self.FeildDict.keys())
        print(keys)

        for x in range(len(keys)):
            Box = QLineEdit();
            Box.textChanged.connect(self.NoteText)
            self.LineEditArray.append(Box)
            self.Responses.append("");

        for x in range(len(keys)):
            layout.addRow(QLabel(keys[x]), self.LineEditArray[x])

        formGroupBox.setLayout(layout)
        return formGroupBox

    def GetAllFeildResponses(self):

        return self.Responses


    def NoteText(self):
        for x in range(len(self.Responses)):
            self.Responses[x] = self.LineEditArray[x].text();
    
    # Custom Accept Function.
    def Accept(self):
        print(self.Responses)
        AllTestsPass = False;
        for x in self.LineEditArray:
            if(x.text() == ""):
                Q = QMessageBox();
                Q.setIcon(QMessageBox.Critical);
                Q.setStandardButtons(QMessageBox.Ok);
                Q.setWindowTitle("BBBB")
                Q.setText("AAA");
                Q.setDetailedText("More Additional Information.")
                Q.exec_();
                break;
        if AllTestsPass == True:
            self.accept();

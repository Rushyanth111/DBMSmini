from PyQt5.QtWidgets import (
    QDialog,
    QFormLayout,
    QLabel,
    QLineEdit,
    QDialogButtonBox,
    QVBoxLayout,
    QGroupBox,
)


class FormDialog(QDialog):
    def __init__(self, formName, FeildNames, parent=None):
        super().__init__(parent=parent)

        self.Feilds = FeildNames
        ##Set the FormName.
        self.setWindowTitle(formName)
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
        layout = QFormLayout()

        self.LineEditArray = []

        for x in self.Feilds:
            self.LineEditArray.append(QLineEdit())

        for x in range(len(self.LineEditArray)):
            layout.addRow(QLabel(self.Feilds[x]), self.LineEditArray[x])

        formGroupBox.setLayout(layout)

        return formGroupBox

    def GetAllFeildResponses(self):
        Responses = []
        for x in self.LineEditArray:
            Responses.append(x.text())
        
        return Responses;

    # Custom Accept Function.
    def Accept(self):
        Q = QDialog(self)
        Q.setWindowTitle("Something Else!")
        Q.exec_()
        self.accept()

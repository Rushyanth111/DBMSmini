from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QTextEdit, QDateEdit
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from typing import Union


class QVarFeild(QWidget):
    def __init__(self, ftype: str, prim: str, parent=None):
        super().__init__(parent=parent)

        self.input_line: Union[QLineEdit, QTextEdit, QDateEdit]
        self.__empty_allowed__ = True
        self.ftype = ftype
        self.prim = prim

        if ftype == "Integer":
            self.input_line = QLineEdit()
            self.input_line.setValidator(QIntValidator())
        elif ftype == "Float":
            self.input_line = QLineEdit()
            self.input_line.setValidator(QDoubleValidator())
        elif ftype == "Date":
            self.input_line = QDateEdit()
        elif ftype == "Text":
            self.input_line = QLineEdit()
        else:  # Large Text
            self.input_line = QTextEdit()

        if prim == 1:
            self.__empty_allowed__ = False

        layout = QVBoxLayout(self)
        layout.addWidget(self.input_line)
        self.setLayout(layout)

    def text(self):
        return self.input_line.text()

    def setDataText(self, data):
        if self.ftype == "Date":
            self.input_line.setDate(self.input_line.dateTimeFromText(str(data)))
        else:
            self.input_line.setText(str(data))

from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QLabel
from PyQt5.QtGui import QIntValidator, QDoubleValidator


class FilterView(QDialog):
    def __init__(self, col_name, col_type, parent=None):
        super().__init__(parent=parent)

        layout = QFormLayout()

        self.edit_box = QLineEdit()

        if col_type == "Integer":
            self.edit_box.setValidator(QIntValidator())
        elif col_type == "Float":
            self.edit_box.setValidator(QDoubleValidator())

        label = QLabel(col_name)

        layout.addRow(label, self.edit_box)

        self.setLayout(layout)

    def text(self):
        return self.edit_box.text()


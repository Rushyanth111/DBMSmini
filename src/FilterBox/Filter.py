from PyQt5.QtWidgets import QDialog, QFormLayout, QLineEdit, QLabel, QDateEdit, QDialogButtonBox
from PyQt5.QtGui import QIntValidator, QDoubleValidator


class FilterView(QDialog):
    def __init__(self, col_name, col_type, parent=None):
        super().__init__(parent=parent)

        layout = QFormLayout()

        self.where_string = ""
        self.col_name = col_name
        self.edit_box = QLineEdit()

        if col_type == "Integer":
            self.edit_box.setValidator(QIntValidator())
            self.where_string = "{} = {}"
        elif col_type == "Float":
            self.edit_box.setValidator(QDoubleValidator())
            self.where_string = "{} = {}"
        elif col_type == "Date":
            self.edit_box = QDateEdit()
            self.where_string = "{} >= {}"
        else:
            self.where_string = "{} LIKE '{}'"

        label = QLabel(col_name)

        layout.addRow(label, self.edit_box)
        ok_cancel_options = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        ok_cancel_options.accepted.connect(self.accept)
        ok_cancel_options.rejected.connect(self.reject)
        layout.addWidget(ok_cancel_options)
        self.setLayout(layout)

    def where_text(self):
        return self.where_string.format(self.col_name, self.edit_box.text())


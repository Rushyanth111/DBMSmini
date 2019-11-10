from typing import List

from PyQt5.QtWidgets import (
    QComboBox,
    QDateEdit,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QMessageBox,
    QVBoxLayout,
)


class InsertDialog(QDialog):
    def __init__(self, form_names: List[str], form_types: List[str], parent):
        super().__init__(parent=parent)

        self.__names__ = form_names
        self.__form_types = form_types

        form = self.__create_form__()
        ok_cancel_options = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        layout = QVBoxLayout()
        layout.addWidget(form)
        layout.addWidget(ok_cancel_options)

        self.setWindowTitle("Insert Table.")
        self.setLayout(layout)

    def __create_form__(self):
        from_group = QGroupBox("SS")

        layout = QFormLayout()

        for itr, item in enumerate(self.__names__):
            layout.addRow(QLabel(item), QLineEdit(self))

        from_group.setLayout(layout)

        return from_group

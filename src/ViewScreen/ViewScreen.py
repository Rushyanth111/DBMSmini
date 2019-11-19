from PyQt5.QtWidgets import QDialog, QFormLayout, QLabel
from PyQt5.QtGui import QFont
from typing import List


class ViewScreen(QDialog):
    def __init__(self, col_name: List[str], col_value: List[str], parent=None):
        super().__init__(parent=parent)

        layout = QFormLayout()
        for name, val in zip(col_name, col_value):
            box = QLabel(str(name) + " : " + str(val))
            box.setFont(QFont("Segoe UI",20))
            layout.addRow(box)

        self.setLayout(layout)
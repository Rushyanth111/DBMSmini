from typing import List

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QFormLayout, QHBoxLayout, QLabel


class ViewScreen(QDialog):
    def __init__(self, col_name: List[str], col_value: List[str], parent=None):
        super().__init__(parent=parent)

        layout_name = QFormLayout()
        layout_colon = QFormLayout()
        layout_val = QFormLayout()

        layout = QHBoxLayout()
        for val in col_name:
            box = QLabel(str(val))
            box.setFont(QFont("Segoe UI", 10))
            box.setUnde
            layout_name.addRow(box)

        for val in col_name:
            box = QLabel(":")
            box.setFont(QFont("Segoe UI", 10))
            layout_colon.addRow(box)


        for val in col_value:
            box = QLabel(str(val))
            box.setFont(QFont("Segoe UI", 10))
            box.setAlignment(Qt.AlignLeft)
            box.setWordWrap(True)
            layout_val.addRow(box)


        layout.addLayout(layout_name)
        layout.addLayout(layout_colon)
        layout.addLayout(layout_val)

        self.setLayout(layout)

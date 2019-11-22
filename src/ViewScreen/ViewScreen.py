from typing import List

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QFormLayout, QHBoxLayout, QLabel

from pylatex import Tabular, Document
class ViewScreen(QDialog):
    def __init__(self, col_name: List[str], col_value: List[str], parent=None):
        super().__init__(parent=parent)

        doc = Document()

        with doc.create(Tabular('rc|cl')) as table:
            table.add_hline()
            table.add_row((1,2,3,4))
            
        doc.generate_pdf()
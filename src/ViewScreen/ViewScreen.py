import os
from typing import List

import tex2pix
from pdf2image import convert_from_path
from pylatex import Command, Document, Tabular
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QDialog, QFormLayout, QHBoxLayout, QLabel


class ViewScreen(QDialog):
    def __init__(self, col_name: List[str], col_value: List[str], parent=None):
        super().__init__(parent=parent)

        doc = Document()
        doc.documentclass = Command(
            "documentclass", options=["preview=true"], arguments=["standalone"]
        )
        with doc.create(Tabular("r|p{5cm}")) as table:
            for name, val in zip(col_name, col_value):
                table.add_hline()
                table.add_row((name, val))

        doc.generate_pdf(filepath="./ViewScreen")

        pages = convert_from_path("ViewScreen.pdf")
        for page in pages:
            page.save("ViewScreen.jpg", "JPEG")

        layout = QHBoxLayout(self)
        label = QLabel(self)
        label.setPixmap(QPixmap("ViewScreen.jpg"))
        layout.addWidget(label)

        self.setLayout(layout)

        os.remove('ViewScreen.jpg')
        os.remove('ViewScreen.pdf')

from pylatex import Table, Document, Tabular, Command
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtCore import QUrl


def PrintToPDF(col_names, cols):
    doc = Document()

    rstring = "|"
    for _ in range(len(col_names)):
        rstring += "r|"

    with doc.create(Tabular(rstring)) as table:
        table.add_hline()
        table.add_row(col_names)
        table.add_hline()
        for col in cols:
            table.add_row(col)
            table.add_hline()

    filestr = QFileDialog.getSaveFileName(None, "&Save File", "", "PDF (*.pdf)")[0]

    doc.generate_pdf(filepath=filestr)

"""[summary]
"""

from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import (
    QDialogButtonBox,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from CustomTable import Table
from InsertDialog import InsertDialog
from ViewScreen import ViewScreen

from .ActionButtons import ActionButtons
import qtmodern.windows


class Central(QWidget):
    def __init__(self, Tablename: str, parent=None):
        super().__init__(parent=parent)
        self.Tablename = Tablename
        self.database = QSqlDatabase()
        self.__set_layout__()

    def __set_layout__(self):
        layout = QVBoxLayout(self)
        boxx = ActionButtons(
            {
                "InputData": self.__insert_show__,
                "Delete": self.__delete_row__,
                "Update": self.__update_menu__,
                "Show in Window": self.__view_menu__,
                "Filter By": self.__filter_window__,
                "Reset Filter": self.__reset_filter__,
                "Export to PDF": self.__pdf__,
            }
        )
        self.table = Table(self.Tablename, self)

        layout.addWidget(boxx)
        layout.addWidget(self.table)
        # layout.addWidget(button_test)

    def __insert_show__(self):
        # Form Button Holds the data even after exec_(),
        # use that incase of error
        form = InsertDialog(
            self.table.get_col_names(),
            self.table.get_col_types(),
            self.table.get_col_prim(),
            self,
        )
        
        form_result = form.exec_()
        if form_result:
            insert_result = self.table.insert_into_table(*form.get_input())

        while form_result and not insert_result:
            # form_result has to be true and insert result has to be false
            warn = QMessageBox()

            warn.setIcon(QMessageBox.Critical)
            warn.setStandardButtons(QMessageBox.Ok)
            warn.setWindowTitle("Error")
            warn.setText(self.table.get_last_error())
            warn.setDetailedText(self.table.__last__error__)

            warn.exec_()
            form_result = form.exec_()
            insert_result = self.table.insert_into_table(*form.get_input())

    def __delete_row__(self):
        self.table.__model__.removeRow(self.table.currentIndex().row())
        self.table.refresh()

    def __pdf__(self):
        pass

    def __view_menu__(self):
        S = ViewScreen(self.table.get_col_names(), self.table.get_row_selected())
        S = qtmodern.windows.ModernWindow(S)
        S.show()

    def __update_menu__(self):
        form = InsertDialog(
            self.table.get_col_names(),
            self.table.get_col_types(),
            self.table.get_col_prim(),
            self,
            self.table.get_row_selected(),
        )

        form_result = form.exec_()

        if form_result:
            insert_result = self.table.update(*form.get_input())

        while form_result and not insert_result:
            # form_result has to be true and insert result has to be false
            warn = QMessageBox()

            warn.setIcon(QMessageBox.Critical)
            warn.setStandardButtons(QMessageBox.Ok)
            warn.setWindowTitle("Error")
            warn.setText(self.table.get_last_error())
            warn.setDetailedText(self.table.__last__error__)

            warn.exec_()
            form_result = form.exec_()
            insert_result = self.table.update(*form.get_input())

    # Implemented in it's own initalization.

    def __filter_window__(self):
        pass

    def __reset_filter__(self):
        pass

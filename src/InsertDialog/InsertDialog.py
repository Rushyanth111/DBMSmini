from typing import List, Any

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

from .Feild import QVarFeild

from itertools import zip_longest


class InsertDialog(QDialog):
    def __init__(
        self,
        form_names: List[str],
        form_types: List[str],
        form_prim_keys: List[int],
        parent,
        prev_data=[],
    ):
        super().__init__(parent=parent)

        self.__names__ = form_names
        self.__types__ = form_types
        self.__accept_status__ = False
        self.__primary__ = form_prim_keys
        self.__prev_data__ = prev_data
        self.__resulted_data_raw__: List[QLineEdit] = []
        self.__result_data__: List[str] = []
        

        form = self.__create_form__()
        ok_cancel_options = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        ok_cancel_options.accepted.connect(self.__custom_accept__)
        ok_cancel_options.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(form)
        layout.addWidget(ok_cancel_options)

        self.setFixedWidth(400)
        self.setWindowTitle("Insert Table.")
        self.setLayout(layout)

    def __create_form__(self):
        from_group = QGroupBox("SS")

        layout = QFormLayout()
        for (name, ftype, prim, pdata) in zip_longest(
            self.__names__, self.__types__, self.__primary__, self.__prev_data__
        ):
            edit_line = QVarFeild(ftype, prim)
            if pdata is not None:
                edit_line.setDataText(pdata)
            self.__resulted_data_raw__.append(edit_line)
            layout.addRow(QLabel(name), edit_line)

        from_group.setLayout(layout)

        return from_group

    def __custom_accept__(self):
        res = []
        for item in self.__resulted_data_raw__:
            res.append(item.text())
        self.__result_data__ = res
        self.__accept_status__ = True
        self.accept()

    def get_input(self) -> List[Any]:
        """Returns the data from the form

        Returns:
            List[Any] -- Data in List Form
        """
        return self.__result_data__

    def is_accepted(self):
        return self.__accept_status__


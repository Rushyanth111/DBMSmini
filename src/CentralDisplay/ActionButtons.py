from PyQt5.QtWidgets import QWidget, QDialogButtonBox, QPushButton, QHBoxLayout

from typing import Dict, Callable


class ActionButtons(QWidget):
    def __init__(self, action_dict: Dict, parent=None):
        super().__init__(parent=parent)
        self.__action_dict__: dict = action_dict

        layout = QHBoxLayout()
        buttons = QDialogButtonBox(self)
        for key, val in self.__action_dict__.items():
            button = QPushButton(key)
            button.clicked.connect(val)
            buttons.addButton(button, QDialogButtonBox.ActionRole)

        layout.addWidget(buttons)
        self.setLayout(layout)

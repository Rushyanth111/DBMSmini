from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QSizePolicy,
)


class QLogin(QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("self")

        self.__set_font__()
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.__set_text__())
        main_layout.addLayout(self.__set_username__())
        main_layout.addLayout(self.__set_password__())
        main_layout.addWidget(self.__set_button_accept__())

        self.setLayout(main_layout)

    def __set_text__(self):
        text_layout = QHBoxLayout()
        text_layout.setAlignment(Qt.AlignHCenter)
        welcome = QLabel("Login")
        welcome.setFont(QFont("Segoe UI Black", 14, 20))
        welcome.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        text_layout.addWidget(welcome)

        return text_layout

    def __set_username__(self):
        u_layout = QHBoxLayout()

        self.username = QLineEdit(self)
        self.username.setText("")
        self.username.setPlaceholderText("")
        self.username.setClearButtonEnabled(True)
        self.username.setObjectName("lineEdit")
        self.username.editingFinished.connect(self.__handle_username__)

        label = QLabel("Username:", self)
        label.setTextFormat(Qt.RichText)
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignLeft)
        label.setObjectName("label")

        u_layout.addWidget(label)
        u_layout.addWidget(self.username)

        return u_layout

    def __set_password__(self):
        p_layout = QHBoxLayout()

        self.password = QLineEdit(self)
        self.password.setPlaceholderText("")
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName("lineEdit_2")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.editingFinished.connect(self.__handle_password__)

        label_2 = QLabel("Password:", self)
        label_2.setTextFormat(Qt.RichText)
        label_2.setScaledContents(True)
        label_2.setAlignment(Qt.AlignLeft)
        label_2.setObjectName("label_2")

        p_layout.addWidget(label_2)
        p_layout.addWidget(self.password)

        return p_layout

    def __set_button_accept__(self):
        confirm_reject_box = QDialogButtonBox(self)
        confirm_reject_box.setOrientation(Qt.Horizontal)
        confirm_reject_box.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok
        )
        confirm_reject_box.setObjectName("buttonBox")
        confirm_reject_box.accepted.connect(self.accept)
        confirm_reject_box.rejected.connect(self.reject)

        return confirm_reject_box

    def __set_font__(self):
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)

    def __auth__(self):
        pass

    def __handle_username__(self):
        print(self.username.text())

    def __handle_password__(self):
        print(self.password.text())

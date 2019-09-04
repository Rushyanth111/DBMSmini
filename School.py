from PyQt5.QtWidgets import QVBoxLayout, QTabWidget, QWidget

class School(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setInternalCategory()

    def setInternalCategory(self):
        layout = QVBoxLayout(self)
        tabs = self.makeInternalTabs()
        layout.addWidget(tabs)

        self.setLayout(layout)

    def makeInternalTabs(self):
        tabs = QTabWidget(self)

        tab1 = QWidget()
        tab2 = QWidget()

        tabs.addTab(tab1, "AAA")
        tabs.addTab(tab2, "BBB")

        return tabs


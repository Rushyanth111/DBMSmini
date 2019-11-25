"""Custom Class Extending Features of the Central Table:
"""

from CentralDisplay import Central
from FilterBox import FilterView


class PTM(Central):
    def __init__(self, parent=None):
        super().__init__("PTM", parent=parent)

    def __filter_by__(self):
        fil = FilterView("SNo", "Integer", self)

        fil.exec_()

        self.table.__filter__("Sno LIKE {}".format(fil.text()))

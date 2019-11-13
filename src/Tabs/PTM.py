"""Custom Class Extending Features of the Central Table:
"""

from CentralTable import Central


class PTM(Central):
    def __init__(self, parent=None):
        super().__init__("PTM", parent=parent)

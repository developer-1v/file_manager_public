from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class OrgSubAccess(QWidget):
    def __init__(self):
        super().__init__()
        self.name = "Organizational Sub Access"
        self.initUI()

    def initUI(self):
        self.setToolTip(self.name)
        # layout = QVBoxLayout()
        # self.setLayout(layout)
        label = QLabel(self.name, self)
        # layout.addWidget(label)
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class Properties(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.name = "Properties"
        self.initUI()

    def initUI(self):
        self.setToolTip(self.name)
        # layout = QVBoxLayout()
        # self.setLayout(layout)
        label = QLabel("Properties", self)
        # layout.addWidget(label)
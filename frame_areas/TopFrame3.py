from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class TopFrame3(QWidget):
    def __init__(self, parent, style="Background: transparent;"):
        super().__init__(parent)
        self.name = "Top Frame 3"
        self.initUI()

    def initUI(self):
        self.setToolTip(self.name)
        # layout = QVBoxLayout()
        # self.setLayout(layout)
        label = QLabel(self.name, self)
        # layout.addWidget(label)
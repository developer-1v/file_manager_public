from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class CommandBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.name = "Command Bar"
        self.initUI()
        

    def initUI(self):
        self.setToolTip(self.name)
        # layout = QVBoxLayout()
        # self.setLayout(layout)
        label = QLabel(self.name, self)
        # layout.addWidget(label)
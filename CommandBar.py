from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class CommandBar(QWidget):
    print('----blah')
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ...
        # layout = QVBoxLayout()
        # self.setLayout(layout)
        label = QLabel("Command Bar", self)
        print('--2')
        # layout.addWidget(label)
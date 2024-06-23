from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class CommandBar(QWidget):
    print('----blah')
    def __init__(self):
        super().__init__()
        self.name = "Command Bar"
        self.initUI()
        

    def initUI(self):
        self.setToolTip(self.name)
        # layout = QVBoxLayout()
        # self.setLayout(layout)
        label = QLabel(self.name, self)
        print('--2')
        # layout.addWidget(label)
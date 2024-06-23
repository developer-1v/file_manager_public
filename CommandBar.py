from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class CommandBar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # layout = QVBoxLayout()
        # self.setLayout(layout)
        label = QLabel("Command Bar", self)
        # layout.addWidget(label)
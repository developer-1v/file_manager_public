from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class TopFrame4(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # layout = QVBoxLayout()
        # self.setLayout(layout)
        label = QLabel("Top Frame 4", self)
        # layout.addWidget(label)
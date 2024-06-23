from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class TopFrame3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # layout = QVBoxLayout()
        # self.setLayout(layout)
        label = QLabel("Top Frame 3", self)
        # layout.addWidget(label)
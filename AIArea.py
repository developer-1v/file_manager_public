from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class AIArea(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # layout = QVBoxLayout()
        # self.setLayout(layout)
        label = QLabel("AI Area", self)
        # layout.addWidget(label)
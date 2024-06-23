from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class SearchArea(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # layout = QVBoxLayout()
        # self.setLayout(layout)
        label = QLabel("Search Frame", self)
        # layout.addWidget(label)
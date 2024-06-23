from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class OrgSubAccess(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # layout = QVBoxLayout()
        # self.setLayout(layout)
        label = QLabel("Organizational Sub Access", self)
        # layout.addWidget(label)
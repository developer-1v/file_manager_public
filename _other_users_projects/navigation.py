

class Navigation(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        label = QLabel("Navigation", self)
        layout.addWidget(label)


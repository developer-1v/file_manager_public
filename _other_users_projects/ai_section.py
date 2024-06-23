

class AISection(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        label = QLabel("Extra 1", self)
        layout.addWidget(label)


class SubNavigation(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        label = QLabel("Sub Navigation", self)
        layout.addWidget(label)
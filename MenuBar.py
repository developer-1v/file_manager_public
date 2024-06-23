from PySide6.QtWidgets import QMenuBar

class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()
        self.name = "Menu Bar"
        self.setToolTip(self.name)
        self.addMenu("File")
        self.addMenu("Edit")
        self.addMenu("View")
        self.addMenu("Help")
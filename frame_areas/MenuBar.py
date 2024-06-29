from PySide6.QtWidgets import QMenuBar

class MenuBar(QMenuBar):
    def __init__(self, parent, style="Background: transparent;"):
        super().__init__(parent)
        self.name = "Menu Bar"
        self.setToolTip(self.name)
        self.addMenu("File")
        self.addMenu("Edit")
        self.addMenu("View")
        self.addMenu("Help")
        self.setStyleSheet(style)
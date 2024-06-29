from PySide6.QtWidgets import QMenuBar

class MenuBar(QMenuBar):
    def __init__(self, parent=None):  # Add parent parameter with default value
        super().__init__(parent)  # Pass parent to the superclass constructor
        self.name = "Menu Bar"
        self.setToolTip(self.name)
        self.addMenu("File")
        self.addMenu("Edit")
        self.addMenu("View")
        self.addMenu("Help")
        self.setStyleSheet("""
            QMenuBar {
                background-color: #333;
                color: #D8DEE9;
            }
            QMenuBar::item {
                background-color: #333;
                color: #D8DEE9;
            }
            QMenuBar::item:selected {
                background-color: #555;
                color: #D8DEE9;
            }
            QMenu {
                background-color: #333;
                color: #D8DEE9;
            }
            QMenu::item:selected {
                background-color: #555;
                color: #D8DEE9;
            }
        """)
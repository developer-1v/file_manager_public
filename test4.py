from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QMenuBar, QStatusBar
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window Example")
        self.setGeometry(100, 100, 800, 600)

        # Central widget
        central_widget = QWidget()
        central_layout = QVBoxLayout(central_widget)
        central_layout.addWidget(QLabel("This is the central widget"))
        self.setCentralWidget(central_widget)

        # Menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        exit_action = QAction("Exit", self)
        file_menu.addAction(exit_action)

        # Status bar
        # status_bar = self.statusBar()
        # status_bar.showMessage("Ready")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
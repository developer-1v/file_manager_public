import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtAxContainer import QAxWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Embedded File Explorer")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create the ActiveX widget
        self.ax_widget = QAxWidget("{8856F961-340A-11D0-A96B-00C04FD705A2}")
        layout.addWidget(self.ax_widget)

        # Navigate to the desired folder (optional)
        self.ax_widget.dynamicCall("Navigate(const QString&)", "C:\\")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
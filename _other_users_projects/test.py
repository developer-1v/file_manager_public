from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QListWidget, QFrame, QVBoxLayout
import sys
import os

class FileExplorerApp(QWidget):
    def __init__(self, rows=1, columns=4):
        super().__init__()
        self.initUI(rows, columns)

    def initUI(self, rows, columns):
        # Set the window title and size
        self.setWindowTitle('Configurable Grid File Explorer')
        self.setGeometry(100, 100, 800, 600)

        # Create a grid layout
        grid = QGridLayout()
        self.setLayout(grid)

        # Add buttons at the top
        top_frame = QFrame(self)
        top_layout = QVBoxLayout()
        top_frame.setLayout(top_layout)
        btn = QPushButton('Click Me', top_frame)
        top_layout.addWidget(btn)
        grid.addWidget(top_frame, 0, 0, 1, columns)  # Span all columns

        # Create file explorer frames based on the specified grid
        for r in range(1, rows + 1):
            for c in range(columns):
                frame = QFrame(self)
                frame_layout = QVBoxLayout()
                frame.setLayout(frame_layout)
                listbox = QListWidget(frame)
                self.populate_listbox(listbox)
                frame_layout.addWidget(listbox)
                grid.addWidget(frame, r, c)

    def populate_listbox(self, listbox):
        # Populate the listbox with the contents of the root directory
        for item in os.listdir('/'):
            listbox.addItem(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileExplorerApp(2, 3)
    ex.show()
    sys.exit(app.exec_())
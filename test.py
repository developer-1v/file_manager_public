from print_tricks import pt

















''' Right Click Context Menu '''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget, QMenu, QFileSystemModel
from PySide6.QtCore import Qt

class FileManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced File Manager")

        # Set up the file system model
        self.model = QFileSystemModel()
        self.model.setRootPath('')

        # Set up the tree view
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(''))
        self.tree.setDragEnabled(True)
        self.tree.setAcceptDrops(True)
        self.tree.setDropIndicatorShown(True)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.tree)

        # Set up the central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Connect context menu
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.open_context_menu)

    def open_context_menu(self, position):
        indexes = self.tree.selectedIndexes()
        if indexes:
            menu = QMenu()
            menu.addAction("Open")
            menu.addAction("Copy")
            menu.addAction("Paste")
            menu.addAction("Delete")
            menu.exec(self.tree.viewport().mapToGlobal(position))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        context_menu.addAction("Open")
        context_menu.addAction("Copy")
        context_menu.addAction("Paste")
        context_menu.addAction("Delete")
        context_menu.exec(event.globalPos())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileManager()
    window.show()
    sys.exit(app.exec())














from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTreeView, QHBoxLayout, QPushButton, QLineEdit, QApplication, QFileSystemModel
from PySide6.QtCore import Qt, QDir, QEvent, QTimer, QModelIndex, QSortFilterProxyModel
from PySide6.QtGui import QIcon
import os
import sys

class SortingModel(QSortFilterProxyModel):
    def lessThan(self, source_left: QModelIndex, source_right: QModelIndex):
        file_info1 = self.sourceModel().fileInfo(source_left)
        file_info2 = self.sourceModel().fileInfo(source_right)       
        
        if file_info1.fileName() == "..":
            return self.sortOrder() == Qt.SortOrder.AscendingOrder

        if file_info2.fileName() == "..":
            return self.sortOrder() == Qt.SortOrder.DescendingOrder
                
        if (file_info1.isDir() and file_info2.isDir()) or (file_info1.isFile() and file_info2.isFile()):
            return super().lessThan(source_left, source_right)

        return file_info1.isDir() and self.sortOrder() == Qt.SortOrder.AscendingOrder

class FileExplorer(QWidget):
    def __init__(self, parent, style="Background: transparent;"):
        super().__init__(parent)
        self.name = "File Explorer"
        self.current_path = os.path.expanduser('~')
        self.history = []
        self.history_index = -1
        self.path_display_had_focus = False  # Initialize the focus flag

        self.initUI()

    def initUI(self):
        self.setToolTip(self.name)
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Navigation bar
        nav_layout = QHBoxLayout()
        self.back_button = QPushButton('<')
        self.back_button.setFixedSize(30, 30)
        self.back_button.clicked.connect(self.go_back)
        self.forward_button = QPushButton('>')
        self.forward_button.setFixedSize(30, 30)
        self.forward_button.clicked.connect(self.go_forward)
        self.up_button = QPushButton('↑')
        self.up_button.setFixedSize(30, 30)
        self.up_button.clicked.connect(self.go_up)
        
        self.path_display = QLineEdit(self.current_path)
        self.path_display.setReadOnly(False)  # Allow editing
        self.path_display.setToolTip(self.current_path)  # Set tooltip to display full path
        self.path_display.installEventFilter(self)  # Install event filter for custom behavior
        
        nav_layout.addWidget(self.back_button)
        nav_layout.addWidget(self.forward_button)
        nav_layout.addWidget(self.up_button)
        nav_layout.addWidget(self.path_display)
        main_layout.addLayout(nav_layout)

        # File tree view
        self.tree_view = QTreeView(self)
        self.model = QFileSystemModel()
        self.model.setRootPath(self.current_path)
        self.model.setFilter(QDir.NoDotAndDotDot | QDir.AllEntries)  # Change filter to exclude ".."
        self.model.sort(0, Qt.SortOrder.AscendingOrder)
        
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(self.current_path))
        self.tree_view.header().setSortIndicator(0, Qt.AscendingOrder)
        self.tree_view.setSortingEnabled(True)
        # self.tree_view.selectionModel().selectionChanged.connect(self.update_path_display)
        self.tree_view.doubleClicked.connect(self.change_directory)
        
        main_layout.addWidget(self.tree_view)

    # def update_path_display(self, selected, deselected):
    #     indexes = selected.indexes()
    #     self.update_path()
    #     if indexes:
    #         new_path = self.model.filePath(indexes[0])
    #         self.path_display.setText(new_path)
    #         self.path_display.setToolTip(new_path)
    #         self.current_path = new_path

    def change_directory(self, index):
        new_path = self.model.filePath(index)
        if os.path.isdir(new_path):
            self.current_path = new_path
            self.update_path()

    def update_path(self, dont_add_to_history=False):
        if not dont_add_to_history:
            if self.history_index == -1 or self.history[self.history_index] != self.current_path:
                self.history = self.history[:self.history_index + 1]
                self.history.append(self.current_path)
                self.history_index += 1
        self.path_display.setText(os.path.abspath(self.current_path))
        self.path_display.setToolTip(self.current_path)  # Update tooltip with new path
        self.tree_view.setRootIndex(self.model.index(self.current_path))

    def go_back(self):
        if self.history_index > 0:
            self.history_index -= 1
            self.current_path = self.history[self.history_index]
            self.update_path()
        else:
            self.go_up(dont_add_to_history=True)

    def go_forward(self):
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.current_path = self.history[self.history_index]
            self.update_path()

    def go_up(self, dont_add_to_history=False):
        parent_path = os.path.dirname(self.current_path)
        if self.history_index > 0:
            self.history_index -= 1
            self.current_path = parent_path
            self.update_path()
        elif parent_path != self.current_path:
            self.current_path = parent_path
            self.update_path(dont_add_to_history=dont_add_to_history)

    def eventFilter(self, source, event):
        if source == self.path_display:
            if event.type() == QEvent.MouseButtonPress:
                if not self.path_display_had_focus:
                    QTimer.singleShot(0, self.path_display.selectAll)
                    self.path_display_had_focus = True
                    return True
            elif event.type() == QEvent.FocusOut:
                self.path_display_had_focus = False
                return True
        return super().eventFilter(source, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    file_explorer = FileExplorer()
    file_explorer.resize(800, 600)
    file_explorer.show()
    sys.exit(app.exec())
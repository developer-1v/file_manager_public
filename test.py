from print_tricks import pt

import sys
import os
import ctypes
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget, QFileSystemModel
from PySide6.QtCore import Qt, QDir
import win32con
import win32api
import win32gui
import win32com.client

class FileManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced File Manager")

        # Set up the file system model
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())

        # Set up the tree view
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(QDir.rootPath()))
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
        index = self.tree.indexAt(position)
        if not index.isValid():
            return

        file_path = self.model.filePath(index)
        self.show_windows_context_menu(file_path, self.tree.viewport().mapToGlobal(position))

    def show_windows_context_menu(self, path, global_position):
        # Convert the path to a PIDL
        pidl = ctypes.windll.shell32.ILCreateFromPathW(path)
        pt(path, global_position, pidl)
        if not pidl:
            return

        # Get the parent folder's PIDL
        parent_pidl = ctypes.windll.shell32.ILClone(pidl)
        ctypes.windll.shell32.ILRemoveLastID(parent_pidl)

        # Get the IShellFolder interface for the parent folder
        shell = win32com.client.Dispatch("Shell.Application")
        parent_folder = shell.NameSpace(os.path.dirname(path))

        # Get the IContextMenu interface for the item
        item = parent_folder.ParseName(os.path.basename(path))
        context_menu = item.GetContextMenu()

        # Create a popup menu
        menu = win32gui.CreatePopupMenu()

        # Populate the menu with the context menu items
        for i in range(context_menu.Count):
            verb = context_menu.Item(i)
            if verb.Name:
                win32gui.AppendMenu(menu, win32con.MF_STRING, 1000 + i, verb.Name)

        # Display the context menu
        command = win32gui.TrackPopupMenu(menu, win32con.TPM_RETURNCMD | win32con.TPM_RIGHTBUTTON, global_position.x(), global_position.y(), 0, self.winId(), None)
        if command:
            context_menu.Item(command - 1000).DoIt()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileManager()
    window.show()
    sys.exit(app.exec())
















# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget, QMenu, QFileSystemModel
# from PySide6.QtCore import Qt

# class FileManager(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Advanced File Manager")

#         # Set up the file system model
#         self.model = QFileSystemModel()
#         self.model.setRootPath('')

#         # Set up the tree view
#         self.tree = QTreeView()
#         self.tree.setModel(self.model)
#         self.tree.setRootIndex(self.model.index(''))
#         self.tree.setDragEnabled(True)
#         self.tree.setAcceptDrops(True)
#         self.tree.setDropIndicatorShown(True)

#         # Set up the layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.tree)

#         # Set up the central widget
#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#         # Connect context menu
#         self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
#         self.tree.customContextMenuRequested.connect(self.open_context_menu)

#     def open_context_menu(self, position):
#         indexes = self.tree.selectedIndexes()
#         if indexes:
#             menu = QMenu()
#             menu.addAction("Open")
#             menu.addAction("Copy")
#             menu.addAction("Paste")
#             menu.addAction("Delete")
#             menu.exec(self.tree.viewport().mapToGlobal(position))

#     def dragEnterEvent(self, event):
#         if event.mimeData().hasUrls():
#             event.acceptProposedAction()

#     def dropEvent(self, event):
#         if event.mimeData().hasUrls():
#             event.acceptProposedAction()

#     def contextMenuEvent(self, event):
#         context_menu = QMenu(self)
#         context_menu.addAction("Open")
#         context_menu.addAction("Copy")
#         context_menu.addAction("Paste")
#         context_menu.addAction("Delete")
#         context_menu.exec(event.globalPos())

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = FileManager()
#     window.show()
#     sys.exit(app.exec())














'''

        
        
        
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

    model = QFileSystemModel()
    model.setRootPath('.')
    model.setFilter(QDir.NoDot | QDir.AllEntries)
    model.sort(0, Qt.SortOrder.AscendingOrder)
    sorting_model = SortingModel()
    sorting_model.setSourceModel(model)
    view.tree_view.setModel(sorting_model)
    view.tree_view.setRootIndex(sorting_model.mapFromSource(model.index('.')))
    view.tree_view.header().setSortIndicator(0, Qt.AscendingOrder)
    view.tree_view.setSortingEnabled(True)
    
    '''
from PySide6.QtWidgets import QMenuBar, QMenu
from PySide6.QtGui import QAction

class MenuBar(QMenuBar):
    def __init__(self, parent, style="Background: transparent;"):
        super().__init__(parent)
        self.name = "Menu Bar"
        self.setToolTip(self.name)
        
        file_menu = self.addMenu("File")
        edit_menu = self.addMenu("Edit")
        view_menu = self.addMenu("View")
        help_menu = self.addMenu("Help")
        
        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        
        undo_action = QAction("Undo", self)
        redo_action = QAction("Redo", self)
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)
        
        zoom_in_action = QAction("Zoom In", self)
        zoom_out_action = QAction("Zoom Out", self)
        view_menu.addAction(zoom_in_action)
        view_menu.addAction(zoom_out_action)
        
        about_action = QAction("About", self)
        help_menu.addAction(about_action)
        
        self.setStyleSheet(style)
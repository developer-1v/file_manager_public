from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget
from PySide6.QtCore import Qt
import os

class FileExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        listbox = QListWidget(self)
        self.populate_listbox(listbox)
        layout.addWidget(listbox)

    def populate_listbox(self, listbox):
        for item in os.listdir('/'):
            listbox.addItem(item)
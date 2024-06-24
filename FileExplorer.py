from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QHBoxLayout, QPushButton, QLineEdit, QListWidgetItem, QApplication
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QIcon
import os
import sys
from print_tricks import pt

class FileExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.name = "File Explorer"
        self.current_path = os.path.expanduser('~')
        self.history = []
        self.history_index = -1
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
        
        nav_layout.addWidget(self.back_button)
        nav_layout.addWidget(self.forward_button)
        nav_layout.addWidget(self.up_button)
        nav_layout.addWidget(self.path_display)
        main_layout.addLayout(nav_layout)

        # File list
        self.listbox = QListWidget(self)
        self.listbox.itemDoubleClicked.connect(self.change_directory)
        self.populate_listbox(self.listbox)
        main_layout.addWidget(self.listbox)

    def populate_listbox(self, listbox):
        listbox.clear()
        for item in os.listdir(self.current_path):
            item_path = os.path.join(self.current_path, item)
            list_item = QListWidgetItem(item)
            if os.path.isdir(item_path):
                list_item.setIcon(QIcon.fromTheme("folder"))
            else:
                list_item.setIcon(QIcon.fromTheme("text-x-generic"))
            listbox.addItem(list_item)

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
            pt()
            self.history_index -= 1
            self.current_path = parent_path
            self.update_path()
        elif parent_path != self.current_path:
                self.current_path = parent_path
                self.update_path(dont_add_to_history=dont_add_to_history)

    def change_directory(self, item):
        new_path = os.path.join(self.current_path, item.text())
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
        self.populate_listbox(self.listbox)

    def eventFilter(self, source, event):
        if source == self.path_display and event.type() == QEvent.MouseButtonPress:
            if not self.path_display.hasFocus():
                self.path_display.selectAll()  # Select all text on first click
            else:
                self.path_display.deselect()  # Deselect text on subsequent clicks
            return True
        return super().eventFilter(source, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    file_explorer = FileExplorer()
    file_explorer.show()
    sys.exit(app.exec())
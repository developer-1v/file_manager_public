from print_tricks import pt

import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QTreeView, QFrame, QFileSystemModel, QSizePolicy, QPushButton
from PySide6.QtWidgets import QMainWindow, QStatusBar, QMenuBar, QWidget, QVBoxLayout

class CustomVideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title_bar_height = 30
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(1111, 333, 1920, 1080)
        self.resizing = False  # Add a flag to track resizing

        self.initUI()
        self.show()

    def initUI(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.createGifLabel()
        self.createTitleBar()
        self.createAdditionalUI()
        self.createFileTreeView()
        self.createLayouts()

    def createStatusBar(self):
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

    def createMenuBar(self):
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        file_menu = self.menu_bar.addMenu("File")
        edit_menu = self.menu_bar.addMenu("Edit")
        view_menu = self.menu_bar.addMenu("View")
        help_menu = self.menu_bar.addMenu("Help")

    def createLayouts(self):
        main_layout = QVBoxLayout(self.central_widget)  # Set layout on central widget
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.gif_label)

        ui_layout = QVBoxLayout()
        ui_layout.addWidget(self.label1)
        ui_layout.addWidget(self.input1)
        ui_layout.addWidget(self.label2)
        ui_layout.addWidget(self.input2)
        ui_layout.addWidget(self.file_tree)

        self.ui_frame = QFrame(self.gif_label)
        self.ui_frame.setLayout(ui_layout)
        self.ui_frame.setStyleSheet("background: rgba(222, 222, 222, 0.7); color: #D8DEE9;")
        self.ui_frame.setGeometry(0, self.title_bar_height, 111, self.height() - self.title_bar_height + 550)



    def createGifLabel(self):
        self.gif_label = QLabel(self)
        self.movie = QMovie("lightspeed-10957.gif")
        self.gif_label.setMovie(self.movie)
        self.movie.start()
        self.gif_label.setScaledContents(True)
        self.gif_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

    def createTitleBar(self):
        self.title_bar = QFrame(self)
        self.title_bar.setStyleSheet("background: rgba(55, 55, 55, 0.8); color: #D8DEE9;")
        self.title_bar.setFixedHeight(self.title_bar_height)
        self.title_bar_layout = QHBoxLayout(self.title_bar)
        self.title_bar_layout.setContentsMargins(0, 0, 0, 0)

        self.title_label = QLabel("Custom Title Bar", self.title_bar)
        self.title_label.setAlignment(Qt.AlignCenter)

        button_style = "QPushButton { width: 30px; height: 30px; }"
        self.minimize_button = QPushButton("-", self.title_bar)
        self.minimize_button.setStyleSheet(button_style)
        self.maximize_button = QPushButton("□", self.title_bar)
        self.maximize_button.setStyleSheet(button_style)
        self.close_button = QPushButton("X", self.title_bar)
        self.close_button.setStyleSheet(button_style)

        self.title_bar_layout.addStretch()
        self.title_bar_layout.addStretch()
        self.title_bar_layout.addWidget(self.title_label)
        self.title_bar_layout.addStretch()
        self.title_bar_layout.addWidget(self.minimize_button)
        self.title_bar_layout.addWidget(self.maximize_button)
        self.title_bar_layout.addWidget(self.close_button)

        self.minimize_button.clicked.connect(self.showMinimized)
        self.maximize_button.clicked.connect(self.toggleMaximizeRestore)
        self.close_button.clicked.connect(self.close)

        self.title_bar.mousePressEvent = self.start_drag
        self.title_bar.mouseMoveEvent = self.do_drag

    def createAdditionalUI(self):
        self.label1 = QLabel("Label 1", self)
        self.label1.setStyleSheet("background-color: yellow;")
        self.label2 = QLabel("Label 2", self)
        self.label2.setStyleSheet("background-color: lightblue;")
        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)

    def createFileTreeView(self):
        self.file_tree = QTreeView(self)
        self.file_model = QFileSystemModel()
        self.file_model.setRootPath('')
        self.file_tree.setModel(self.file_model)


    def mousePressEvent(self, event):
        pt()
        if event.button() == Qt.LeftButton:
            if self.is_on_edge(event.position().toPoint()):
                self.resizing = True
                self.drag_position = event.globalPosition().toPoint()
            else:
                self.start_drag(event)

    def mouseMoveEvent(self, event):
        pt()
        if self.resizing:
            self.do_resize(event)
        else:
            if self.is_on_edge(event.position().toPoint()):
                self.setCursor(Qt.SizeFDiagCursor)
            else:
                self.setCursor(Qt.ArrowCursor)
            self.do_drag(event)

    def is_on_edge(self, pos):
        pt.every(0.3)
        margin = 10
        on_left_edge = pos.x() <= margin
        on_right_edge = pos.x() >= self.width() - margin
        on_bottom_edge = pos.y() >= self.height() - margin
        return on_left_edge or on_right_edge or on_bottom_edge

    def do_resize(self, event):
        delta = event.globalPosition().toPoint() - self.drag_position
        new_width = self.width()
        new_height = self.height()
        new_x = self.x()
        new_y = self.y()

        if self.drag_position.x() <= 10:  # Left edge
            new_width -= delta.x()
            new_x += delta.x()
        elif self.drag_position.x() >= self.width() - 10:  # Right edge
            new_width += delta.x()
        if self.drag_position.y() >= self.height() - 10:  # Bottom edge
            new_height += delta.y()

        self.setGeometry(new_x, new_y, new_width, new_height)
        self.drag_position = event.globalPosition().toPoint()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.title_bar.setGeometry(0, 0, self.width(), self.title_bar_height)
        self.title_label.setGeometry(self.width() // 2 - 100, 0, 200, self.title_bar_height)
        self.minimize_button.setGeometry(self.width() - 90, 0, 30, self.title_bar_height)
        self.maximize_button.setGeometry(self.width() - 60, 0, 30, self.title_bar_height)
        self.close_button.setGeometry(self.width() - 30, 0, 30, self.title_bar_height)
        self.ui_frame.setGeometry(0, self.title_bar_height, self.width(), self.height() - self.title_bar_height)
        self.minimize_button.setFixedSize(30, self.title_bar_height)  # Ensure fixed size
        self.maximize_button.setFixedSize(30, self.title_bar_height)  # Ensure fixed size
        self.close_button.setFixedSize(30, self.title_bar_height)  # Ensure fixed size

    def mouseReleaseEvent(self, event):
        self.resizing = False

    def start_drag(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def do_drag(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    def toggleMaximizeRestore(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

if __name__ == "__main__":
    app = QApplication([])
    player = CustomVideoPlayer()  # Updated class name
    sys.exit(app.exec())
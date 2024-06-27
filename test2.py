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
        self.button_size_percentage = 0.075  # Button size as a percentage of window width
        self.button_spacing_percentage = 0.01  # Spacing as a percentage of window width
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(1111, 333, 1920, 1080)
        self.resizing = False  # Add a flag to track resizing

        # self.setMouseTracking(True)  # Enable mouse tracking for the main window
        self.initUI()
        self.show()

    def initUI(self):
        self.central_widget = QWidget(self)
        # self.central_widget.setMouseTracking(True)  # Enable mouse tracking for the central widget
        self.setCentralWidget(self.central_widget)
        self.createGifLabel()
        self.createTitleBar()
        self.createAdditionalUI()
        self.createFileTreeView()
        self.createEdgeButtons()  # Create edge buttons
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
        # self.ui_frame.setGeometry(0, self.title_bar_height, 111, self.height() - self.title_bar_height + 550)

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
        self.reset_size_position_button = QPushButton('[]',self.title_bar)
        # self.reset_size_position_button.setIcon(QIcon("path/to/fugue/icons/appropriate_icon.png"))  # Set appropriate icon
        self.reset_size_position_button.setStyleSheet(button_style)

        self.title_bar_layout.addStretch()
        self.title_bar_layout.addWidget(self.title_label)
        self.title_bar_layout.addStretch()
        self.title_bar_layout.addWidget(self.reset_size_position_button)  # Add half size button
        self.title_bar_layout.addWidget(self.minimize_button)
        self.title_bar_layout.addWidget(self.maximize_button)
        self.title_bar_layout.addWidget(self.close_button)

        self.reset_size_position_button.clicked.connect(self.set_half_size)  # Connect button to function


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
                self.drag_position = event.globalPosition().toPoint()  # Ensure drag_position is set
            else:
                self.start_drag(event)

    def start_drag(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def do_drag(self, event):
        if hasattr(self, 'drag_position'):
            if event.buttons() == Qt.LeftButton:
                self.move(event.globalPosition().toPoint() - self.drag_position)
                event.accept()
        else:
            self.start_drag(event)

    def do_resize(self, event):
        if self.resizing and hasattr(self, 'drag_position'):
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

    def createEdgeButtons(self):
        margin = 10

        self.left_edge_button = QPushButton(self)
        self.left_edge_button.setGeometry(0, 0, margin, self.height())
        self.left_edge_button.setStyleSheet("background: transparent;")
        self.left_edge_button.setMouseTracking(True)
        self.left_edge_button.enterEvent = self.on_edge_enter
        self.left_edge_button.leaveEvent = self.on_edge_leave
        self.left_edge_button.mousePressEvent = self.start_resize  # Ensure drag_position is set
        self.left_edge_button.mouseMoveEvent = self.do_resize
        self.left_edge_button.mouseReleaseEvent = self.stop_resize

        self.right_edge_button = QPushButton(self)
        self.right_edge_button.setGeometry(self.width() - margin, 0, margin, self.height())
        self.right_edge_button.setStyleSheet("background: transparent;")
        self.right_edge_button.setMouseTracking(True)
        self.right_edge_button.enterEvent = self.on_edge_enter
        self.right_edge_button.leaveEvent = self.on_edge_leave
        self.right_edge_button.mousePressEvent = self.start_resize  # Ensure drag_position is set
        self.right_edge_button.mouseMoveEvent = self.do_resize
        self.right_edge_button.mouseReleaseEvent = self.stop_resize

        self.bottom_edge_button = QPushButton(self)
        self.bottom_edge_button.setGeometry(0, self.height() - margin, self.width(), margin)
        self.bottom_edge_button.setStyleSheet("background: transparent;")
        self.bottom_edge_button.setMouseTracking(True)
        self.bottom_edge_button.enterEvent = self.on_edge_enter
        self.bottom_edge_button.leaveEvent = self.on_edge_leave
        self.bottom_edge_button.mousePressEvent = self.start_resize  # Ensure drag_position is set
        self.bottom_edge_button.mouseMoveEvent = self.do_resize
        self.bottom_edge_button.mouseReleaseEvent = self.stop_resize

    def start_resize(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPosition().toPoint()
            self.resizing = True
            event.accept()

    def stop_resize(self, event):
        if event.button() == Qt.LeftButton:
            self.resizing = False
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.resizing = False
            self.check_snap(event.globalPosition().toPoint())  # Check for snap
            event.accept()

    def check_snap(self, pos):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        margin = 10

        if pos.x() <= margin:  # Snap to left
            self.setGeometry(screen_geometry.x(), screen_geometry.y(), screen_geometry.width() // 2, screen_geometry.height())
        elif pos.x() >= screen_geometry.width() - margin:  # Snap to right
            self.setGeometry(screen_geometry.width() // 2, screen_geometry.y(), screen_geometry.width() // 2, screen_geometry.height())
        elif pos.y() <= margin:  # Snap to top
            self.setGeometry(screen_geometry.x(), screen_geometry.y(), screen_geometry.width(), screen_geometry.height() // 2)
        elif pos.y() >= screen_geometry.height() - margin:  # Snap to bottom
            self.setGeometry(screen_geometry.x(), screen_geometry.height() // 2, screen_geometry.width(), screen_geometry.height() // 2)








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
        pt()
        if pt.every(1.5):
            pt.t()
        margin = 10
        on_left_edge = pos.x() <= margin
        on_right_edge = pos.x() >= self.width() - margin
        on_bottom_edge = pos.y() >= self.height() - margin
        return on_left_edge or on_right_edge or on_bottom_edge

    def on_edge_enter(self, event):
        self.setCursor(Qt.SizeFDiagCursor)

    def on_edge_leave(self, event):
        self.setCursor(Qt.ArrowCursor)

    def set_half_size(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        new_width = screen_geometry.width() // 2
        new_height = screen_geometry.height() // 2
        new_x = (screen_geometry.width() - new_width) // 2
        new_y = (screen_geometry.height() - new_height) // 2
        self.setGeometry(new_x, new_y, new_width, new_height)


    def resizeEvent(self, event):
        super().resizeEvent(event)
        button_size = int(self.width() * self.button_size_percentage)
        button_spacing = int(self.width() * self.button_spacing_percentage)
        
        self.title_bar.setGeometry(0, 0, self.width(), self.title_bar_height)
        self.title_label.setGeometry(self.width() // 2 - 100, 0, 200, self.title_bar_height)
        self.reset_size_position_button.setGeometry(self.width() - 4 * (button_size + button_spacing), 0, button_size, self.title_bar_height)  # Adjust position
        self.minimize_button.setGeometry(self.width() - 3 * (button_size + button_spacing), 0, button_size, self.title_bar_height)
        self.maximize_button.setGeometry(self.width() - 2 * (button_size + button_spacing), 0, button_size, self.title_bar_height)
        self.close_button.setGeometry(self.width() - (button_size), 0, button_size, self.title_bar_height)
        self.ui_frame.setGeometry(0, self.title_bar_height, self.width(), self.height() - self.title_bar_height)
        # Remove fixed size to restore original button size
        self.minimize_button.setFixedSize(button_size, self.title_bar_height)  # Ensure fixed size
        self.maximize_button.setFixedSize(button_size, self.title_bar_height)  # Ensure fixed size
        self.close_button.setFixedSize(button_size, self.title_bar_height)  # Ensure fixed size
        
        margin = 10
        self.left_edge_button.setGeometry(0, 0, margin, self.height())
        self.right_edge_button.setGeometry(self.width() - margin, 0, margin, self.height())
        self.bottom_edge_button.setGeometry(0, self.height() - margin, self.width(), margin)

    def toggleMaximizeRestore(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

if __name__ == "__main__":
    app = QApplication([])
    player = CustomVideoPlayer()  # Updated class name
    sys.exit(app.exec())
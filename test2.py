import sys
from PySide6.QtCore import QUrl, QTimer, Qt  # Added Qt import
from PySide6.QtGui import QMovie
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QTreeView, QFrame, QFileSystemModel, QSizePolicy, QPushButton  # Added QPushButton import




class BackgroundVideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.title_bar_height = 30  # Define a variable for the title bar height
        self.setWindowFlags(Qt.FramelessWindowHint)  # Remove the default title bar
        self.setGeometry(1111, 333, 1920, 1080)

        # Create a QLabel to display the GIF
        self.gif_label = QLabel(self)
        self.movie = QMovie("lightspeed-10957.gif")
        self.gif_label.setMovie(self.movie)
        self.movie.start()

        # Create a custom title bar
        self.title_bar = QFrame(self)  # Attach title bar to self instead of gif_label
        self.title_bar.setStyleSheet("background: rgba(55, 55, 55, 0.8); color: #D8DEE9;")
        self.title_bar.setFixedHeight(self.title_bar_height)
        self.title_bar_layout = QHBoxLayout(self.title_bar)
        self.title_bar_layout.setContentsMargins(0, 0, 0, 0)

        # Add title label in the center
        self.title_label = QLabel("Custom Title Bar", self.title_bar)
        self.title_label.setAlignment(Qt.AlignCenter)

        # Add minimize, maximize, and close buttons with fixed sizes
        button_style = "QPushButton { width: 30px; height: 30px; }"
        self.minimize_button = QPushButton("-", self.title_bar)
        self.minimize_button.setStyleSheet(button_style)
        self.maximize_button = QPushButton("□", self.title_bar)
        self.maximize_button.setStyleSheet(button_style)
        self.close_button = QPushButton("X", self.title_bar)
        self.close_button.setStyleSheet(button_style)

        # Add widgets to layout
        self.title_bar_layout.addStretch()
        self.title_bar_layout.addStretch()

        self.title_bar_layout.addWidget(self.title_label)
        self.title_bar_layout.addStretch() 

        self.title_bar_layout.addWidget(self.minimize_button)
        self.title_bar_layout.addWidget(self.maximize_button)
        self.title_bar_layout.addWidget(self.close_button)

        # Connect buttons to their functions
        self.minimize_button.clicked.connect(self.showMinimized)
        self.maximize_button.clicked.connect(self.toggleMaximizeRestore)
        self.close_button.clicked.connect(self.close)

        # Enable dragging the window by the title bar
        self.title_bar.mousePressEvent = self.start_drag
        self.title_bar.mouseMoveEvent = self.do_drag

        # Create additional UI elements
        self.label1 = QLabel("Label 1", self)
        self.label1.setStyleSheet("background-color: yellow;")  # Set background color for label1
        self.label2 = QLabel("Label 2", self)
        self.label2.setStyleSheet("background-color: lightblue;")  # Set background color for label2
        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)

        # Create a file tree view
        self.file_tree = QTreeView(self)
        self.file_model = QFileSystemModel()
        self.file_model.setRootPath('')
        self.file_tree.setModel(self.file_model)

        # Layouts
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)  # No spacing
        main_layout.addWidget(self.gif_label)

        ui_layout = QVBoxLayout()
        ui_layout.addWidget(self.label1)
        ui_layout.addWidget(self.input1)
        ui_layout.addWidget(self.label2)
        ui_layout.addWidget(self.input2)
        ui_layout.addWidget(self.file_tree)

        # Frame to overlay UI elements
        ui_frame = QFrame(self.gif_label)  # Attach ui_frame to gif_label
        ui_frame.setLayout(ui_layout)
        ui_frame.setStyleSheet("background: rgba(222, 222, 222, 0.7); color: #D8DEE9;")
        ## key:                x, y, width, height
        # ui_frame.setGeometry(0, self.title_bar_height, 111, self.height() - self.title_bar_height +550)  # Adjust position and size

        # Add the frame on top of the video
        self.gif_label.setLayout(QVBoxLayout())
        self.gif_label.layout().addWidget(ui_frame)

        self.setLayout(main_layout)

        # Resize the gif to the size of the window
        self.gif_label.setScaledContents(True)
        self.gif_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        self.setLayout(main_layout)

        # Show the widget
        self.show()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.title_bar.setGeometry(0, 0, self.width(), self.title_bar_height)
        self.title_label.setGeometry(self.width() // 2 - 100, 0, 200, self.title_bar_height)
        self.minimize_button.setGeometry(self.width() - 90, 0, 30, self.title_bar_height)
        self.maximize_button.setGeometry(self.width() - 60, 0, 30, self.title_bar_height)
        self.close_button.setGeometry(self.width() - 30, 0, 30, self.title_bar_height)
        self.gif_label.layout().itemAt(0).widget().setGeometry(0, self.title_bar_height, self.width(), self.height() - self.title_bar_height)  # Adjust ui_f

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
    player = BackgroundVideoPlayer()
    sys.exit(app.exec())
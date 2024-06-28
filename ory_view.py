from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QTreeView, QFrame, QFileSystemModel, QSizePolicy, QPushButton
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt

class OrganizationallyView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title_bar_height = 30
        self.button_size_percentage = 0.075
        self.button_spacing_percentage = 0.01
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(1111, 333, 1920, 1080)
        self.resizing = False

        self.init_ui()
        self.show()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.create_gif_background()
        self.create_title_bar()
        self.create_additional_ui()
        self.create_file_tree_view()
        self.create_edge_buttons()
        self.create_layouts()

    def create_layouts(self):
        main_layout = QVBoxLayout(self.central_widget)
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

    def create_gif_background(self):
        self.gif_label = QLabel(self)
        self.movie = QMovie("lightspeed-10957.gif")
        self.gif_label.setMovie(self.movie)
        self.movie.start()
        self.gif_label.setScaledContents(True)
        self.gif_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

    def create_title_bar(self):
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
        self.reset_size_position_button = QPushButton('[□]', self.title_bar)
        self.reset_size_position_button.setStyleSheet(button_style)

        self.title_bar_layout.addStretch()
        self.title_bar_layout.addWidget(self.title_label)
        self.title_bar_layout.addStretch()
        self.title_bar_layout.addWidget(self.reset_size_position_button)
        self.title_bar_layout.addWidget(self.minimize_button)
        self.title_bar_layout.addWidget(self.maximize_button)
        self.title_bar_layout.addWidget(self.close_button)

    def create_additional_ui(self):
        self.label1 = QLabel("Label 1", self)
        self.label1.setStyleSheet("background-color: yellow;")
        self.label2 = QLabel("Label 2", self)
        self.label2.setStyleSheet("background-color: lightblue;")
        self.input1 = QLineEdit(self)
        self.input2 = QLineEdit(self)

    def create_file_tree_view(self):
        self.file_tree = QTreeView(self)
        self.file_model = QFileSystemModel()
        self.file_model.setRootPath('')
        self.file_tree.setModel(self.file_model)

    def create_edge_buttons(self):
        margin = 10

        self.left_edge_button = QPushButton(self)
        self.left_edge_button.setGeometry(0, 0, margin, self.height())
        self.left_edge_button.setStyleSheet("background: transparent;")
        self.left_edge_button.setMouseTracking(True)

        self.right_edge_button = QPushButton(self)
        self.right_edge_button.setGeometry(self.width() - margin, 0, margin, self.height())
        self.right_edge_button.setStyleSheet("background: transparent;")
        self.right_edge_button.setMouseTracking(True)

        self.bottom_edge_button = QPushButton(self)
        self.bottom_edge_button.setGeometry(0, self.height() - margin, self.width(), margin)
        self.bottom_edge_button.setStyleSheet("background: transparent;")
        self.bottom_edge_button.setMouseTracking(True)
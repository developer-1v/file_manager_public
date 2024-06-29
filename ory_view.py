"Organizationally, your organization ally for file management, project management, research, and more"

from print_tricks import pt

import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QTreeView, QFrame, QFileSystemModel, QSizePolicy, QPushButton
from PySide6.QtWidgets import QMainWindow, QStatusBar, QMenuBar, QWidget, QVBoxLayout

class OrganizationallyView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title_bar_height = 30
        self.button_size_percentage = 0.075  # Button size as a percentage of window width
        self.button_spacing_percentage = 0.01  # Spacing as a percentage of window width
        self.border_size = 10
        self.grabbing_edge_size = 10
        self.spacing_between_widgets = 10
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(1111, 333, 1920, 1080)
        self.resizing = False
        
        ## Key: Background = Background color. Color = Text color.
        self.title_bar_style = "background: rgba(55, 55, 55, 0.8); color: #D8DEE9;"
        # self.ui_frame_style = "background: rgba(222, 222, 222, 0.7); color: #D8DEE9;"
        self.ui_frame_style = "background: transparent;"
        self.edge_button_style = "background: transparent;"
        self.default_widget_style = "background: rgba(33, 33, 33, 0.99); color: #D8DEE9;"

        self.init_ui()
        self.show()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.create_gif_background()
        self.create_title_bar()
        self.createAdditionalUI()
        self.createFileTreeView()
        self.create_edge_buttons()
        self.create_layouts()

    def create_layouts(self):
        main_layout = QVBoxLayout(self.central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.gif_label)

        ui_layout = QVBoxLayout()
        ui_layout.setContentsMargins(0, 0, 0, 0)
        ui_layout.setSpacing(self.spacing_between_widgets)
        ui_layout.addWidget(self.label1)
        ui_layout.addWidget(self.input1)
        ui_layout.addWidget(self.label2)
        ui_layout.addWidget(self.input2)
        ui_layout.addWidget(self.file_tree)

        self.ui_frame = QFrame(self.central_widget)
        self.ui_frame.setLayout(ui_layout)
        self.ui_frame.setStyleSheet(self.ui_frame_style)

    def create_gif_background(self):
        self.gif_label = QLabel(self.central_widget)
        self.movie = QMovie("assets/backgrounds/lightspeed-10957.gif")
        self.gif_label.setMovie(self.movie)
        self.movie.start()
        self.gif_label.setScaledContents(True)
        self.gif_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        
    def create_title_bar(self):
        self.title_bar = QFrame(self)
        self.title_bar.setStyleSheet(self.title_bar_style)
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
        self.reset_size_position_button = QPushButton('[□]',self.title_bar)
        # self.reset_size_position_button.setIcon(QIcon("path/to/fugue/icons/appropriate_icon.png"))  # Set appropriate icon
        self.reset_size_position_button.setStyleSheet(button_style)

        self.title_bar_layout.addStretch()
        self.title_bar_layout.addWidget(self.title_label)
        self.title_bar_layout.addStretch()
        self.title_bar_layout.addWidget(self.reset_size_position_button)  # Add half size button
        self.title_bar_layout.addWidget(self.minimize_button)
        self.title_bar_layout.addWidget(self.maximize_button)
        self.title_bar_layout.addWidget(self.close_button)



## TODO DELETE
    def createAdditionalUI(self): ## TODO DELETE
        self.label1 = QLabel("Label 1", self)
        self.label1.setStyleSheet(self.default_widget_style)
        self.label2 = QLabel("Label 2", self)
        self.label2.setStyleSheet(self.default_widget_style)
        self.input1 = QLineEdit(self)
        self.input1.setStyleSheet(self.default_widget_style)
        self.input2 = QLineEdit(self)
        self.input2.setStyleSheet(self.default_widget_style)


## TODO DELETE
    def createFileTreeView(self): ## TODO DELETE
        self.file_tree = QTreeView(self)
        self.file_tree.setStyleSheet(self.default_widget_style)
        self.file_model = QFileSystemModel()
        self.file_model.setRootPath('')
        self.file_tree.setModel(self.file_model)


    def create_edge_buttons(self):
        margin = 10

        self.left_edge_button = QPushButton(self)
        self.left_edge_button.setGeometry(0, 0, margin, self.height())
        self.left_edge_button.setStyleSheet(self.edge_button_style)
        self.left_edge_button.setMouseTracking(True)

        self.right_edge_button = QPushButton(self)
        self.right_edge_button.setGeometry(self.width() - margin, 0, margin, self.height())
        self.right_edge_button.setStyleSheet(self.edge_button_style)
        self.right_edge_button.setMouseTracking(True)

        self.bottom_edge_button = QPushButton(self)
        self.bottom_edge_button.setGeometry(0, self.height() - margin, self.width(), margin)
        self.bottom_edge_button.setStyleSheet(self.edge_button_style)
        self.bottom_edge_button.setMouseTracking(True)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        button_size = int(self.width() * self.button_size_percentage)
        button_spacing = int(self.width() * self.button_spacing_percentage)
        
        
        ## TITLE BAR AREA
        
        ## Key setGeometry(x, y, width, height) - setGeometry Key
        self.title_bar.setGeometry(
            self.border_size, 
            0, 
            self.width() - self.border_size*2, 
            self.title_bar_height
        )
        self.title_label.setGeometry(self.width() // 2 - 100, 0, 200, self.title_bar_height)
        
        self.reset_size_position_button.setGeometry(self.width() - 4 * (button_size + button_spacing), 0, button_size, self.title_bar_height)  # Adjust position
        self.reset_size_position_button.setFixedSize(button_size, self.title_bar_height)
        
        self.minimize_button.setGeometry(self.width() - 3 * (button_size + button_spacing), 0, button_size, self.title_bar_height)
        self.minimize_button.setFixedSize(button_size, self.title_bar_height)
        
        self.maximize_button.setGeometry(self.width() - 2 * (button_size + button_spacing), 0, button_size, self.title_bar_height)
        self.maximize_button.setFixedSize(button_size, self.title_bar_height)
        
        self.close_button.setGeometry(self.width() - (button_size), 0, button_size, self.title_bar_height)
        self.close_button.setFixedSize(button_size, self.title_bar_height)
        
        
        ## UI AREA
        
        self.ui_frame.setGeometry(
            self.border_size,
            self.title_bar_height,
            self.width() - self.border_size*2, 
            self.height() - self.title_bar_height - self.border_size
        )
        
        
        ## EDGE AREAS
        
        self.left_edge_button.setGeometry(0, 0, self.grabbing_edge_size, self.height())
        self.right_edge_button.setGeometry(self.width() - self.grabbing_edge_size, 0, self.grabbing_edge_size, self.height())
        self.bottom_edge_button.setGeometry(0, self.height() - self.grabbing_edge_size, self.width(), self.grabbing_edge_size)


if __name__ == "__main__":
    app = QApplication([])
    player = OrganizationallyView()
    sys.exit(app.exec())
    


'''












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










    def on_edge_enter(self, event):
        self.setCursor(Qt.SizeFDiagCursor)

    def on_edge_leave(self, event):
        self.setCursor(Qt.ArrowCursor)

    def reset_size_to_half_and_center(self):
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


        self.reset_size_position_button.setFixedSize(button_size, self.title_bar_height)
        self.minimize_button.setFixedSize(button_size, self.title_bar_height)
        self.maximize_button.setFixedSize(button_size, self.title_bar_height)
        self.close_button.setFixedSize(button_size, self.title_bar_height)
        
        margin = 10
        self.left_edge_button.setGeometry(0, 0, margin, self.height())
        self.right_edge_button.setGeometry(self.width() - margin, 0, margin, self.height())
        self.bottom_edge_button.setGeometry(0, self.height() - margin, self.width(), margin)

    def toggle_maximize_restore(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
            
            
            '''
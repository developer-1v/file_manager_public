'''
Organizationally: 
Your organization ally for files, projects, research, and more!

'''

from print_tricks import pt

import sys
from PySide6.QtCore import Qt, QObject
from PySide6.QtCore import QEvent
from PySide6.QtGui import QMovie, QCursor
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QTreeView, QFrame, QFileSystemModel, QSizePolicy, QPushButton
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from frame_areas.MenuBar import MenuBar
from frame_areas.CommandBar import CommandBar
from frame_areas.TopFrame3 import TopFrame3
from frame_areas.TopFrame4 import TopFrame4
from frame_areas.OrgAccess import OrgAccess
from frame_areas.OrgSubAccess import OrgSubAccess
from frame_areas.FileExplorer import FileExplorer
from frame_areas.AIArea import AIArea
from frame_areas.SearchArea import SearchArea
from frame_areas.Status import Status
from frame_areas.Properties import Properties
from frame_areas.TreeView import TreeView

class ZArea(QFrame):
    def __init__(self, parent, style="Background: transparent;"):
        super().__init__(parent)
        self.setStyleSheet(style)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)



class ZAreasEvents(QObject):
    def __init__(self, z_areas):
        super().__init__()
        self.z_areas = z_areas
        self.z_areas.z_area_left.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.z_areas.z_area_left:
            if event.type() == QEvent.Enter:
                self.expand_left_area()
            elif event.type() == QEvent.Leave:
                self.retract_left_area()
        return super().eventFilter(obj, event)

    def expand_left_area(self):
        if not self.z_areas.is_left_expanded:
            self.z_areas.is_left_expanded = True
            bottom_height = self.z_areas.z_area_bottom.height()
            self.z_areas.z_area_left.setGeometry(
                0, 
                0, 
                int(self.z_areas.parent.width() * self.z_areas.expanded_side_areas_width_ratio), 
                self.z_areas.parent.height() - bottom_height)  # Use bottom area's height

    def retract_left_area(self):
        if self.z_areas.is_left_expanded:
            self.z_areas.is_left_expanded = False
            bottom_height = self.z_areas.z_area_bottom.height()
            self.z_areas.z_area_left.setGeometry(
                0, 
                0, 
                int(self.z_areas.parent.width() * self.z_areas.side_areas_width_ratio),
                self.z_areas.parent.height() - bottom_height)  # Use bottom area's height

class ZAreas:
    def __init__(self, 
            parent, 
            bottom_height_ratio=0.045, 
            top_height_ratio=None,
            side_areas_width_ratio=0.03,  # Initial left width ratio
            expanded_side_areas_width_ratio=0.15,  # Expanded left width ratio
            spacing=1, 
            style="rgba(55, 55, 55, 0.8)"):
        self.parent = parent
        self.bottom_height_ratio = bottom_height_ratio
        self.top_height_ratio = top_height_ratio if top_height_ratio is not None else bottom_height_ratio * 3
        self.side_areas_width_ratio = side_areas_width_ratio
        self.expanded_side_areas_width_ratio = expanded_side_areas_width_ratio
        self.spacing = spacing
        self.style = style
        self.is_left_expanded = False
        

        
        pt(top_height_ratio, bottom_height_ratio, side_areas_width_ratio, expanded_side_areas_width_ratio, spacing, style)
        # pt(self.width)
        self.init_main_areas(parent)
        self.add_widgets_to_areas()
        self.update_geometries(parent.width(), parent.height())
        self.raise_areas()

    def init_main_areas(self, parent):
        self.z_area_center_container = ZArea(parent)
        self.z_area_left = ZArea(self.z_area_center_container, style=self.style)
        self.z_area_middle = ZArea(self.z_area_center_container, style=self.style)
        self.z_area_right = ZArea(self.z_area_center_container, style=self.style)
        
        self.z_area_top = ZArea(parent, style=self.style)
        self.z_area_bottom = ZArea(parent, style=self.style)

    def update_geometries(self, width, height, debug=True):
        top_height = int(height * self.top_height_ratio)
        bottom_height = int(height * self.bottom_height_ratio)
        side_width = int(width * self.side_areas_width_ratio)
        widget_height = int(height * 0.07)
        
        self.z_area_center_container.setGeometry(0, 0, width, height)
        self.z_area_left.setGeometry(0, 0, side_width, height - bottom_height)
        self.z_area_middle.setGeometry(side_width, 0, width - 2 * side_width, height - bottom_height)
        self.z_area_right.setGeometry(width - side_width, 0, side_width, height - bottom_height)
        pt(height, height, self.z_area_left.height(), self.z_area_middle.height(), self.z_area_right.height())
        
        self.z_area_top.setGeometry(0, 0, width, top_height)
        self.z_area_bottom.setGeometry(0, height - bottom_height, width, bottom_height)
        
        self.org_access.setFixedHeight(widget_height)
        self.org_sub_access.setFixedHeight(widget_height)
        self.ai_area.setFixedHeight(widget_height)
        self.search_area.setFixedHeight(widget_height)
        if debug:
            self.z_area_middle.setStyleSheet("background: red;")
            self.z_area_left.setStyleSheet("background: green;")
            self.z_area_right.setStyleSheet("background: blue;")

    def add_widgets_to_areas(self):
        self.add_widgets_to_left_area()
        self.add_widgets_to_right_area()
        self.add_widgets_to_top_area()
        self.add_widgets_to_bottom_area()

    def add_widgets_to_left_area(self):
        self.org_access = OrgAccess(self.z_area_left)
        self.org_sub_access = OrgSubAccess(self.z_area_left)
        left_layout = QHBoxLayout(self.z_area_left)
        left_layout.addWidget(self.org_access)
        left_layout.addWidget(self.org_sub_access)
        self.z_area_left.setLayout(left_layout)

    def add_widgets_to_right_area(self):
        self.ai_area = AIArea(self.z_area_right)
        self.search_area = SearchArea(self.z_area_right)
        right_layout = QHBoxLayout(self.z_area_right)
        right_layout.addWidget(self.ai_area)
        right_layout.addWidget(self.search_area)
        self.z_area_right.setLayout(right_layout)

    def add_widgets_to_top_area(self):
        self.command_bar = CommandBar(self.z_area_top)
        self.top_frame3 = TopFrame3(self.z_area_top)
        self.top_frame4 = TopFrame4(self.z_area_top)
        top_layout = QVBoxLayout(self.z_area_top)
        top_layout.setSpacing(self.spacing)
        top_layout.addWidget(self.command_bar)
        top_layout.addWidget(self.top_frame3)
        top_layout.addWidget(self.top_frame4)
        self.z_area_top.setLayout(top_layout)

    def add_widgets_to_bottom_area(self):
        self.status = Status(self.z_area_bottom)
        self.properties = Properties(self.z_area_bottom)
        self.tree_view = TreeView(self.z_area_bottom)
        bottom_layout = QHBoxLayout(self.z_area_bottom)
        bottom_layout.addWidget(self.status)
        bottom_layout.addWidget(self.properties)
        bottom_layout.addWidget(self.tree_view)
        self.z_area_bottom.setLayout(bottom_layout)

    def raise_areas(self):
        self.z_area_center_container.raise_()
        self.z_area_middle.raise_()
        self.z_area_left.raise_()
        self.z_area_right.raise_()
        self.z_area_bottom.raise_()
        self.z_area_top.raise_()


class OrganizationallyView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title_bar_height = 30
        self.button_size_percentage = 0.075
        self.button_spacing_percentage = 0.01
        self.border_size = 10
        self.grabbing_edge_size = 10
        self.spacing_between_widgets = 10
        self.edge_margin = 10
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(1111, 333, 1920, 1080)
        self.resizing = False
        
        self.theme_menu_bg_color = "rgba(55, 55, 55, 0.8)"
        self.theme_menu_text_color = "#D8DEE9"
        self.theme_menu_style = f"background: {self.theme_menu_bg_color}; color: {self.theme_menu_text_color};"
        self.ui_frame_style = "background: transparent;"
        self.edge_button_style = "background: transparent;"
        self.default_widget_style = f"background: rgba(33, 33, 33, 0.999); color: {self.theme_menu_text_color};"
        
        self.bg_movie_speed = 33
        
        self.init_ui()
        self.z_areas = ZAreas(self.ui_frame, style=self.theme_menu_style)
        self.z_areas_events = ZAreasEvents(self.z_areas)

        self.events = OrganizationallyViewEvents(self)
        self.show()

    def init_ui(self):
        self.create_central_widget()
        self.create_movie_background()
        self.create_title_bar()
        self.create_edge_buttons()
        self.create_ui_frame()
        # self.createAdditionalUI()
        self.create_layouts()

    def create_layouts(self):
        main_layout = QVBoxLayout(self.central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.movie_label)
        
        self.ui_layout = QVBoxLayout()
        self.ui_layout.setContentsMargins(0, 0, 0, 0)
        self.ui_layout.setSpacing(self.spacing_between_widgets)
        
        self.ui_frame.setLayout(self.ui_layout)

    def create_ui_frame(self):
        self.ui_frame = QFrame(self.central_widget)
        self.ui_frame.setStyleSheet(self.ui_frame_style)
        # self.create_z_areas()

    def create_central_widget(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

    def create_movie_background(self):
        self.movie_label = QLabel(self.central_widget)
        self.movie = QMovie("assets/backgrounds/lightspeed-10957.mp4")
        self.movie.setSpeed(self.bg_movie_speed)
        self.movie_label.setMovie(self.movie)
        self.movie.start()
        self.movie_label.setScaledContents(True)
        self.movie_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

    def create_title_bar(self):
        self.title_bar = QFrame(self)
        self.title_bar.setStyleSheet(self.theme_menu_style)
        self.title_bar.setFixedHeight(self.title_bar_height)
        self.title_bar_layout = QHBoxLayout(self.title_bar)
        self.title_bar_layout.setContentsMargins(self.border_size, 0, 0, 0)  # Adjust left margin

        self.menu_bar = MenuBar(self.title_bar, self.theme_menu_style)
        self.title_bar_layout.addWidget(self.menu_bar)

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

    def create_edge_buttons(self, debug=False):
        self.left_edge_button = QPushButton(self)
        self.left_edge_button.setMouseTracking(True)
        
        self.right_edge_button = QPushButton(self)
        self.right_edge_button.setMouseTracking(True)
        
        self.bottom_edge_button = QPushButton(self)
        self.bottom_edge_button.setMouseTracking(True)
        
        self.left_bottom_corner_button = QPushButton(self)
        self.left_bottom_corner_button.setMouseTracking(True)
        
        self.right_bottom_corner_button = QPushButton(self)
        self.right_bottom_corner_button.setMouseTracking(True)
        
        if not debug:
            self.left_edge_button.setStyleSheet(self.edge_button_style)
            self.right_edge_button.setStyleSheet(self.edge_button_style)
            self.bottom_edge_button.setStyleSheet(self.edge_button_style)
            self.left_bottom_corner_button.setStyleSheet(self.edge_button_style)
            self.right_bottom_corner_button.setStyleSheet(self.edge_button_style)
        else:
            self.left_edge_button.setStyleSheet('background: rgba(255, 0, 0, 1);')
            self.right_edge_button.setStyleSheet('background: rgba(255, 0, 0, 1);')
            self.bottom_edge_button.setStyleSheet('background: rgba(0, 255, 0, 1);')
            self.left_bottom_corner_button.setStyleSheet('background: rgba(0, 0, 255, 1);')
            self.right_bottom_corner_button.setStyleSheet('background: rgba(0, 0, 255, 1);')

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_sizes()

    def update_sizes(self, debug=False):
        button_size = int(self.width() * self.button_size_percentage)
        button_spacing = int(self.width() * self.button_spacing_percentage)
        
        
        ## TITLE BAR AREA
        
        ## Key setGeometry(x, y, width, height) - setGeometry Key
        self.title_bar.setGeometry(
            0,
            # self.border_size,
            0, 
            # self.width() - self.border_size*2, 
            self.width(), 
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
            self.title_bar_height + self.border_size,
            self.width() - self.border_size*2, 
            self.height() - self.title_bar_height - self.border_size*2
        )


        
        
        ## EDGE AREAS
        
        self.left_edge_button.setGeometry(0, 0, self.grabbing_edge_size, self.height())
        self.right_edge_button.setGeometry(self.width() - self.grabbing_edge_size, 0, self.grabbing_edge_size, self.height())
        self.bottom_edge_button.setGeometry(0, self.height() - self.grabbing_edge_size, self.width(), self.grabbing_edge_size)

        corner_multiplier = 2
        self.left_bottom_corner_button.setGeometry(0, self.height() - self.grabbing_edge_size*corner_multiplier, self.grabbing_edge_size*corner_multiplier, self.grabbing_edge_size*corner_multiplier)
        self.right_bottom_corner_button.setGeometry(self.width() - self.grabbing_edge_size*corner_multiplier, self.height() - self.grabbing_edge_size*corner_multiplier, self.grabbing_edge_size*corner_multiplier, self.grabbing_edge_size*corner_multiplier)

        self.z_areas.update_geometries(self.ui_frame.width(), self.ui_frame.height())
        self.z_areas.raise_areas()




class OrganizationallyViewEvents:
    def __init__(self, view):
        self.view = view

    def start_drag(self, event):
        if event.button() == Qt.LeftButton:
            self.view.drag_position = event.globalPosition().toPoint() - self.view.frameGeometry().topLeft()
            event.accept()

    def do_drag(self, event):
        if hasattr(self.view, 'drag_position'):
            if event.buttons() == Qt.LeftButton:
                self.view.move(event.globalPosition().toPoint() - self.view.drag_position)
                event.accept()
        else:
            self.start_drag(event)

    def do_resize(self, event):
        if self.view.resizing and hasattr(self.view, 'drag_position'):
            delta = event.globalPosition().toPoint() - self.view.drag_position
            new_width = self.view.width()
            new_height = self.view.height()
            new_x = self.view.x()
            new_y = self.view.y()

            if self.view.drag_position.x() <= 10:  # Left edge
                new_width -= delta.x()
                new_x += delta.x()
            elif self.view.drag_position.x() >= self.view.width() - 10:  # Right edge
                new_width += delta.x()
            if self.view.drag_position.y() >= self.view.height() - 10:  # Bottom edge
                new_height += delta.y()

            self.view.setGeometry(new_x, new_y, new_width, new_height)
            self.view.drag_position = event.globalPosition().toPoint()

    def start_resize(self, event):
        if event.button() == Qt.LeftButton:
            self.view.drag_position = event.globalPosition().toPoint()
            self.view.resizing = True
            event.accept()

    def stop_resize(self, event):
        if event.button() == Qt.LeftButton:
            self.view.resizing = False
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.view.resizing = False
            self.check_snap(event.globalPosition().toPoint())  # Check for snap
            event.accept()

    def check_snap(self, pos):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        margin = 10

        if pos.x() <= margin:  # Snap to left
            self.view.setGeometry(screen_geometry.x(), screen_geometry.y(), screen_geometry.width() // 2, screen_geometry.height())
        elif pos.x() >= screen_geometry.width() - margin:  # Snap to right
            self.view.setGeometry(screen_geometry.width() // 2, screen_geometry.y(), screen_geometry.width() // 2, screen_geometry.height())
        elif pos.y() <= margin:  # Snap to top
            self.view.setGeometry(screen_geometry.x(), screen_geometry.y(), screen_geometry.width(), screen_geometry.height() // 2)
        elif pos.y() >= screen_geometry.height() - margin:  # Snap to bottom
            self.view.setGeometry(screen_geometry.x(), screen_geometry.height() // 2, screen_geometry.width(), screen_geometry.height() // 2)

    def reset_size_to_half_and_center(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        new_width = screen_geometry.width() // 2
        new_height = screen_geometry.height() // 2
        new_x = (screen_geometry.width() - new_width) // 2
        new_y = (screen_geometry.height() - new_height) // 2
        self.view.setGeometry(new_x, new_y, new_width, new_height)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        button_size = int(self.view.width() * self.view.button_size_percentage)
        button_spacing = int(self.view.width() * self.view.button_spacing_percentage)

        self.view.title_bar.setGeometry(0, 0, self.view.width(), self.view.title_bar_height)
        self.view.title_label.setGeometry(self.view.width() // 2 - 100, 0, 200, self.view.title_bar_height)
        self.view.reset_size_position_button.setGeometry(self.view.width() - 4 * (button_size + button_spacing), 0, button_size, self.view.title_bar_height)  # Adjust position
        self.view.minimize_button.setGeometry(self.view.width() - 3 * (button_size + button_spacing), 0, button_size, self.view.title_bar_height)
        self.view.maximize_button.setGeometry(self.view.width() - 2 * (button_size + button_spacing), 0, button_size, self.view.title_bar_height)
        self.view.close_button.setGeometry(self.view.width() - (button_size), 0, button_size, self.view.title_bar_height)
        self.view.ui_frame.setGeometry(0, self.view.title_bar_height, self.view.width(), self.view.height() - self.view.title_bar_height)

        self.view.reset_size_position_button.setFixedSize(button_size, self.view.title_bar_height)
        self.view.minimize_button.setFixedSize(button_size, self.view.title_bar_height)
        self.view.maximize_button.setFixedSize(button_size, self.view.title_bar_height)
        self.view.close_button.setFixedSize(button_size, self.view.title_bar_height)

        margin = 10
        self.view.left_edge_button.setGeometry(0, 0, margin, self.view.height())
        self.view.right_edge_button.setGeometry(self.view.width() - margin, 0, margin, self.view.height())
        self.view.bottom_edge_button.setGeometry(0, self.view.height() - margin, self.view.width(), margin)

    def toggle_maximize_restore(self):
        if self.view.isMaximized():
            self.view.showNormal()
        else:
            self.view.showMaximized()



if __name__ == "__main__":
    app = QApplication([])
    player = OrganizationallyView()
    sys.exit(app.exec())


'''




'''



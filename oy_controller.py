from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from oy_model import OrganizationallyModel
from oy_view import OrganizationallyView, OrganizationallyViewEvents

from print_tricks import pt


class OrganizationallyController:
    def __init__(self):
        self.model = OrganizationallyModel()
        self.view = OrganizationallyView()
        self.events = OrganizationallyViewEvents(self.view)
        
        self.view.reset_size_position_button.clicked.connect(self.events.reset_size_to_half_and_center)
        self.view.minimize_button.clicked.connect(self.view.showMinimized)
        self.view.maximize_button.clicked.connect(self.events.toggle_maximize_restore)
        self.view.close_button.clicked.connect(self.view.close)
        
        self.view.title_bar.mousePressEvent = self.events.start_drag
        self.view.title_bar.mouseMoveEvent = self.events.do_drag
        
        # Connect edge buttons to resize events and change cursor
        self.view.left_edge_button.setCursor(Qt.SizeHorCursor)
        self.view.left_edge_button.mousePressEvent = self.events.start_resize
        self.view.left_edge_button.mouseMoveEvent = self.events.do_resize
        self.view.left_edge_button.mouseReleaseEvent = self.events.stop_resize
        
        self.view.right_edge_button.setCursor(Qt.SizeHorCursor)
        self.view.right_edge_button.mousePressEvent = self.events.start_resize
        self.view.right_edge_button.mouseMoveEvent = self.events.do_resize
        self.view.right_edge_button.mouseReleaseEvent = self.events.stop_resize
        
        self.view.bottom_edge_button.setCursor(Qt.SizeVerCursor)
        self.view.bottom_edge_button.mousePressEvent = self.events.start_resize
        self.view.bottom_edge_button.mouseMoveEvent = self.events.do_resize
        self.view.bottom_edge_button.mouseReleaseEvent = self.events.stop_resize
        
        self.view.left_bottom_corner_button.setCursor(Qt.SizeBDiagCursor)
        self.view.left_bottom_corner_button.mousePressEvent = self.events.start_resize
        self.view.left_bottom_corner_button.mouseMoveEvent = self.events.do_resize
        self.view.left_bottom_corner_button.mouseReleaseEvent = self.events.stop_resize
        
        self.view.right_bottom_corner_button.setCursor(Qt.SizeFDiagCursor)
        self.view.right_bottom_corner_button.mousePressEvent = self.events.start_resize
        self.view.right_bottom_corner_button.mouseMoveEvent = self.events.do_resize
        self.view.right_bottom_corner_button.mouseReleaseEvent = self.events.stop_resize



if __name__ == "__main__":
    app = QApplication([])
    controller = OrganizationallyController()
    app.exec()
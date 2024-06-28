from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from ory_model import OrganizationallyModel
from ory_view import OrganizationallyView

class OrganizationallyController:
    def __init__(self):
        self.model = OrganizationallyModel()
        self.view = OrganizationallyView()

        self.view.reset_size_position_button.clicked.connect(self.reset_size_to_half_and_center)
        self.view.minimize_button.clicked.connect(self.view.showMinimized)
        self.view.maximize_button.clicked.connect(self.toggle_maximize_restore)
        self.view.close_button.clicked.connect(self.view.close)

        self.view.title_bar.mousePressEvent = self.start_drag
        self.view.title_bar.mouseMoveEvent = self.do_drag

    def start_drag(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.view.frameGeometry().topLeft()
            event.accept()

    def do_drag(self, event):
        if event.buttons() == Qt.LeftButton:
            self.view.move(event.globalPosition().toPoint() - self.drag_position)
            event.accept()

    def reset_size_to_half_and_center(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        new_width = screen_geometry.width() // 2
        new_height = screen_geometry.height() // 2
        new_x = (screen_geometry.width() - new_width) // 2
        new_y = (screen_geometry.height() - new_height) // 2
        self.view.setGeometry(new_x, new_y, new_width, new_height)

    def toggle_maximize_restore(self):
        if self.view.isMaximized():
            self.view.showNormal()
        else:
            self.view.showMaximized()

if __name__ == "__main__":
    app = QApplication([])
    controller = OrganizationallyController()
    app.exec()
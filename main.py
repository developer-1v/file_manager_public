from PySide6.QtWidgets import QApplication

from oy_controller import OrganizationallyController

class Organizationally:
    def __init__(self):
        app = QApplication([])
        
        
        self.controller = OrganizationallyController()
        self.controller.view.show()
        app.exec()

if __name__ == "__main__":
    Organizationally()
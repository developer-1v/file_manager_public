from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QFrame, QSplitter, QLabel, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor
from MenuBar import MenuBar
from CommandBar import CommandBar
from TopFrame3 import TopFrame3
from TopFrame4 import TopFrame4
from OrgAccess import OrgAccess
from OrgSubAccess import OrgSubAccess
from FileExplorer import FileExplorer
from AIArea import AIArea
from SearchArea import SearchArea
from TreeView import TreeView
from Properties import Properties

class HoverFrame(QFrame):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.setToolTip(name)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dynamic GUI")
        self.setGeometry(100, 100, 1920, 1080)
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(QVBoxLayout())

        self.create_top_frame_area()
        self.create_middle_frame_area()
        self.create_bottom_frame_area()

    def create_top_frame_area(self):
        top_frame = HoverFrame("Top Frame Area")
        top_frame.setFrameShape(QFrame.StyledPanel)
        top_frame.setFixedHeight(self.height() * 0.18)
        top_layout = QVBoxLayout(top_frame)
        top_layout.setSpacing(1)

        menu_bar = HoverFrame("MenuBar")
        command_bar = HoverFrame("CommandBar")
        top_frame3 = HoverFrame("TopFrame3")
        top_frame4 = HoverFrame("TopFrame4")

        top_layout.addWidget(menu_bar)
        top_layout.addWidget(command_bar)
        top_layout.addWidget(top_frame3)
        top_layout.addWidget(top_frame4)

        self.centralWidget().layout().addWidget(top_frame)

    def create_middle_frame_area(self):
        middle_frame = HoverFrame("Middle Frame Area")
        middle_frame.setFrameShape(QFrame.StyledPanel)
        middle_layout = QHBoxLayout(middle_frame)
        middle_layout.setSpacing(1)

        org_access = HoverFrame("OrgAccess")
        org_sub_access = HoverFrame("OrgSubAccess")
        file_explorer_area = self.create_file_explorer_area()
        ai_area = HoverFrame("AIArea")
        search_area = HoverFrame("SearchArea")

        middle_layout.addWidget(org_access)
        middle_layout.addWidget(org_sub_access)
        middle_layout.addWidget(file_explorer_area)
        middle_layout.addWidget(ai_area)
        middle_layout.addWidget(search_area)

        self.centralWidget().layout().addWidget(middle_frame)

    def create_bottom_frame_area(self):
        bottom_frame = HoverFrame("Bottom Frame Area")
        bottom_frame.setFrameShape(QFrame.StyledPanel)
        bottom_frame.setFixedHeight(self.height() * 0.05)
        bottom_layout = QHBoxLayout(bottom_frame)
        bottom_layout.setSpacing(1)

        properties = HoverFrame("Properties")
        tree_view = HoverFrame("TreeView")

        bottom_layout.addWidget(properties)
        bottom_layout.addWidget(tree_view)

        self.centralWidget().layout().addWidget(bottom_frame)

    def create_file_explorer_area(self):
        file_explorer_area = HoverFrame("FileExplorerArea")
        file_explorer_area.setFrameShape(QFrame.StyledPanel)
        file_explorer_layout = QVBoxLayout(file_explorer_area)
        file_explorer_layout.setSpacing(1)

        for _ in range(2):  # 2 rows
            row_layout = QHBoxLayout()
            for _ in range(3):  # 3 columns
                file_explorer = HoverFrame("FileExplorer")
                row_layout.addWidget(file_explorer)
            file_explorer_layout.addLayout(row_layout)

        return file_explorer_area

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
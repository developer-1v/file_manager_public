''' copy of original main.py'''

from print_tricks import pt


from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QFrame, QSplitter, QLabel, QWidget
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QCursor, QPalette, QColor, QMovie
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dynamic GUI")
        self.setGeometry(1111, 333, 1920, 1080)
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(QVBoxLayout())
        # self.setStyleSheet("color: #D8DEE9;")
        self.setStyleSheet("background-color: #2E3440; color: #D8DEE9;")
        
        self.generic_spacing = 0

        self.create_top_frame_area()
        self.create_middle_frame_area()
        self.create_bottom_frame_area()




    def create_top_frame_area(self):
        top_frame = QFrame()
        top_frame.setFrameShape(QFrame.StyledPanel)
        top_frame.setFixedHeight(self.height() * 0.18)
        top_layout = QVBoxLayout(top_frame)
        top_layout.setSpacing(self.generic_spacing)

        menu_bar = MenuBar(self)
        command_bar = CommandBar(self)
        top_frame3 = TopFrame3(self)
        top_frame4 = TopFrame4(self)

        top_layout.addWidget(menu_bar)
        top_layout.addWidget(command_bar)
        top_layout.addWidget(top_frame3)
        top_layout.addWidget(top_frame4)

        def expand():
            pt(menu_bar.height())
            command_bar.show()
            top_frame3.show()
            top_frame4.show()
            top_frame.setFixedHeight(self.height() * 0.18)

        def collapse():
            pt(menu_bar.height())
            command_bar.hide()
            top_frame3.hide()
            top_frame4.hide()
            top_frame.setFixedHeight(menu_bar.height() * 1.5)

        menu_bar.enterEvent = lambda event: expand()
        top_frame.leaveEvent = lambda event: collapse()

        self.centralWidget().layout().addWidget(top_frame)
        collapse()  # Start collapsed

    def create_middle_frame_area(self, org_access_pct=7, org_sub_access_pct=7, ai_area_pct=7, search_area_pct=7):
        middle_frame = QFrame()
        middle_frame.setFrameShape(QFrame.StyledPanel)
        middle_layout = QHBoxLayout(middle_frame)
        middle_layout.setSpacing(self.generic_spacing)

        org_access = self.create_collapsible_frame(OrgAccess(self), org_access_pct)
        org_sub_access = self.create_collapsible_frame(OrgSubAccess(self), org_sub_access_pct)
        file_explorer_area = self.create_file_explorer_area()
        ai_area = self.create_collapsible_frame(AIArea(self), ai_area_pct)
        search_area = self.create_collapsible_frame(SearchArea(self), search_area_pct)

        remaining_pct = 100 - (org_access_pct + org_sub_access_pct + ai_area_pct + search_area_pct)

        middle_layout.addWidget(org_access, org_access_pct)
        middle_layout.addWidget(org_sub_access, org_sub_access_pct)
        middle_layout.addWidget(file_explorer_area, remaining_pct)
        middle_layout.addWidget(ai_area, ai_area_pct)
        middle_layout.addWidget(search_area, search_area_pct)

        self.centralWidget().layout().addWidget(middle_frame)

    def create_bottom_frame_area(self):
        bottom_frame = QFrame()
        bottom_frame.setFrameShape(QFrame.StyledPanel)
        bottom_frame.setFixedHeight(self.height() * 0.05)
        bottom_layout = QHBoxLayout(bottom_frame)
        bottom_layout.setSpacing(self.generic_spacing)

        status = Status(self)
        properties = Properties(self)
        tree_view = TreeView(self)

        bottom_layout.addWidget(status)
        bottom_layout.addWidget(properties)
        bottom_layout.addWidget(tree_view)

        self.centralWidget().layout().addWidget(bottom_frame)

    def create_file_explorer_area(self, rows=2, columns=3):
        file_explorer_area = QFrame()
        file_explorer_area.setFrameShape(QFrame.StyledPanel)
        file_explorer_layout = QVBoxLayout(file_explorer_area)
        file_explorer_layout.setSpacing(self.generic_spacing)

        for _ in range(rows):  # 2 rows
            row_layout = QHBoxLayout()
            for _ in range(columns):  # 3 columns
                file_explorer = FileExplorer(self)
                row_layout.addWidget(file_explorer)
            file_explorer_layout.addLayout(row_layout)

        return file_explorer_area

    def create_collapsible_frame(self, widget, pct):
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFixedWidth(self.width() * (pct / 100))
        layout = QVBoxLayout(frame)
        layout.addWidget(widget)
        frame.setFixedWidth(self.width() * 0.01)  # Start collapsed

        def expand():
            frame.setFixedWidth(self.width() * (pct / 100))

        def collapse():
            frame.setFixedWidth(self.width() * 0.01)

        frame.enterEvent = lambda event: expand()
        frame.leaveEvent = lambda event: collapse()

        return frame

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()




'''


1 - Give me the complete code that meets all of my requirements, even if it takes additional prompts and don't explain, just show the code. Also, go over your own answer to make sure it covers all of my requirements. 
2 - use pyside6 to create a gui that can dynamically change the size of its internal frames based on the changing size of the window. Set the window size to be variable, but default to 1920x1080, and centered on the screen. 
3 - In general, any frame area and sub frame area that we create should have a parameter passed to change the percentage width and height size of the frame area and each individual frame. 
4 - And frame areas should be able to have the mouse click/drag on their borders to resize them. 
5 - Hovering over a frame will say what that sub frame area is. 
6 - The spacing between each frame should be configurable, but default to just 1.
7 - Make a top frame area that contains 4 subframes. The subframes will hold the imported instances of MenuBar, CommandBar, TopFrame3, and TopFrame4. The top frame area should be 100% width and defaulted to 18% height of the window. Each subframe should be vertically stacked on each other and take up 100% of the width and .25% of the height of the top frame area. 
8 - NOw make a bottom frames area. This will be 100% width and defaulted to 5% height of the window. This will contain 2 subframes. The subframes will hold the imported instances of Properties and TreeView. 
9 - NOw make a middle frames area. This will be 100% width and it's % height will be the height that is left over after subtracting the top and bottom frame areas from the window. This middle frames area will contain 5 subframes in order horizontally from left to right that contain the imported instances of OrgAccess, OrgSubAccess, FileExplorerArea, AIArea, and SearchArea. These will all take up 7% of the width and 100% of the height of the middle frames area, except for the FileExplorerArea that will take up the remaining % of the width and 100% of the height of the middle frames area. 
10 - The FileExplorerArea Will contain a variable amount of 1 to 6 imported instances of FileExplorer. It should have a configurable number of rows and columns. Let's default this to 2 rows and 3 columns. 
11 - use my imports to create the gui. 
'''
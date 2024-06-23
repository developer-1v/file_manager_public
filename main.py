from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QFrame, QSplitter, QLabel
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dynamic GUI")
        self.setGeometry(100, 100, 1920, 1080)
        self.setCentralWidget(QFrame())
        self.centralWidget().setLayout(QVBoxLayout())
        
        self.create_top_frame_area()
        self.create_middle_frame_area()
        self.create_bottom_frame_area()

    def create_top_frame_area(self):
        top_frame = QFrame()
        top_frame.setFrameShape(QFrame.StyledPanel)
        top_frame.setLayout(QVBoxLayout())
        top_frame.setFixedHeight(self.height() * 0.18)
        
        menu_bar = MenuBar()
        command_bar = CommandBar()
        top_frame3 = TopFrame3()
        top_frame4 = TopFrame4()
        
        for widget in [menu_bar, command_bar, top_frame3, top_frame4]:
            frame = QFrame()
            frame.setFrameShape(QFrame.StyledPanel)
            frame.setLayout(QVBoxLayout())
            frame.layout().addWidget(widget)
            frame.setFixedHeight(top_frame.height() * 0.25)
            frame.setToolTip(widget.__class__.__name__)
            top_frame.layout().addWidget(frame)
        
        self.centralWidget().layout().addWidget(top_frame)

    def create_middle_frame_area(self):
        middle_frame = QSplitter(Qt.Horizontal)
        middle_frame.setFrameShape(QFrame.StyledPanel)
        
        org_access = OrgAccess()
        org_sub_access = OrgSubAccess()
        file_explorer_area = self.create_file_explorer_area()
        ai_area = AIArea()
        search_area = SearchArea()
        
        for widget in [org_access, org_sub_access, file_explorer_area, ai_area, search_area]:
            frame = QFrame()
            frame.setFrameShape(QFrame.StyledPanel)
            frame.setLayout(QVBoxLayout())
            frame.layout().addWidget(widget)
            frame.setToolTip(widget.__class__.__name__)
            middle_frame.addWidget(frame)
        
        self.centralWidget().layout().addWidget(middle_frame)

    def create_bottom_frame_area(self):
        bottom_frame = QFrame()
        bottom_frame.setFrameShape(QFrame.StyledPanel)
        bottom_frame.setLayout(QHBoxLayout())
        bottom_frame.setFixedHeight(self.height() * 0.05)
        
        properties = Properties()
        tree_view = TreeView()
        
        for widget in [properties, tree_view]:
            frame = QFrame()
            frame.setFrameShape(QFrame.StyledPanel)
            frame.setLayout(QVBoxLayout())
            frame.layout().addWidget(widget)
            frame.setToolTip(widget.__class__.__name__)
            bottom_frame.layout().addWidget(frame)
        
        self.centralWidget().layout().addWidget(bottom_frame)

    def create_file_explorer_area(self):
        file_explorer_area = QFrame()
        file_explorer_area.setFrameShape(QFrame.StyledPanel)
        file_explorer_area.setLayout(QVBoxLayout())
        
        for _ in range(6):  # Example with 6 FileExplorer instances
            file_explorer = FileExplorer()
            frame = QFrame()
            frame.setFrameShape(QFrame.StyledPanel)
            frame.setLayout(QVBoxLayout())
            frame.layout().addWidget(file_explorer)
            frame.setToolTip(file_explorer.__class__.__name__)
            file_explorer_area.layout().addWidget(frame)
        
        return file_explorer_area

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
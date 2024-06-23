from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class MenuBar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # layout = QVBoxLayout()
        # self.setLayout(layout)
        label = QLabel("Menu Bar", self)
        # layout.addWidget(label)
        
        
'''

1 - use pyside6 to create a gui that can dynamically change the size of its internal frames based on the changing size of the window. Set the window size to be variable, but default to 1920x1080, and centered on the screen. 
2 - In general, any frame area and sub frame area that we create should have a parameter passed to change the percentage width and height size of the frame area and each individual frame. And all should be click-draqggable to resize them. And hovering over them will say what that sub frame area is. 
3 - Make a top frame area that contains 4 subframes. The subframes will hold the instances of MenuBar, CommandBar, TopFrame3, and TopFrame4. The top frame area should be 100% width and defaulted to 18% height of the window. 
4 - NOw make a bottom frames area. This will be 100% width and defaulted to 5% height of the window. This will contain 2 subframes. The subframes will hold the instances of TreeView and Properties. 
5 - NOw make a middle frames area. This will be 100% width and it's % height will be the height that is left over after subtracting the top and bottom frame areas from the window. This middle frames area will contain 5 subframes in order horizontally from left to right: OrgAccess, OrgSubAccess, FileExplorerArea, AIArea, and SearchArea. These will all take up 7% of the width and 100% of the height of the middle frames area, except for the FileExplorerArea. This will take up the remaining % of the width and 100% of the height of the middle frames area. 
6 - The middle frames area: Will that contain a variable amount of 1 to 6 instances of FileExplorer. It should have a configurable number of rows and columns.

'''
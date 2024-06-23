from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QScrollArea, QFrame
from PyQt5.QtCore import QSize, Qt
import sys
from MenuBar import MenuBar
from CommandBar import CommandBar
from OrgAccess import OrgAccess
from OrgSubAccess import OrgSubAccess
from FileExplorer import FileExplorer
from AIArea import AIArea
from SearchArea import SearchArea
from TreeView import TreeView
from TopFrame3 import TopFrame3
from TopFrame4 import TopFrame4



class FileManager(QWidget):
    def __init__(self, 
            rows=1, 
            columns=4, 
            left_frames=2, 
            right_frames=2, 
            left_side=True, 
            top_frames=4, 
            window_width=1200, 
            window_height=800, 
            window_position=(100, 100), 
            spacing=0,
            top_frames_height=55, 
            vertical_frame_width=200,
            bottom_frame_height=200,
        ):
        super().__init__()
        
        self.initUI(rows, columns, left_frames, right_frames, left_side, top_frames, window_width, window_height, window_position, spacing, top_frames_height, vertical_frame_width, bottom_frame_height)

    def initUI(self, rows, columns, left_frames, right_frames, left_side, top_frames, window_width, window_height, window_position, spacing, top_frames_height, vertical_frame_width, bottom_frame_height):
        self.setWindowTitle('Configurable Grid File Explorer')
        self.setGeometry(100, 100, window_width, window_height)

        grid = QGridLayout()
        grid.setSpacing(spacing)
        self.setLayout(grid)

        def create_frame(widget_class, width_percent, height_percent, min_width, min_height):
            frame = QFrame()
            frame.setFrameShape(QFrame.Box)
            frame.setLineWidth(1)
            frame.setMinimumSize(min_width, min_height)
            frame.setFixedSize(int(window_width * width_percent), int(window_height * height_percent))
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
            scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            widget = widget_class()
            scroll_area.setWidget(widget)
            layout = QGridLayout()
            layout.setContentsMargins(0, 0, 0, 0)
            layout.addWidget(scroll_area)
            frame.setLayout(layout)
            return frame

        # Add top frames
        top_frame_classes = [MenuBar, CommandBar, TopFrame3, TopFrame4]
        top_frame_sizes = [(1.0, 0.1, 100, 25), (1.0, 0.1, 100, 25), (1.0, 0.1, 100, 25), (1.0, 0.1, 100, 25)]
        for i in range(min(top_frames, 4)):
            if top_frame_classes[i]:
                width_percent, height_percent, min_width, min_height = top_frame_sizes[i]
                frame = create_frame(top_frame_classes[i], width_percent, height_percent, min_width, min_height)
                grid.addWidget(frame, i, 0, 1, columns + left_frames + right_frames)

        # Calculate height for vertical and inner frames
        vertical_frame_height_percent = (window_height - sum([window_height * size[1] for size in top_frame_sizes]) - bottom_frame_height) / window_height
        middle_frame_height_percent = vertical_frame_height_percent

        # Add left or right vertical frames
        vertical_frame_classes = [OrgAccess, OrgSubAccess]
        if left_side:
            for i in range(left_frames):
                frame = create_frame(vertical_frame_classes[i], vertical_frame_width / window_width, vertical_frame_height_percent, 100, 100)
                grid.addWidget(frame, top_frames, i, rows, 1)
        else:
            for i in range(right_frames):
                frame = create_frame(vertical_frame_classes[i], vertical_frame_width / window_width, vertical_frame_height_percent, 100, 100)
                grid.addWidget(frame, top_frames, columns + 1 + i, rows, 1)

        # Add file explorer frames
        for r in range(rows):
            for c in range(columns):
                frame = create_frame(FileExplorer, vertical_frame_width / window_width, middle_frame_height_percent, 100, 100)
                if left_side:
                    grid.addWidget(frame, top_frames + r, left_frames + c, 1, 1)
                else:
                    grid.addWidget(frame, top_frames + r, c, 1, 1)

        # Add right vertical frames if left_side is True
        if not left_side:
            for i in range(right_frames):
                frame = create_frame(vertical_frame_classes[i], vertical_frame_width / window_width, vertical_frame_height_percent, 100, 100)
                grid.addWidget(frame, top_frames, columns + left_frames + i, rows, 1)

        # Add extra frames
        extra_frame_classes = [AIArea, SearchArea]
        if left_side:
            for i in range(right_frames):
                frame = create_frame(extra_frame_classes[i], vertical_frame_width / window_width, vertical_frame_height_percent, 100, 100)
                grid.addWidget(frame, top_frames, columns + left_frames + i, rows, 1)
        else:
            for i in range(left_frames):
                frame = create_frame(extra_frame_classes[i], vertical_frame_width / window_width, vertical_frame_height_percent, 100, 100)
                grid.addWidget(frame, top_frames, i, rows, 1)

        # Add bottom frame
        bottom_frame = create_frame(TreeView, 1.0, bottom_frame_height / window_height, 100, 25)
        grid.addWidget(bottom_frame, top_frames + rows, 0, 1, columns + left_frames + right_frames)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    fm = FileManager(
        rows=2, 
        columns=3, 
        left_frames=2, 
        right_frames=2, 
        left_side=True, 
        top_frames=4, 
        window_width=1920, 
        window_height=1080, 
        spacing=0,
        top_frames_height=25,
        vertical_frame_width=200,
        bottom_frame_height=25)
    fm.show()
    sys.exit(app.exec_())
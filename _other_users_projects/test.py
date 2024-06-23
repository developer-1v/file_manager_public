from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLabel, QFrame
import sys
import os

class FileExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        listbox = QListWidget(self)
        self.populate_listbox(listbox)
        layout.addWidget(listbox)

    def populate_listbox(self, listbox):
        for item in os.listdir('/'):
            listbox.addItem(item)



class FileExplorerApp(QWidget):
    def __init__(self, rows=1, columns=4, left_frames=2, right_frames=2, left_side=True, top_frames=4):
        super().__init__()
        self.initUI(rows, columns, left_frames, right_frames, left_side, top_frames)

    def initUI(self, rows, columns, left_frames, right_frames, left_side, top_frames):
        self.setWindowTitle('Configurable Grid File Explorer')
        self.setGeometry(100, 100, 1200, 800)

        grid = QGridLayout()
        self.setLayout(grid)

        # Add top frames
        top_frame_classes = [TopFrame1, TopFrame2, TopFrame3, TopFrame4]
        for i in range(min(top_frames, 4)):
            frame = top_frame_classes[i]()
            grid.addWidget(frame, i, 0, 1, columns + 2)  # Span all columns + side frames

        # Add left or right vertical frames
        vertical_frame_classes = [Navigation, SubNavigation]
        if left_side:
            for i in range(left_frames):
                frame = vertical_frame_classes[i]()
                grid.addWidget(frame, top_frames, i, rows, 1)
        else:
            for i in range(right_frames):
                frame = vertical_frame_classes[i]()
                grid.addWidget(frame, top_frames, columns + 1 + i, rows, 1)

        # Add file explorer frames
        for r in range(rows):
            for c in range(columns):
                frame = FileExplorer()
                if left_side:
                    grid.addWidget(frame, top_frames + r, left_frames + c, 1, 1)
                else:
                    grid.addWidget(frame, top_frames + r, c, 1, 1)

        # Add right vertical frames if left_side is True
        if not left_side:
            for i in range(right_frames):
                frame = vertical_frame_classes[i]()
                grid.addWidget(frame, top_frames, columns + left_frames + i, rows, 1)

        # Add extra frames
        extra_frame_classes = [Extra1, Extra2]
        if left_side:
            for i in range(right_frames):
                frame = extra_frame_classes[i]()
                grid.addWidget(frame, top_frames, columns + left_frames + i, rows, 1)
        else:
            for i in range(left_frames):
                frame = extra_frame_classes[i]()
                grid.addWidget(frame, top_frames, i, rows, 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileExplorerApp(rows=2, columns=3, left_frames=2, right_frames=2, left_side=True, top_frames=4)
    ex.show()
    sys.exit(app.exec_())
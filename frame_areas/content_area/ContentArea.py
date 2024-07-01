from print_tricks import pt
pt.easy_imports('main.py')

from PySide6.QtWidgets import QApplication






from PySide6.QtWidgets import QFrame, QVBoxLayout, QGridLayout, QScrollArea, QSizePolicy, QSplitter
from PySide6.QtCore import Qt
from PySide6.QtWebEngineWidgets import QWebEngineView
import os
import sys
from frame_areas.content_area.FileExplorer import FileExplorer

class ContentArea(QFrame):
    def __init__(self, 
            parent, 
            rows=12, 
            cols=12, 
            visible_rows=2, 
            visible_cols=2, 
            zoom=1.0, 
            style="Background: transparent;", 
            content_size=(1920, 1080)):
        super().__init__(parent)
        self.name = "Content Area"
        self.rows = rows
        self.cols = cols
        self.visible_rows = visible_rows
        self.visible_cols = visible_cols
        self.zoom = zoom
        self.style = style
        self.content_size = content_size
        self.initUI()
        
        pt(self.size(), self.visible_rows, self.visible_cols, self.zoom)

    def initUI(self):
        self.resize(self.content_size[0], self.content_size[1])
        self.setToolTip(self.name)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.createScrollArea(layout)
        self.updateGrid()
        self.resizeEvent = self.onResize  # Connect resize event to onResize method

    def createScrollArea(self, layout):
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        layout.addWidget(scroll_area)
        self.scroll_area = scroll_area

        # Set custom style for scrollbars
        self.scroll_area.setStyleSheet("""
            QScrollBar:vertical, QScrollBar:horizontal {
                background: transparent;
                width: 8px;
                height: 8px;
            }
            QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
                background: #888;
                border-radius: 4px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                background: none;
            }
        """)


    def mouseMoveEvent(self, event):
        margin = 0.05  # 5% margin
        width = self.width()
        height = self.height()
        x, y = event.x(), event.y()

        if x < width * margin or x > width * (1 - margin) or y < height * margin or y > height * (1 - margin):
            pt()
            self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        else:
            pt()
            self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        super().mouseMoveEvent(event)


    def enterEvent(self, event):
        pt()
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        super().enterEvent(event)

    def leaveEvent(self, event):
        pt()
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        super().leaveEvent(event)

    def updateGrid(self):
        grid_widget = QFrame()
        grid_layout = QGridLayout(grid_widget)
        grid_widget.setLayout(grid_layout)
        self.scroll_area.setWidget(grid_widget)
        for row in range(self.rows):
            for col in range(self.cols):
                splitter = QSplitter(Qt.Horizontal)
                if (row + col) % 2 == 0:
                    cell_widget = FileExplorer(self)
                else:
                    cell_widget = QWebEngineView()
                    cell_widget.setUrl("https://www.example.com")
                splitter.addWidget(cell_widget)
                grid_layout.addWidget(splitter, row, col)
        self.adjustCellSize(grid_widget)

    def onResize(self, event):
        self.adjustCellSize(self.scroll_area.widget())
        super().resizeEvent(event)

    def adjustCellSize(self, grid_widget):
        cell_size_x = self.size().width() / self.visible_cols
        cell_size_y = self.size().height() / self.visible_rows
        for row in range(self.rows):
            for col in range(self.cols):
                widget = grid_widget.layout().itemAtPosition(row, col).widget()
                widget.setFixedSize(cell_size_x, cell_size_y)
        grid_widget.setMinimumSize(int(cell_size_x * self.cols), int(cell_size_y * self.rows))


## TODO NOT CALLED
    def setZoom(self, zoom):
        self.zoom = zoom
        self.visible_rows = int(self.rows / (zoom / 100))
        self.visible_cols = int(self.cols / (zoom / 100))
        self.updateGrid()

## TODO NOT CALLED
    def setVisibleArea(self, visible_rows, visible_cols):
        self.visible_rows = visible_rows
        self.visible_cols = visible_cols
        self.zoom = 100 * (self.rows / visible_rows)
        self.updateGrid()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    content_area = ContentArea(
        None, 
        rows=12, 
        cols=12, 
        visible_rows=2, 
        visible_cols=2,
        style="Background: transparent;",
        content_size=(1920, 1080),
    )

    content_area.show()
    sys.exit(app.exec())
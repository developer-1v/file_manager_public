from print_tricks import pt
pt.easy_imports('main.py')

from PySide6.QtWidgets import QApplication






from PySide6.QtWidgets import QFrame, QVBoxLayout, QGridLayout, QScrollArea, QSizePolicy, QSplitter
from PySide6.QtCore import Qt
from PySide6.QtWebEngineWidgets import QWebEngineView
import os
import sys
from frame_areas.content_area.FileExplorer import FileExplorer

import json


class ContentArea(QFrame):
    def __init__(self, 
            parent,
            rows=12,
            cols=12,
            visible_rows=2,
            visible_cols=2,
            current_row=0,
            current_col=0,
            zoom=1.0,
            style="Background: transparent;",
            content_size=(1920, 1080)):
        super().__init__(parent)
        self.name = "Content Area"
        self.rows = rows
        self.cols = cols
        self.visible_rows = visible_rows
        self.visible_cols = visible_cols
        self.current_row = current_row
        self.current_col = current_col
        self.zoom = zoom
        self.style = style
        self.content_size = content_size
        self.data_file = "content_area_data.json"
        self.cell_data = self.loadCellData()
        self.initUI()
        
        pt(self.size(), self.visible_rows, self.visible_cols, self.zoom)
        # pt.t()

    def loadCellData(self):
        pt('load cell data')
        if os.path.exists(self.data_file) and os.path.getsize(self.data_file) > 0:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        else:
            return self.generateCellData()

    def generateCellData(self):
        pt('generate cell data')
        cell_data = []
        for row in range(self.rows):
            row_data = []
            for col in range(self.cols):
                if (row + col) % 2 == 0:
                    row_data.append({"type": "FileExplorer", "path": r"c:/Users/user/Documents"})  # Use forward slashes
                else:
                    row_data.append({"type": "QWebEngineView", "url": "https://www.example.com"})
            cell_data.append(row_data)
        with open(self.data_file, 'w') as file:
            json.dump(cell_data, file)
        return cell_data

    def updateGrid(self):
        pt('upgrade grid')
        grid_widget = QFrame()
        grid_layout = QGridLayout(grid_widget)
        grid_widget.setLayout(grid_layout)
        self.scroll_area.setWidget(grid_widget)
        self.scroll_area.verticalScrollBar().valueChanged.connect(self.printVisibleCells)
        self.scroll_area.horizontalScrollBar().valueChanged.connect(self.printVisibleCells)
        for row in range(self.rows):
            for col in range(self.cols):
                splitter = QSplitter(Qt.Horizontal)
                cell_info = self.cell_data[row][col]
                if cell_info["type"] == "FileExplorer":
                    cell_widget = FileExplorer(self, start_path=cell_info["path"])  # Ensure path is correctly passed
                else:
                    cell_widget = QWebEngineView()
                    cell_widget.setUrl(cell_info["url"])
                splitter.addWidget(cell_widget)
                grid_layout.addWidget(splitter, row, col)
        self.adjustCellSize(grid_widget)
        self.printVisibleCells()  # Print visible cells after updating the grid

    def printVisibleCells(self, value=None, debug=True):
        if not debug:
            return
        
        vertical_scroll_value = self.scroll_area.verticalScrollBar().value()
        horizontalScrollBar = self.scroll_area.horizontalScrollBar().value()
        cell_size_x = self.size().width() / self.visible_cols
        cell_size_y = self.size().height() / self.visible_rows
        self.current_row = int(vertical_scroll_value / cell_size_y)
        self.current_col = int(horizontalScrollBar / cell_size_x)
        print(f"Current position: Row {self.current_row}, Col {self.current_col}")
        pt.c("Visible cells:")
        for row in range(self.current_row, self.current_row + self.visible_rows):
            for col in range(self.current_col, self.current_col + self.visible_cols):
                print(f"Cell ({row}, {col}): {self.cell_data[row][col]}")


    def onResize(self, event):
        self.adjustCellSize(self.scroll_area.widget())
        self.printVisibleCells()  # Print visible cells on resize
        super().resizeEvent(event)

    def mouseMoveEvent(self, event):
        margin = 0.05  # 5% margin
        width = self.width()
        height = self.height()
        x, y = event.x(), event.y()

        if x < width * margin or x > width * (1 - margin) or y < height * margin or y > height * (1 - margin):
            self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        else:
            self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        super().mouseMoveEvent(event)
        self.printVisibleCells()  # P
        
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
    pt.t()
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
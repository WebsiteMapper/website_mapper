from PyQt6.QtWidgets import QMainWindow, QSplitter, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtWebEngineWidgets import QWebEngineView
from core.mapper import Mapper
from ui.controls import setup_controls

class WebsiteMapper(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Website Mapper")
        self.setGeometry(100, 100, 1200, 800)

        # Main layout
        main_layout = QSplitter(Qt.Orientation.Horizontal)
        self.setCentralWidget(main_layout)

        # Browser view
        self.browser = QWebEngineView()
        main_layout.addWidget(self.browser)

        # Map view
        self.map_widget = QWidget()
        self.map_layout = QVBoxLayout()
        self.map_widget.setLayout(self.map_layout)
        main_layout.addWidget(self.map_widget)

        # Initialize mapper
        self.mapper = Mapper(self.browser)

        # Set up UI elements
        setup_controls(self)

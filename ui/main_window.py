from PyQt6.QtWidgets import QMainWindow, QSplitter, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QFileDialog, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtWebEngineWidgets import QWebEngineView
from core.mapper import Mapper
from ui.controls import setup_controls
from utils.export_import import export_map, import_map

class WebsiteMapper(QMainWindow):
    """
    Main window class for the Website Mapper application.
    
    This class sets up the user interface and connects the various
    components of the application.
    """
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

        # Add buttons for notes, endpoints, export, and import
        self.add_note_button = QPushButton("Add Note")
        self.add_note_button.clicked.connect(self.add_note)
        
        self.capture_endpoint_button = QPushButton("Capture Endpoints")
        self.capture_endpoint_button.clicked.connect(self.mapper.capture_endpoint)

        self.export_button = QPushButton("Export Map")
        self.export_button.clicked.connect(self.export_map)

        self.import_button = QPushButton("Import Map")
        self.import_button.clicked.connect(self.import_map)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_note_button)
        button_layout.addWidget(self.capture_endpoint_button)
        button_layout.addWidget(self.export_button)
        button_layout.addWidget(self.import_button)
        
        self.map_layout.addLayout(button_layout)

    def add_note(self):
        current_url = self.browser.url().toString()
        self.mapper.add_note(current_url)

    def export_map(self):
    """
    Export the current map to a JSON file.
        
    Opens a file dialog for the user to choose the save location,
    then exports the map data to the chosen file.
    """
        file_name, _ = QFileDialog.getSaveFileName(self, "Export Map", "", "JSON Files (*.json)")
        if file_name:
            try:
                export_map(self.mapper.graph.graph, file_name)
                QMessageBox.information(self, "Success", "Map exported successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred while exporting the map: {str(e)}")

    def import_map(self):
    """
    Import a previously exported map from a JSON file.
        
    Opens a file dialog for the user to choose the file to import,
    then loads the map data and updates the display.
    """
        file_name, _ = QFileDialog.getOpenFileName(self, "Import Map", "", "JSON Files (*.json)")
        if file_name:
            try:
                imported_graph = import_map(file_name)
                self.mapper.graph.graph = imported_graph
                self.mapper.update_map()
                QMessageBox.information(self, "Success", "Map imported successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred while importing the map: {str(e)}")

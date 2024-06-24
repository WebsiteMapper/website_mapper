from PyQt6.QtWidgets import QLineEdit, QPushButton, QVBoxLayout

def setup_controls(window):
    # URL input
    window.url_input = QLineEdit()
    window.url_input.setPlaceholderText("Enter URL to map")
    window.url_input.returnPressed.connect(window.mapper.start_mapping)

    # Start mapping button
    window.start_button = QPushButton("Start Mapping")
    window.start_button.clicked.connect(window.mapper.start_mapping)

    # Add to layout
    controls_layout = QVBoxLayout()
    controls_layout.addWidget(window.url_input)
    controls_layout.addWidget(window.start_button)
    window.map_layout.addLayout(controls_layout)

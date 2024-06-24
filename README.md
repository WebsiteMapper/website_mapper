# Website Mapper

Website Mapper is a desktop application that allows users to create visual maps of websites by manually clicking through links. It's designed to assist Quality Assurance engineers and Product managers in understanding website structures.

## Features

- Create website maps by manually navigating through pages
- Visualize website structure as an interactive graph
- Add custom notes to pages
- Capture and display endpoint information
- Export and import maps for sharing or later use

## Installation

1. Ensure you have Python 3.7 or later installed on your system.
2. Clone this repository: git clone https://github.com/yourusername/website-mapper.git
3. Install the required dependencies: pip install -r requirements.txt

## Usage

1. Run the application: python main.py
2. Enter a URL in the input field and click "Start Mapping" or press Enter.
3. Navigate through the website using the embedded browser. The map will update as you visit new pages.
4. Use the buttons at the bottom of the window to add notes, capture endpoints, or export/import maps.

## User Guide

### Creating a Map
1. Enter the starting URL for the website you want to map.
2. Click "Start Mapping" to begin.
3. Use the embedded browser to click through the website. Each new page you visit will be added to the map.

### Adding Notes
1. Navigate to the page you want to add a note to.
2. Click the "Add Note" button.
3. Enter your note in the popup dialog and click OK.

### Capturing Endpoints
1. Navigate to the page you want to capture endpoints for.
2. Click the "Capture Endpoints" button.
3. The application will automatically detect and add endpoint information to the current page node.

### Exporting Maps
1. Click the "Export Map" button.
2. Choose a location and filename to save your map.
3. The map will be saved as a JSON file.

### Importing Maps
1. Click the "Import Map" button.
2. Select a previously exported map file.
3. The application will load the map and display it.

## Contributing

Contributions to Website Mapper are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import WebsiteMapper

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mapper = WebsiteMapper()
    mapper.show()
    sys.exit(app.exec())

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtGui import QFont, QFontDatabase
from src.menu_bar import MenuBar
from src.branches_list_frame import BrancheslistFrame
import sys

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(800, 600)
        self.setWindowTitle(".gitui")

        self.menu_bar = MenuBar(self)
        self.menu_bar.setFont(QFont('Inter', 12))
        self.setMenuBar(self.menu_bar)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self.branches_list_frame = BrancheslistFrame()
        self.main_layout.addWidget(self.branches_list_frame)

        self.main_layout.addStretch()
    def _setup_font(self):
        font_pathes = (r'res\fonts\Inter\Inter-VariableFont_opsz,wght.ttf', r'res\fonts\JetBrains_Mono\JetBrainsMono-VariableFont_wght.ttf')

        for font_path in font_pathes:
            QFontDatabase.addApplicationFont(font_path)

        self.setFont(QFont("Inter", 12))
        self.mono_font = "JetBrains Mono"

        self.setStyleSheet(r"""
            QMainWindow, QDialog, QWidget {{
                font-family: "Inter", "Segoe UI", "Arial", sans-serif;
                font-size: 10pt;
            }}
            
            QMenuBar {{
                font-family: "Inter", "Segoe UI", "Arial", sans-serif;
                font-size: 10pt;
            }}
            
            QTableWidget, QTextEdit, QPlainTextEdit, QListWidget {{
                font-family: "JetBrains Mono", "Courier New", monospace;
                font-size: 10pt;
            }}
            
            QPushButton {{
                font-weight: bold;
                font-size: 10pt;
            }}
        """)
        
if __name__ == '__main__':
    application = QApplication(sys.argv)
    app = App()
    app.show()
    sys.exit(application.exec())
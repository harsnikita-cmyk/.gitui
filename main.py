from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFont, QFontDatabase
from src.menu_bar import MenuBar
import sys

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle(".gitui")

        self.menu_bar = MenuBar(self)
        self.menu_bar.setFont(QFont('Inter', 12))
        self.setMenuBar(self.menu_bar)

    def _setup_font(self):
        font_id = QFontDatabase.addApplicationFont("fonts/Inter-Regular.ttf")
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            font = QFont(font_family, 10)
            self.setFont(font)

        font_id_mono = QFontDatabase.addApplicationFont("fonts/JetBrainsMono-Regular.ttf")
        if font_id_mono != -1:
            mono_family = QFontDatabase.applicationFontFamilies(font_id_mono)[0]

        self.setStyleSheet(r"""
            /* Всё приложение */
            QMainWindow, QDialog, QWidget {{
                font-family: "Inter", "Segoe UI", "Arial", sans-serif;
                font-size: 10pt;
            }}
            
            /* Меню (чуть крупнее для удобства) */
            QMenuBar {{
                font-family: "Inter", "Segoe UI", "Arial", sans-serif;
                font-size: 10pt;
            }}
            
            /* Таблицы и лог (моноширинный) */
            QTableWidget, QTextEdit, QPlainTextEdit, QListWidget {{
                font-family: "JetBrains Mono", "Courier New", monospace;
                font-size: 10pt;
            }}
            
            /* Кнопки (жирный для акцента) */
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
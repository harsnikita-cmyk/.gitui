from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import QSize
import sys

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle(".gitui")

        self.create_toolbar()

    def create_toolbar(self):
        self.toolbar = self.addToolBar("Home")
        self.toolbar.setMovable(False)

        self.toolbar.setIconSize(QSize(24, 24))

        new_action = QAction(QIcon("icons/new-btn.svg"), "New", self)
        self.toolbar.addAction(new_action)

        new_action = QAction(QIcon("icons/open-btn.svg"), "Open", self)
        self.toolbar.addAction(new_action)

        new_action = QAction(QIcon("icons/refresh-btn.svg"), "Refresh", self)
        self.toolbar.addAction(new_action)

        new_action = QAction(QIcon("icons/commit-btn.svg"), "Commit", self)
        self.toolbar.addAction(new_action)
        
if __name__ == '__main__':
    application = QApplication(sys.argv)
    app = App()
    app.show()
    sys.exit(application.exec())
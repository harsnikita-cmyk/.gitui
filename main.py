from PySide6.QtWidgets import QApplication, QMainWindow
import sys

class App(QMainWindow):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    app = App()
    app.show()
    sys.exit(application.exec())
from PySide6.QtWidgets import QMenuBar, QMessageBox
from PySide6.QtGui import QAction, QKeySequence
class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        
        # ✅ Сохраняем ссылку на главное окно
        self.main_window = parent

        self.menu_elements = {
            'File': [["New Repository", QKeySequence("Ctrl+N"), None],
                     ["Open Repository", QKeySequence("Ctrl+O"), None],
                     ["Close Repository", QKeySequence("Ctrl+W"), None],
                     ["Quit", QKeySequence("Alt+F4"), None]],
            'Repository': [["Refresh", QKeySequence("F5"), None],
                           ["Add All", QKeySequence("Ctrl+A"), None],
                           ["Cancel Adding", QKeySequence("Ctrl+Shift+A"), None],
                           ["Commit", QKeySequence("Ctrl+Enter"), None],
                           ["Cancel Last Commit", QKeySequence("Ctrl+Z"), None]],
            'Branch': [["New Branch", QKeySequence("Ctrl+B"), None],
                       ["Switch Branch", QKeySequence("Ctrl+Shift+B"), None],
                       ["New And Switch", QKeySequence("Ctrl+Shift+N"), None],
                       ["Merge", QKeySequence("Ctrl+M"), None],
                       ["Delete Branch", QKeySequence("Del"), None]],
            'Sync': [["Pull", QKeySequence("Ctrl+Shift+P"), None],
                     ["Push", QKeySequence("Ctrl+P"), None],
                     ["Remote Control", QKeySequence("Ctrl+R"), None],
                     ["Clone Online Repository", QKeySequence("Ctrl+Shift+O"), None]],
            'Log': [["History", QKeySequence("Ctrl+L"), None],
                    ["Commit Details", QKeySequence("Enter"), None],
                    ["Compare With Last", QKeySequence("Ctrl+D"), None]],
            'Tools': [["Settings", QKeySequence("Ctrl+,"), None],
                      ["Dark / Light Theme", QKeySequence("Ctrl+T"), None],
                      ["Update Git", QKeySequence("Ctrl+U"), None]],
            'Help': [["Documentation", QKeySequence("F1"), None],
                     ["About .gitui", QKeySequence("Ctrl+Shift+A"), self.about]]
        }

        # Создаём меню из словаря
        for menu_name, menu_content in self.menu_elements.items():
            menu = self.addMenu(menu_name)
            for element in menu_content:
                action = QAction(element[0], menu)
                action.setShortcut(element[1])
                
                # ✅ Подключаем функцию, если она есть
                if element[2] is not None:
                    action.triggered.connect(element[2])
                
                menu.addAction(action)

    def about(self):
        QMessageBox.about(
            self.main_window,
            "О программе",
            "<h2>.gitUi</h2>"
            "<p>Версия: 0.1.0</p>"
            "<p>Мой первый серьёзный Git-клиент</p>"
            "<p>Сделано с ❤️ на Python + PySide6</p>"
        )
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton, QVBoxLayout
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class BranchItem(QFrame):
    """Один элемент списка веток"""
    def __init__(self, name, last_commit, is_current=False, parent=None):
        super().__init__(parent)
        self.name = name
        self.last_commit = last_commit
        self.is_current = is_current

        self.setFixedHeight(50)
        self.setStyleSheet('margin: 0 auto;')
        self.setup_ui()
        self.apply_style()
    
    def setup_ui(self):
        # Основной горизонтальный лейаут
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(10)
        
        # 1. Иконка ветки
        self.icon_label = QLabel("⎇" if not self.is_current else "★")
        self.icon_label.setFixedWidth(30)
        self.icon_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.icon_label)
        
        # 2. Название ветки (жирное)
        self.name_label = QLabel(self.name)
        self.name_label.setFont(QFont("Inter", 10, QFont.Bold))
        self.name_label.setMinimumWidth(120)
        layout.addWidget(self.name_label)
        
        # 3. Последний коммит (хэш + сообщение)
        self.commit_label = QLabel(self.last_commit)
        self.commit_label.setStyleSheet("QLabel{color: #A0A0A0; font-size: 9pt;}")
        self.commit_label.setWordWrap(True)
        layout.addWidget(self.commit_label)
        
        # Растяжка, чтобы элементы были по краям
        layout.addStretch()
        
        # 4. Кнопка "Переключиться" (только если это не текущая ветка)
        if not self.is_current:
            self.switch_btn = QPushButton("Switch")
            self.switch_btn.setStyleSheet('''QPushButton{background-color: #00a2ff;}
                                            QPushButton:hover{background-color: #10b2ff}
                                            QPushButton:pressed{background-color: #0092ef}
                                            ''')
            self.switch_btn.setFixedWidth(90)
            # self.switch_btn.clicked.connect(self.on_switch_clicked)
            layout.addWidget(self.switch_btn)
        else:
            # Метка "Текущая"
            current_label = QLabel("Текущая")
            current_label.setStyleSheet("color: #4CAF50; font-weight: bold;")
            current_label.setFixedWidth(120)
            current_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(current_label)
    
    def apply_style(self):
        # Фон зависит от того, текущая ветка или нет
        bg_color = "#2D2D30" if not self.is_current else "#1E3A2F"
        border_color = "#3D3D40" if not self.is_current else "#4CAF50"
        
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {bg_color};
                border: 1px solid {border_color};
                border-radius: 6px;
                margin: 2px 0px;
            }}
        """)

class BrancheslistFrame(QFrame):
    def __init__(self):
        super().__init__()

        self.setObjectName('parent_frame')
        # self.setFixedWidth(400)
        self.setFixedHeight(300)
        self.setStyleSheet('''#parent_frame {
                            border-radius: 16px;
                            border: 2px solid #6e6e6e;
                            background-color: #3b3b3b;
                            }''')

        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)
        self.setBranches([0, 1, 2, 3, 4])

    def setBranches(self, branches_name: list):
        for name in range(3):
            branch = BranchItem('Test_123', last_commit='Tested_test_test', parent=self)
            self.main_layout.addWidget(branch)
        self.main_layout.addStretch()

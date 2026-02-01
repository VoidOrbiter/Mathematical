from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout
)
from src.page_logic.page_navigation import switch_to_page

class MainMenu(QWidget):
    def __init__(self, main_window):
        super().__init__()
        from registries.page_manifest import PAGE_MANIFEST

        self.main_window = main_window
        page_name = "Main Menu"
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        for page in PAGE_MANIFEST:
            owner = page.get("owner")
            if owner == "MainMenu":
                target      = page.get("page")
                page_name   = page.get("name")
                btn         = QPushButton(page_name)
                self.layout.addWidget(btn)
                btn.clicked.connect(lambda checked, t=target: switch_to_page(self, t))

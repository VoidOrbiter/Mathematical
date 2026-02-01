import sys
import os
from PyQt5.QtWidgets import (
    QMainWindow, QStackedWidget, QToolBar,
    QAction, QApplication
)
from src.page_logic.page_navigation import go_back, jump_home, update_ui
from registries.page_registry import PAGE_REGISTRY

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mathematical!")
        self.resize(700, 800)

        # --- STACK ---
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        for entry in PAGE_REGISTRY:
            
            page_widget = entry(self)
            self.stack.addWidget(page_widget)

        # --- TOOLBAR ---
        self.toolbar = QToolBar("Main Toolbar")
        self.addToolBar(self.toolbar)
        self.toolbar.setMovable(False)

        self.home_action = QAction("Home", self)
        self.home_action.triggered.connect(lambda: jump_home(self))
        self.toolbar.addAction(self.home_action)

        self.toolbar.addSeparator()

        self.back_action = QAction("← Back", self)
        self.back_action.triggered.connect(lambda: go_back(self))
        self.toolbar.addAction(self.back_action)

        update_ui(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # --- THEME LOADING ---
    script_dir = os.path.dirname(os.path.abspath(__file__))
    qss_path = os.path.join(script_dir, "theme/main.qss")

    try:
        with open(qss_path, "r") as f:
            style = f.read()
            app.setStyleSheet(style)
    except FileNotFoundError:
        print(f"Warning: {qss_path} not found. Using default styles.")

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
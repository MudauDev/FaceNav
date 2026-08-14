from PySide6.QtWidgets import QApplication

from src.ui.main_window import MainWindow


class FaceNavApplication:
    """Application coordinator for FaceNav."""

    def __init__(self, app: QApplication) -> None:
        self.app = app
        self.main_window = MainWindow()

    def start(self) -> None:
        """Start the FaceNav desktop application."""
        self.main_window.show()
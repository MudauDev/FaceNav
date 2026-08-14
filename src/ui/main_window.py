from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    """Main FaceNav application window."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("FaceNav")
        self.setMinimumSize(1100, 700)

        self._build_ui()
        self._apply_styles()

    def _build_ui(self) -> None:
        """Build the main application interface."""

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        sidebar = self._create_sidebar()
        content = self._create_content()

        main_layout.addWidget(sidebar)
        main_layout.addWidget(content, 1)

    def _create_sidebar(self) -> QFrame:
        """Create the application navigation sidebar."""

        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(240)

        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(20, 25, 20, 20)
        layout.setSpacing(10)

        logo = QLabel("FaceNav")
        logo.setObjectName("logo")

        subtitle = QLabel("Facial Navigation")
        subtitle.setObjectName("subtitle")

        layout.addWidget(logo)
        layout.addWidget(subtitle)
        layout.addSpacing(30)

        navigation_items = [
            "Dashboard",
            "Tracking",
            "Calibration",
            "Profiles",
            "Settings",
            "About",
        ]

        for item in navigation_items:
            button = QPushButton(item)
            button.setMinimumHeight(48)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            layout.addWidget(button)

        layout.addStretch()

        powered_by = QLabel(
            "Powered by\nFloSie Business Intelligence"
        )
        powered_by.setObjectName("poweredBy")

        layout.addWidget(powered_by)

        return sidebar

    def _create_content(self) -> QFrame:
        """Create the main dashboard content area."""

        content = QFrame()
        content.setObjectName("content")

        layout = QVBoxLayout(content)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)

        title = QLabel("Welcome to FaceNav")
        title.setObjectName("pageTitle")

        description = QLabel(
            "AI-powered facial navigation for accessible computing."
        )
        description.setObjectName("description")

        status_card = QFrame()
        status_card.setObjectName("statusCard")

        status_layout = QVBoxLayout(status_card)

        status_title = QLabel("System Status")
        status_title.setObjectName("cardTitle")

        status = QLabel(
            "● Ready — Tracking is currently inactive"
        )
        status.setObjectName("status")

        status_layout.addWidget(status_title)
        status_layout.addWidget(status)

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addWidget(status_card)

        layout.addStretch()

        return content

    def _apply_styles(self) -> None:
        """Apply FaceNav application styling."""

        self.setStyleSheet(
            """
            QMainWindow {
                background: #F5F7FA;
            }

            QFrame#sidebar {
                background: #0F172A;
            }

            QFrame#content {
                background: #F5F7FA;
            }

            QLabel#logo {
                font-size: 28px;
                font-weight: bold;
                color: white;
            }

            QLabel#subtitle {
                font-size: 13px;
                color: #94A3B8;
            }

            QLabel#pageTitle {
                font-size: 32px;
                font-weight: bold;
                color: #0F172A;
            }

            QLabel#description {
                font-size: 16px;
                color: #64748B;
            }

            QPushButton {
                border: none;
                border-radius: 10px;
                padding: 12px;
                text-align: left;
                font-size: 15px;
                color: #334155;
                background: transparent;
            }

            QPushButton:hover {
                background: #E2E8F0;
            }

            QFrame#sidebar QPushButton {
                color: #CBD5E1;
            }

            QFrame#sidebar QPushButton:hover {
                background: #1E293B;
                color: white;
            }

            QFrame#statusCard {
                background: white;
                border-radius: 16px;
                padding: 20px;
            }

            QLabel#cardTitle {
                font-size: 18px;
                font-weight: bold;
                color: #0F172A;
            }

            QLabel#status {
                font-size: 15px;
                color: #16A34A;
            }

            QLabel#poweredBy {
                font-size: 11px;
                color: #64748B;
            }
            """
        )
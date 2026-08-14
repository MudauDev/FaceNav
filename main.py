import sys

from PySide6.QtWidgets import QApplication

from src.core.application import FaceNavApplication


def main() -> int:
    app = QApplication(sys.argv)

    face_nav = FaceNavApplication(app)
    face_nav.start()

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
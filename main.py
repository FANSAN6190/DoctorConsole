# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMessageBox, QPushButton, QStackedWidget, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile

class MainWindow(QMainWindow):
    def __init__(self, ui_file_path):
        super().__init__()
        self.ui_file_path = ui_file_path
        self.load_ui()
        self.setup_ui()

    def load_ui(self):
        ui_file = QFile(self.ui_file_path)
        if not ui_file.open(QFile.ReadOnly):
            raise IOError(f"Cannot open {self.ui_file_path}: {ui_file.errorString()}")

        loader = QUiLoader()
        self.window = loader.load(ui_file, self)
        ui_file.close()

        if self.window is None:
            raise RuntimeError(f"Failed to load UI file: {self.ui_file_path}")

    def setup_ui(self):
        # Find the QStackedWidget
        self.stacked_widget = self.window.findChild(QStackedWidget, "stackedWidget")

        # Find the buttons
        self.button_page1 = self.window.findChild(QPushButton, "medHistory")
        self.button_page2 = self.window.findChild(QPushButton, "newPriscrip")

        # Connect buttons to change pages
        self.button_page1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.button_page2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        self.window.show()

def main():
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)

    try:
        MainWindow("mainwindow.ui")
        sys.exit(app.exec())

    except Exception as e:
        QMessageBox.critical(None, "Error", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()

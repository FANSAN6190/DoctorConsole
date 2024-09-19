# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMessageBox, QPushButton, QStackedWidget, QMainWindow, QLineEdit, QLabel
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile

class MainWindow(QMainWindow):
    def __init__(self, ui_file_path):
        super().__init__()
        self.ui_file_path = ui_file_path
        self.load_ui()
        self.setup_ui()
        self.current_patient = None

        self.userDb = {
            "patient1@example.com": "Patient 1: John Doe, Age: 30, Condition: Healthy",
            "patient2@example.com": "Patient 2: Jane Smith, Age: 25, Condition: Flu",
            "patient3@example.com": "Patient 3: Bob Johnson, Age: 40, Condition: Diabetes"
        }

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

        # Find the search input and button
        self.email_input = self.window.findChild(QLineEdit, "searchInput")
        self.search_button = self.window.findChild(QPushButton, "searchButton")
        self.text_details = self.window.findChild(QLabel, "textDetails")

        # Connect the search button to the search function
        self.search_button.clicked.connect(self.search_patient)

        self.window.show()

    def search_patient(self):
        email = self.email_input.text()
        patient_details = self.fetch_patient_details(email)
        if patient_details:
            self.text_details.setText(patient_details)
        else:
            self.text_details.setText("Patient not found")

    def fetch_patient_details(self, email):
        return self.userDb.get(email, None)

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

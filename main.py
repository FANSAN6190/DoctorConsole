# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMessageBox, QPushButton, QStackedWidget, QMainWindow, QLineEdit, QLabel, QDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile

class AuthWindow(QDialog):
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
        print("AuthWindow UI loaded successfully")

    def setup_ui(self):
        # Find the input fields and buttons
        self.username_input = self.window.findChild(QLineEdit, "phone_no")
        self.password_input = self.window.findChild(QLineEdit, "password")
        self.login_button = self.window.findChild(QPushButton, "login")
        self.register_button = self.window.findChild(QPushButton, "regist")

        # Connect buttons to their respective functions
        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if self.authenticate(username, password):
            self.window.accept()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        # Implement registration logic here
        QMessageBox.information(self, "Register", "Registration successful")
        print(username, password)

    def authenticate(self, username, password):
        # Implement authentication logic here
        # For simplicity, using a hardcoded username and password
        return username == "user" and password == "pass"


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
        print("Main Window UI loaded successfully")

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
        auth_window = AuthWindow("authdialog.ui")
        auth_window.setWindowTitle("Login")
        if auth_window.window.exec() == QDialog.Accepted:
            print("Login successful")
            main_window = MainWindow("mainwindow.ui")
            main_window.window.show()
            sys.exit(app.exec())
        else:
            print("Login failed")
            sys.exit(0)

    except Exception as e:
        QMessageBox.critical(None, "Error", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()

# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile

def main():
    # Set the attribute before creating the QApplication instance
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    
    ui_file_path = "mainwindow.ui"
    
    try:
        ui_file = QFile(ui_file_path)
        if not ui_file.open(QFile.ReadOnly):
            raise IOError(f"Cannot open {ui_file_path}: {ui_file.errorString()}")
        
        loader = QUiLoader()
        window = loader.load(ui_file)
        ui_file.close()
        
        if window is None:
            raise RuntimeError(f"Failed to load UI file: {ui_file_path}")
        
        window.show()
        sys.exit(app.exec())
    
    except Exception as e:
        QMessageBox.critical(None, "Error", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()
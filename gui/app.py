from PyQt6 import QtWidgets
from gui.main_window import MainWindow
import sys

def run_app():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.resize(900, 650)
    w.show()
    sys.exit(app.exec())

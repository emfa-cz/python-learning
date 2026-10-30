import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 700, 300)

        label = QLabel('World(Print)"hello"', self)
        label.setFont(QFont("Arial", 20))
        label.setGeometry(59, 184, 281, 100)
        label.setStyleSheet("color: #765341;"
                            "background-color: #676767;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        label.setAlignment(Qt.AlignRight)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
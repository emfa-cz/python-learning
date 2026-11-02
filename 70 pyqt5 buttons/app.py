import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("click me", self)
        self.initUI()

    def initUI(self):
        
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 80px;")
        self.button.clicked.connect(self.onClick)

    def onClick(self):
        print("buttonm clickkdedfjshfiusef")
        self.button.setText("clickced")

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
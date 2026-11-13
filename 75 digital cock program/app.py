import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalCock(QWidget):
    def __init__(self):
        super().__init__()
        self.timeLabel = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("digital cock")
        self.setGeometry(600, 400, 300, 100)
        vbox = QVBoxLayout()
        vbox.addWidget(self.timeLabel)
        self.setLayout(vbox)
        self.timeLabel.setAlignment(Qt.AlignCenter)
        self.timeLabel.setStyleSheet("font-size: 150px;"
                                    "font-family: Comic Sans MS;"
                                    "color: brown;"
                                    )
        self.setStyleSheet("background-color: green")
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)


        self.updateTime()

    def updateTime(self):
        currentTime = QTime.currentTime().toString("hh:mm:ss AP")
        self.timeLabel.setText(currentTime)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    cock = DigitalCock()
    cock.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from PyQt5.QtCore import QTimer, QTime, Qt

class stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.timeLabel = QLabel("00:00:00.00", self)
        self.startButton = QPushButton("Start", self)
        self.stopButton = QPushButton("Stop", self)
        self.resetButton = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("stopwatch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.timeLabel)
        

        self.setLayout(vbox)
        self.timeLabel.setAlignment(Qt.AlignCenter)
        hbox = QHBoxLayout()

        hbox.addWidget(self.startButton)
        hbox.addWidget(self.stopButton)
        hbox.addWidget(self.resetButton)

        vbox.addLayout(hbox)
        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
            }
            QPushButton{
                font-size: 50px;
            }
            QLabel{
                font-size: 120px;
                background-color: orange;
                border-radius: 20px;
            }

        """)

        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.resetButton.clicked.connect(self.reset)
        self.timer.timeout.connect(self.updateDisplay)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.timeLabel.setText(self.formatTime(self.time))

    def formatTime(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        miliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{miliseconds:02}"

    def updateDisplay(self):
        self.time = self.time.addMSecs(10)
        self.timeLabel.setText(self.formatTime(self.time))







if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
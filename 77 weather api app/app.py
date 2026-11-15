import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class weatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.cityLabel = QLabel("Enter city name:", self)
        self.cityInput = QLineEdit(self)
        self.getWeatherButton = QPushButton('Get weather', self)
        self.tempLabel = QLabel(self)
        self.emojiLabel = QLabel(self)
        self.descLabel = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Weather App')
        vbox = QVBoxLayout()
        vbox.addWidget(self.cityLabel)
        vbox.addWidget(self.cityInput)
        vbox.addWidget(self.getWeatherButton)
        vbox.addWidget(self.tempLabel)
        vbox.addWidget(self.emojiLabel)
        vbox.addWidget(self.descLabel)
        self.setLayout(vbox)
        self.cityLabel.setAlignment(Qt.AlignCenter)
        self.cityInput.setAlignment(Qt.AlignCenter)
        self.tempLabel.setAlignment(Qt.AlignCenter)
        self.descLabel.setAlignment(Qt.AlignCenter)
        self.emojiLabel.setAlignment(Qt.AlignCenter)
        self.cityLabel.setObjectName('cityLabel')
        self.cityInput.setObjectName('cityInput')
        self.getWeatherButton.setObjectName('getWeatherButton')
        self.tempLabel.setObjectName('tempLabel')
        self.emojiLabel.setObjectName('emojiLabel')
        self.descLabel.setObjectName('descLabel')
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
                
            }
            QLabel#cityLabel{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#cityInput{
                font-size: 40px;
            }
            QPushButton#getWeatherButton{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#tempLabel{
                font-size: 75px;
            }
            QLabel#emojiLabel{
                font-size: 100px;
                font-family: none;
            }
            QLabel#descLabel{
                font-size: 50px;
            }
                
                            """)

        self.getWeatherButton.clicked.connect(self.getWeather)

    def getWeather(self):
        APIkey = 'c73a52fe8ae767373a53566cb9855f72'
        city = self.cityInput.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIkey}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data["cod"] == 200:
                self.displayWeather(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.displayError('Bad request\nPlease check your input')
                case 401:
                    self.displayError('Unauthorised\nInvalid API key')
                case 403:
                    self.displayError('Access forbidden\nAccess is denied')
                case 404:
                    self.displayError('Not found\nCity not found')
                case 500:
                    self.displayError('Internal server error\nPlease try again later')
                case 502:
                    self.displayError('Bad gateway\ninvalid repsons form sever')
                case 503:
                    self.displayError('service unavailabel\nserver is ownd')
                case 504:
                    self.displayError('gateuwau tineout\nno repoisne sform the nserver')
                case _:
                    print('http error occured\n{http_error}')
        except requests.exceptions.ConnectionError:
            self.displayError('connection error')
        except requests.exceptions.Timeout:
            self.displayError('timeout err')
        except requests.exceptions.TooManyRedirects:
            self.displayError('too many redirects')
        except requests.exceptions.RequestException as reqErr:
            self.displayError(f"request err")


    
    def displayError(self, msg):
        self.tempLabel.setStyleSheet("font-size: 30px")
        self.tempLabel.setText(msg)
        self.emojiLabel.clear()
        self.descLabel.clear()

    
    def displayWeather(self, data):
        self.tempLabel.setStyleSheet("font-size: 75px")
        tempeK = data['main']['temp']
        tempeC = tempeK - 273.15
        tempeF = (tempeK * 9/5) - 459.67
        weatherID = data['weather'][0]['id']
        weatherDesc = data['weather'][0]['description']
        print(data)

        self.tempLabel.setText(f"{tempeC:.1f} degrees C")
        self.emojiLabel.setText(self.getWeatherEmoji(weatherID))
        self.descLabel.setText(weatherDesc)

    @staticmethod
    def getWeatherEmoji(weatherID):
        if weatherID >= 200 and weatherID <= 232:
            return "⛈️"
        elif 300 <= weatherID <= 321:
            return "🌫️"
        elif 500 <= weatherID <= 531:
            return "💦"
        elif 600 <= weatherID <= 622:
            return "❄️"
        elif 701 <= weatherID <= 741:
            return "🌁"
        elif weatherID == 762:
            return "🌋"
        elif weatherID == 771:
            return "🌬️"
        elif weatherID == 781:
            return "🌪️"
        elif weatherID == 800:
            return "☀️"
        elif 801 <= weatherID <= 804:
            return "😶‍🌫️"
        else:
            return ""








if __name__ == '__main__':
    app = QApplication(sys.argv)
    weatherApp = weatherApp()
    weatherApp.show()
    sys.exit(app.exec_())

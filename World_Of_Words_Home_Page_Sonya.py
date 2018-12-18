# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import QFont
import sys
 

# Это добавочный класс, который будет отвечать за вывод "входной страницы"
# Данная страница будет содержать некоторую информацию о назначении нашей программы
class Say_Hello(QWidget):
    def __init__(self, parent=None):  # инициализация
        super().__init__()
        self.initUI()       
        
    def initUI(self):
        self.setGeometry(200, 100, 1000, 600) 
        self.setWindowTitle('World Of Words: home page') 
        # так будет называться наше окно
        self.setStyleSheet("background-color: #EEE8AA; color: #006400; font-family: Times;")
        # настройка цвета фона, шрифта
        self.ad_area = QLabel(self) 
        # первая метка со следующим содержанием:
        self.ad_area.setText("Добро пожаловать в нашу программу World Of Words.\
        \nВ чём же суть программы и для чего она разработана?")  
        self.ad_area.move(20, 20)
        # передвинем метку в то место, где она будет лучше смотреться
        font = QFont('Times', 18)
        # настройка размера и формата шрифта (при помощи подключённого модуля QFont 
        self.ad_area.setFont(font)   
        # и подключение параметров шрифта к тексту метки
        
        self.pixmap = QPixmap()
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(0, 0)        
        self.image.setPixmap(self.pixmap)
        # определяем некую переменную image, которая будет хранить фоторафию
        
        self.table = QLabel(self)
        # новая метка
        self.table.move(20, 60)
        self.table.resize(1400, 150)  
        self.table.setText("Вы часто сталкивались с такой проблемой, что на иностранном языке иногда бываает\
        \nочень трудно прочитать слово? С помощью World Of Words вы сможете с лёгкостью\
        \nтранслитерировать труднопроизносимые слова!\
        \nВаши преданные разработчики - Евсеева Мария и Чекмаева Софья")
        
        font2 = QFont('Times', 14)
        self.table.setFont(font2)   
        # для новой метки свой шрифт
        
    def run(self):
        self.pixmap.load('img.png')
        self.image.setPixmap(self.pixmap)
        # выгружаем фотографию
           

# чтобы код заработал и появилось всплывающее окно, пропишем следующее:        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex2 = Say_Hello()
    ex2.show()
    # показ окна
    sys.exit(app.exec())
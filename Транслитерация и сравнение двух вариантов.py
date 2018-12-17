from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLineEdit,QLabel,QLCDNumber
from PyQt5.QtGui import QPixmap
import sys
 
 
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setGeometry(100, 100, 500, 350)
        self.setWindowTitle('Транслитерация')
 
        self.table = QLCDNumber(self)
        self.table.display('')
        self.setStyleSheet("background-color: #EEE8AA; color: #191970; font-family: Times;")
        self.table.move(20, 20)
        self.table.resize(460, 50)            
        
        self.btn = QPushButton('Нажмите, когда введёте слово', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(217, 120)
        self.btn.clicked.connect(self.coding)
 
        self.label = QLabel(self)
        self.label.setText("Здесь отобразится готовый текст")
        self.label.move(40, 30)
 
        self.word_label = QLabel(self)
        self.word_label.setText("Введите слово: ")
        self.word_label.move(40, 90)
 
        self.word_input = QLineEdit(self)
        self.word_input.move(130, 90)
        self.word_input.resize(330, 20)      
        
        ## Пробую 2
        self.table2 = QLabel(self)
        self.table2.move(20, 200)
        self.table2.resize(480, 20)        
        
        self.table3 = QLabel(self)
        self.table3.move(20, 230)
        self.table3.resize(480, 20)
        
        self.table4 = QLabel(self)
        self.table4.move(20, 260)
        self.table4.resize(480, 20)
 
        self.table5 = QLabel(self)
        self.table5.move(20, 290)
        self.table5.resize(480, 20)
        
        ## Пробую
        self.ad_area = QLabel(self)
        self.ad_area.setText("Здесь Вы можете увидеть некотрую информацию о слове:")
        self.ad_area.move(20, 180)   
        
        ## Пробую в кнопки
        self.btn_to_add = QPushButton('Нажмите, чтобы увидеть данные об этом слове', self)
        self.btn_to_add.resize(self.btn_to_add.sizeHint())
        self.btn_to_add.move(132, 145)
        self.btn_to_add.clicked.connect(self.information)    
    
    
    def coding(self):
        self.d = {'А':'A', 'Б':'B', 'В':'V', 'Г':'G', 'Д':'D', 'Е':'E', 'Ё':'E', 'Ж':'Zh', 'З':'Z', 'И':'I','Й':'I','К':'K','Л':'L', 'М':'M', 'Н':'N', 'О':'O', 'П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'Kh','Ц':'Tc', 'Ч':'Ch','Ш':'Sh','Щ':'Shch', 'Ы':'Y','Э':'E','Ю':'Iu', 'Я':'Ia', 'а':'a', 'б':'b', 'в':'v', 'г':'g', 'д':'d', 'е':'e', 'ё':'e', 'ж':'zh', 'з':'z', 'и':'i','й':'i','к':'k','л':'l', 'м':'m', 'н':'n', 'о':'o', 'п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'kh','ц':'tc', 'ч':'ch','ш':'sh','щ':'shch', 'ы':'y','э':'e','ю':'iu', 'я':'ia' }
        answ = self.word_input.text()
        ans = ''
        for i in answ:
            if i in self.d:
                ans += self.d[i]
            elif i != 'ь' and i != 'Ь' and i != 'ъ' and i != 'Ъ':
                ans += i
        self.label.setText("{}".format(ans))
        self.WORD = ans
    
    def information(self):
        word_to_ad = self.WORD
        word_in_Russian = self.word_input.text()
        self.table2.setText("Оригинал: {};  транслитерация: {}".format(word_in_Russian, word_to_ad))
        self.table3.setText("Длина слова в русском варианте: {};  в транслитерированном: {}".format(len(word_in_Russian), len(word_to_ad)))
        g = ['a', 'u', 'e', 'o', 'y', 'i']
        gg = ['а', 'у', 'о', 'е', 'и', 'я', 'ю', 'ё', 'э', 'ы']
        kk = 0
        for i in word_to_ad:
            if i.lower() in g:
                kk += 1
                
        kkk = 0
        for i in word_in_Russian:
            if i.lower() in gg:
                kkk += 1
                
        self.table4.setText("Количество гласных звуков в русской версии: {};  в транслитерированной версии: {}".format(kkk, kk))
        self.table5.setText("Количество согласных звуков в русской версии: {};  в транслитерированной версии: {}".format(len(word_in_Russian) - kkk, len(word_to_ad) - kk))
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

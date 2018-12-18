# coding: utf8
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import QFont
import sys


# Это основной класс, который работает с главным окном
class The_Main_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(550, 150, 650, 350)
        self.setWindowTitle("World of Words")
        self.setStyleSheet("background-color: #EEE8AA; color: #191970; font-family: Times;")

        self.table = QLCDNumber(self)
        self.table.setStyleSheet('QLCDNumber {background-color: #FFB6C1; color: #191970;}')
        self.table.display('')
        self.table.move(10, 20)
        self.table.resize(380, 50)

        # Когда пользователь будет нажимать на эту кнопку, будет происходить транслитерация
        self.the_main_btn = QPushButton("Нажмите, когда введёте слово", self)
        self.the_main_btn.setStyleSheet('QPushButton {background-color: #8FBC8F; color: #191970;}')
        self.the_main_btn.resize(self.the_main_btn.sizeHint())
        self.the_main_btn.move(10, 120)
        self.the_main_btn.clicked.connect(self.coding)

        self.label = QLabel(self)
        self.label.setText("Здесь отобразится готовый текст")
        self.label.setStyleSheet('QLabel {background-color: #FFB6C1; color: #191970;}')
        self.label.move(20, 30)
        font = QFont('CyrillicOld', 10)
        self.label.setFont(font)

        self.word_label = QLabel(self)
        self.word_label.setText("Введите слово: ")
        self.word_label.move(10, 90)

        self.word_input = QLineEdit(self)
        self.word_input.move(100, 90)
        self.word_input.resize(290, 20)

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

        self.ad_area = QLabel(self)
        self.ad_area.setText("Здесь Вы можете увидеть некоторую информацию о слове:")
        self.ad_area.move(10, 180)
        font = QFont('CyrillicOld', 9)
        self.ad_area.setFont(font)

        self.btn_for_info = QPushButton("Нажмите, чтобы увидеть данные об этом слове", self)
        self.btn_for_info.setStyleSheet('QPushButton {background-color: #8FBC8F; color: #191970;}')
        self.btn_for_info.resize(self.btn_for_info.sizeHint())
        self.btn_for_info.move(10, 150)
        self.btn_for_info.clicked.connect(self.give_info)

        self.pixmap = QPixmap()
        self.image = QLabel(self)
        self.image.move(405, 17)
        self.image.resize(230, 200)
        self.image.setPixmap(self.pixmap)

    def coding(self):
        self.d = {'А': 'A', 'Б': 'B', 'В': 'V',
                  'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh',
                  'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
                  'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
                  'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Tc', 'Ч': 'Ch', 'Ш': 'Sh',
                  'Щ': 'Shch', 'Ы': 'Y', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia', 'а': 'a',
                  'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
                  'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm',
                  'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
                  'ф': 'f', 'х': 'kh', 'ц': 'tc', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
                  'ы': 'y', 'э': 'e', 'ю': 'iu', 'я': 'ia'
                  }

        origin = self.word_input.text().lower()
        if not all(symbol in 'йцукенгшщзхъфывапролджэячсмитьбюё' or symbol in '1234567890-_=+*&^%$#@!~№;,<.>":?\/ |' for symbol in origin):
            self.label.setText('Ой!!!')
            self.translit = origin
        else:
            answ = self.word_input.text()
            ans = ''
            for i in answ:
                if i in self.d:
                    ans += self.d[i]
                elif i != 'ь' and i != 'Ь' and i != 'ъ' and i != 'Ъ':
                    ans += i
            self.label.setText("{}".format(ans))
            self.tranclit = ans

    def give_info(self):
        # В этом методе мы будем сравнивать оригинал и транлитерацию по некоторым параметрам
        word_in_translit = self.translit.lower()
        word_in_Russian = self.word_input.text().lower()

        # Если пользователь ввел неподходящее слово или фразу, то мы не транслитерируем и уведомляем его об этом (было в т.ч. до этого)
        if word_in_translit == word_in_Russian:
            self.table2.setText("Ой, что-то пошло не так, поробуйте снова...")
            self.table3.setText("Возможно, Вы не поменяли раскладку...")
        else:
            self.table2.setText("Оригинал: {};  транслитерация: {}".format(word_in_Russian, word_in_translit))
            self.table3.setText("Количество символов в оригинале: {};  в транслитерации: {}".format(len(word_in_Russian), len(word_in_translit)))

        # Списки букв, гласных и согласных в русском и английском алфавитах
        letters_engl = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        letters_rus = [chr(i) for i in range(ord('а'), ord('я') + 1)]
        vowels_engl = ['a', 'u', 'e', 'o', 'y', 'i']
        vowels_rus = ['а', 'у', 'о', 'е', 'и', 'я', 'ю', 'ё', 'э', 'ы']
        cons_engl = list(filter(lambda letter: letter not in vowels_engl, letters_engl))
        cons_rus = list(filter(lambda letter: letter not in vowels_rus, letters_rus))

        # Защита от дурака, который ввел слово не на русском или с отличными от русских букв и приведенных ниже символов
        if not all(symbol in letters_rus or symbol in '1234567890-_=+*&^%$#@!~№;,<.>":?\/ |' for symbol in word_in_Russian):
            # Похоже на одно сообщение в несколько строк
            self.table4.setText("Или ввели недопустимые символы..")
            self.table5.setText("Будьте внимательней :))))")
            self.pixmap.load("картинка для ошибки.jpg")
            self.image.setPixmap(self.pixmap)

        else:
            # Она сделана под цвет фона, и её не видно
            self.pixmap.load("картинка на случай не ошибки.jpg")
            self.image.setPixmap(self.pixmap)
            # self.image.resize(1, 1)
            # Непосредственно нахождение количества тех или иных букв в словах
            # Сначала создали список со всеми нужными буквами, чтобы не потерять их
            vow_engl_in_word = list(filter(lambda letter: letter in vowels_engl, word_in_translit))
            num_of_vow_engl_in_word = len(vow_engl_in_word)
            vow_rus_in_word = list(filter(lambda letter: letter in vowels_rus, word_in_Russian))
            num_of_vow_rus_in_word = len(vow_rus_in_word)
            cons_engl_in_word = list(filter(lambda letter: letter in cons_engl, word_in_translit))
            num_of_cons_engl_in_word = len(cons_engl_in_word)
            cons_rus_in_word = list(filter(lambda letter: letter in cons_rus, word_in_Russian))
            num_of_cons_rus_in_word = len(cons_rus_in_word)

            self.table4.setText("Количество гласных звуков в русской версии: {};  в транслитерированной версии: {}".format(num_of_vow_rus_in_word, num_of_vow_engl_in_word))
            self.table5.setText("Количество согласных звуков в русской версии: {};  в транслитерированной версии: {}".format(num_of_cons_rus_in_word, num_of_cons_engl_in_word))
            # self.table4.setText("{}, {}".format(vow_rus, vow_engl))
            # self.table5.setText("{}, {}".format(cons_rus, cons_engl))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = The_Main_Window()
    window.show()
    sys.exit(app.exec())
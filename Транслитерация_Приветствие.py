# -*- coding: utf-8 -*-
import pygame
import sys
from pygame.locals import *

# зададим основные цвета, которые будем использовать в программе
my_green = (0, 100, 0)   # тёмно-зелёный цвет для текста
black = (0, 0, 0)
work_color = (238, 232, 170)   # бежевый как основной цвет всплывающих окон
aqua = (0, 255, 255)   # подсветка

# начинаем работу с pygame, задаём параметры (pygame.init() будет в одном из
# будущих классов
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

# запустим специальный класс Clock в модуле time
clock = pygame.time.Clock()


# следующий шаг - для каждой буквы организуем одноимённый класс
class P(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        # загрузка картинки
        self.image = pygame.image.load(filename).convert()
        # задаём нужные размеры
        self.image1 = pygame.transform.scale(self.image, (150, 150))
        # делаем фон прозрачным, чтобы осталась только буква
        self.image1.set_colorkey((0, 0, 0))
        # задаём положения спрайта в окне
        self.rect = self.image1.get_rect(center=(125, 150))
f = P(200, 'P.png')   # используя класс, обработаем картинку P.png


# аналогично с последующими спрайтами
class L(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image2 = pygame.transform.scale(self.image, (150, 140))
        self.image2.set_colorkey((0, 0, 0))
        self.rect2 = self.image2.get_rect(center=(320, 150))
f2 = L(200, 'L.png')


class A(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image3 = pygame.transform.scale(self.image, (150, 150))
        self.image3.set_colorkey((0, 0, 0))
        self.rect3 = self.image3.get_rect(center=(500, 150))
f3 = A(200, 'A.png')


class Y(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image4 = pygame.transform.scale(self.image, (150, 150))
        self.image4.set_colorkey((0, 0, 0))
        self.rect4 = self.image4.get_rect(center=(700, 150))
f4 = Y(200, 'Y.png')


# здесь начинается работа с самим окном (это окно № 1)
class HELLO_PYGAME(object):
    def __init__(self):
        # обязательная инициализация
        pygame.init()
        # делаем возможным применение в программе нескольких видов шрифтов
        font = pygame.font.Font(None, 50)
        # мы решили, что наиболее подходящий шрифт - Times
        self.font = pygame.font.SysFont('Times', 25)
        # у обоих окон будет соответствующий теме заголовок, поскольку
        # приложение называется World Of Words
        pygame.display.set_caption('World Of Words (official app)')
        # далее идёт инициализация окна экрана для отображения
        self.screen = pygame.display.set_mode((width, height), 0, 32)
        self.screen.fill(work_color)
        pygame.display.update()
        self.text = font.render("Hello  from  World  Of  Words!", 1,
                                (0, 100, 0))

        # Внимание! следующие данные понадобятся нам, чтобы вокруг текста
        # с приветствием нарисовать рамку (но сам метод рисования будет
        # описан в функции ниже
        self.text_x = width // 2 - self.text.get_width() // 2
        self.text_y = height // 2 - self.text.get_height() // 2
        self.text_w = self.text.get_width()
        self.text_h = self.text.get_height()
        # self.screen.blit(self.text, (self.text_x, self.text_y))

    # а вот и функция для отрисовки рамки
    def addRect(self):
        self.rect = pygame.draw.rect(self.screen, (0, 100, 0),
                                     (self.text_x - 10, self.text_y - 10,
                                      self.text_w + 20, self.text_h + 20), 1)
        pygame.display.update()

    # для фотографии, которая будет на второй странице, я решила выделить не
    # класс, а отдельную функцию
    def addImageOnSecondPage(self):
            self.play_surf = pygame.image.load('second.png')
            self.play_surf2 = pygame.transform.scale(self.play_surf,
                                                     (450, 150))
            self.play_rect = self.play_surf.get_rect(center=(400, 300))
            self.screen.blit(self.play_surf, self.play_rect)

    # небольшое дополнение - пара красных стрелок, чтобы пользователь видел,
    # что ему необходимо сделать
    def addArrows(self):
        # 1 стрелка
        pygame.draw.line(self.screen, (255, 0, 0), (150, 328), (150, 380), 2)
        pygame.draw.line(self.screen, (255, 0, 0), (150, 380), (140, 360), 2)
        pygame.draw.line(self.screen, (255, 0, 0), (150, 380), (160, 360), 2)

        # 2 стрелка
        pygame.draw.line(self.screen, (255, 0, 0), (650, 328), (650, 380), 2)
        pygame.draw.line(self.screen, (255, 0, 0), (650, 380), (640, 360), 2)
        pygame.draw.line(self.screen, (255, 0, 0), (650, 380), (660, 360), 2)
        pygame.display.update()

    # текст для 1 окна
    def addText(self):
        self.screen.blit(self.text, (self.text_x, self.text_y))
        self.screen.blit(
            self.font.render('После прочтения, пожалуйста, нажмите пробел :)',
                             True, my_green), (self.text_x - 15,
                                               self.text_y + 100)
        )
        pygame.display.update()

    # текст для 2 окна
    def addText2(self):
        self.screen.blit(self.font.render(
            'Приветствуем вас на новом этапе World Of Words!',
            True, (0, 0, 0)), (100, 220))

        self.screen.blit(self.font.render(
            'В этот раз мы подготовили пользователям ещё кое-что интересное.',
            True, (0, 0, 0)), (10, 250))

        self.screen.blit(self.font.render(
            'Вам предстоит показать, насколько хорошо вы можете воспроизвести',
            True, (0, 0, 0)), (10, 280))

        self.screen.blit(self.font.render(
            'самое трудное из слов, которые вводили ранее. Звучит трудно? ',
            True, (0, 0, 0)), (10, 310))

        self.screen.blit(self.font.render('Тогда чего же мы ждём? ',
                                          True, (0, 0, 0)), (250, 340))
        pygame.display.update()

    # и самое главное - функция, без которой наше приложение не заработает
    def functionApp(self):
        if __name__ == '__main__':
            # добавляем часть элементов на первое окно
            self.addRect()
            self.addText()
            self.addArrows()

            # используя time, добавляем заготовленные спрайты
            pygame.time.wait(800)
            screen.blit(f.image1, f.rect)
            pygame.display.update()
            pygame.time.wait(800)
            screen.blit(f2.image2, f2.rect2)
            pygame.display.update()
            pygame.time.wait(800)
            screen.blit(f3.image3, f3.rect3)
            pygame.display.update()
            pygame.time.wait(800)
            screen.blit(f4.image4, f4.rect4)
            pygame.display.update()

            # ПЕРВЫЙ ПОВОРОТ БУКВ
            pygame.time.wait(1000)
            rot_P = pygame.transform.rotate(f.image1, 45)
            rot_P_rect = rot_P.get_rect(center=((125, 150)))
            pygame.draw.rect(screen, work_color, (0, 0, 200, 250), 0)
            screen.blit(rot_P, rot_P_rect)
            pygame.display.update()

            rot_L = pygame.transform.rotate(f2.image2, 45)
            rot_L_rect = rot_L.get_rect(center=((320, 126)))
            pygame.draw.rect(screen, work_color, (225, 0, 180, 250), 0)
            screen.blit(rot_L, rot_L_rect)

            rot_A = pygame.transform.rotate(f3.image3, 25)
            rot_A_rect = rot_A.get_rect(center=((500, 150)))
            pygame.draw.rect(screen, work_color, (425, 0, 160, 250), 0)
            screen.blit(rot_A, rot_A_rect)

            rot_Y = pygame.transform.rotate(f4.image4, 45)
            rot_Y_rect = rot_Y.get_rect(center=((700, 150)))
            pygame.draw.rect(screen, work_color, (600, 0, 200, 250), 0)
            screen.blit(rot_Y, rot_Y_rect)
            pygame.display.update()

            # ВТОРОЙ ПОВОРОТ БУКВ
            pygame.time.wait(300)
            rot_P = pygame.transform.rotate(f.image1, 90)
            rot_P_rect = rot_P.get_rect(center=((125, 150)))
            pygame.draw.rect(screen, work_color, (0, 0, 200, 250), 0)
            screen.blit(rot_P, rot_P_rect)
            pygame.display.update()

            rot_L = pygame.transform.rotate(f2.image2, 90)
            rot_L_rect = rot_L.get_rect(center=((320, 126)))
            pygame.draw.rect(screen, work_color, (220, 0, 202, 250), 0)
            screen.blit(rot_L, rot_L_rect)

            rot_A = pygame.transform.rotate(f3.image3, 90)
            rot_A_rect = rot_A.get_rect(center=((500, 150)))
            pygame.draw.rect(screen, work_color, (425, 0, 180, 250), 0)
            screen.blit(rot_A, rot_A_rect)

            rot_Y = pygame.transform.rotate(f4.image4, 90)
            rot_Y_rect = rot_Y.get_rect(center=((700, 150)))
            pygame.draw.rect(screen, work_color, (600, 0, 200, 250), 0)
            screen.blit(rot_Y, rot_Y_rect)
            pygame.display.update()

            # ТРЕТИЙ ПОВОРОТ БУКВ
            pygame.time.wait(300)
            rot_P = pygame.transform.rotate(f.image1, 135)
            rot_P_rect = rot_P.get_rect(center=((125, 150)))
            pygame.draw.rect(screen, work_color, (0, 0, 200, 250), 0)
            screen.blit(rot_P, rot_P_rect)
            pygame.display.update()

            rot_L = pygame.transform.rotate(f2.image2, 115)
            rot_L_rect = rot_L.get_rect(center=((320, 126)))
            pygame.draw.rect(screen, work_color, (220, 0, 202, 250), 0)
            screen.blit(rot_L, rot_L_rect)

            rot_A = pygame.transform.rotate(f3.image3, 135)
            rot_A_rect = rot_A.get_rect(center=((500, 150)))
            pygame.draw.rect(screen, work_color, (425, 0, 180, 250), 0)
            screen.blit(rot_A, rot_A_rect)

            rot_Y = pygame.transform.rotate(f4.image4, 135)
            rot_Y_rect = rot_Y.get_rect(center=((700, 150)))
            pygame.draw.rect(screen, work_color, (600, 0, 200, 250), 0)
            screen.blit(rot_Y, rot_Y_rect)
            pygame.display.update()

            # ЧЕТВЁРТЫЙ ПОВОРОТ БУКВ
            pygame.time.wait(300)
            rot_P = pygame.transform.rotate(f.image1, 180)
            rot_P_rect = rot_P.get_rect(center=((125, 150)))
            pygame.draw.rect(screen, work_color, (0, 0, 225, 250), 0)
            screen.blit(rot_P, rot_P_rect)
            pygame.display.update()

            rot_L = pygame.transform.rotate(f2.image2, 180)
            rot_L_rect = rot_L.get_rect(center=((320, 150)))
            pygame.draw.rect(screen, work_color, (220, 0, 202, 250), 0)
            screen.blit(rot_L, rot_L_rect)

            rot_A = pygame.transform.rotate(f3.image3, 180)
            rot_A_rect = rot_A.get_rect(center=((500, 150)))
            pygame.draw.rect(screen, work_color, (425, 0, 180, 250), 0)
            screen.blit(rot_A, rot_A_rect)

            rot_Y = pygame.transform.rotate(f4.image4, 180)
            rot_Y_rect = rot_Y.get_rect(center=((675, 150)))
            pygame.draw.rect(screen, work_color, (600, 0, 200, 255), 0)
            screen.blit(rot_Y, rot_Y_rect)
            pygame.display.update()

            # ПЯТЫЙ ПОВОРОТ БУКВ
            pygame.time.wait(300)
            rot_P = pygame.transform.rotate(f.image1, 225)
            rot_P_rect = rot_P.get_rect(center=((125, 150)))
            pygame.draw.rect(screen, work_color, (0, 0, 200, 250), 0)
            screen.blit(rot_P, rot_P_rect)
            pygame.display.update()

            rot_L = pygame.transform.rotate(f2.image2, 225)
            rot_L_rect = rot_L.get_rect(center=((320, 170)))
            pygame.draw.rect(screen, work_color, (225, 0, 180, 250), 0)
            screen.blit(rot_L, rot_L_rect)

            rot_A = pygame.transform.rotate(f3.image3, 200)
            rot_A_rect = rot_A.get_rect(center=((500, 150)))
            pygame.draw.rect(screen, work_color, (425, 0, 160, 250), 0)
            screen.blit(rot_A, rot_A_rect)

            rot_Y = pygame.transform.rotate(f4.image4, 225)
            rot_Y_rect = rot_Y.get_rect(center=((660, 125)))
            pygame.draw.rect(screen, work_color, (600, 0, 200, 250), 0)
            screen.blit(rot_Y, rot_Y_rect)
            pygame.display.update()

            # ШЕСТОЙ ПОВОРОТ БУКВ
            pygame.time.wait(300)
            rot_P = pygame.transform.rotate(f.image1, 270)
            rot_P_rect = rot_P.get_rect(center=((125, 150)))
            pygame.draw.rect(screen, work_color, (0, 0, 215, 250), 0)
            screen.blit(rot_P, rot_P_rect)
            pygame.display.update()

            rot_L = pygame.transform.rotate(f2.image2, 270)
            rot_L_rect = rot_L.get_rect(center=((320, 150)))
            pygame.draw.rect(screen, work_color, (220, 0, 202, 250), 0)
            screen.blit(rot_L, rot_L_rect)

            rot_A = pygame.transform.rotate(f3.image3, 270)
            rot_A_rect = rot_A.get_rect(center=((500, 150)))
            pygame.draw.rect(screen, work_color, (420, 0, 180, 250), 0)
            screen.blit(rot_A, rot_A_rect)

            rot_Y = pygame.transform.rotate(f4.image4, 270)
            rot_Y_rect = rot_Y.get_rect(center=((690, 150)))
            pygame.draw.rect(screen, work_color, (600, 0, 200, 250), 0)
            screen.blit(rot_Y, rot_Y_rect)
            pygame.display.update()

            # СЕДЬМОЙ ПОВОРОТ БУКВ
            pygame.time.wait(300)
            rot_P = pygame.transform.rotate(f.image1, 315)
            rot_P_rect = rot_P.get_rect(center=((125, 150)))
            pygame.draw.rect(screen, work_color, (0, 0, 200, 250), 0)
            screen.blit(rot_P, rot_P_rect)
            pygame.display.update()

            rot_L = pygame.transform.rotate(f2.image2, 295)
            rot_L_rect = rot_L.get_rect(center=((320, 140)))
            pygame.draw.rect(screen, work_color, (225, 0, 180, 250), 0)
            screen.blit(rot_L, rot_L_rect)

            rot_A = pygame.transform.rotate(f3.image3, 315)
            rot_A_rect = rot_A.get_rect(center=((500, 120)))
            pygame.draw.rect(screen, work_color, (425, 0, 160, 250), 0)
            screen.blit(rot_A, rot_A_rect)

            rot_Y = pygame.transform.rotate(f4.image4, 315)
            rot_Y_rect = rot_Y.get_rect(center=((660, 150)))
            pygame.draw.rect(screen, work_color, (600, 0, 200, 250), 0)
            screen.blit(rot_Y, rot_Y_rect)
            pygame.display.update()

            # ВОСЬМОЙ ПОВОРОТ БУКВ
            pygame.time.wait(300)
            rot_P = pygame.transform.rotate(f.image1, 360)
            rot_P_rect = rot_P.get_rect(center=((125, 150)))
            pygame.draw.rect(screen, work_color, (0, 0, 225, 250), 0)
            screen.blit(rot_P, rot_P_rect)
            pygame.display.update()

            rot_L = pygame.transform.rotate(f2.image2, 360)
            rot_L_rect = rot_L.get_rect(center=((320, 150)))
            pygame.draw.rect(screen, work_color, (225, 0, 180, 250), 0)
            screen.blit(rot_L, rot_L_rect)

            rot_A = pygame.transform.rotate(f3.image3, 360)
            rot_A_rect = rot_A.get_rect(center=((500, 150)))
            pygame.draw.rect(screen, work_color, (405, 0, 160, 250), 0)
            screen.blit(rot_A, rot_A_rect)

            rot_Y = pygame.transform.rotate(f4.image4, 360)
            rot_Y_rect = rot_Y.get_rect(center=((675, 150)))
            pygame.draw.rect(screen, work_color, (585, 0, 200, 255), 0)
            screen.blit(rot_Y, rot_Y_rect)
            pygame.display.update()

            # ИСЧЕЗАНИЕ БУКВ
            w = 0
            h = 0
            for i in range(40):
                pygame.time.wait(75)
                pygame.draw.rect(screen, work_color, (w, 0, w + 10, 255), 0)
                w += 10
                pygame.display.update()

            # ПОЯВЛЕНИЕ НАДПИСИ
            pygame.time.wait(100)
            screen.blit(f.image1, f.rect)
            screen.blit(f2.image2, f2.rect2)
            screen.blit(f3.image3, f3.rect3)
            screen.blit(f4.image4, f4.rect4)
            pygame.display.update()

            # ПРЫГАЮЩИЕ БУКВЫ
            pygame.time.wait(800)
            P = f.image1.get_rect(center=(125, 100))
            pygame.draw.rect(screen, work_color, (0, 0, 225, 250), 0)
            screen.blit(f.image1, P)
            pygame.display.update()
            pygame.time.wait(100)
            pygame.draw.rect(screen, work_color, (0, 0, 225, 250), 0)
            screen.blit(f.image1, f.rect)
            pygame.display.update()

            pygame.time.wait(200)
            L = f2.image2.get_rect(center=(320, 100))
            pygame.draw.rect(screen, work_color, (225, 0, 180, 250), 0)
            screen.blit(f2.image2, L)
            pygame.display.update()
            pygame.time.wait(100)
            pygame.draw.rect(screen, work_color, (225, 0, 180, 250), 0)
            screen.blit(f2.image2, f2.rect2)
            pygame.display.update()

            pygame.time.wait(200)
            A = f3.image3.get_rect(center=(500, 100))
            pygame.draw.rect(screen, work_color, (425, 0, 160, 250), 0)
            screen.blit(f3.image3, A)
            pygame.display.update()
            pygame.time.wait(100)
            pygame.draw.rect(screen, work_color, (425, 0, 160, 250), 0)
            screen.blit(f3.image3, f3.rect3)
            pygame.display.update()

            pygame.time.wait(200)
            Y = f4.image4.get_rect(center=(700, 100))
            pygame.draw.rect(screen, work_color, (600, 0, 200, 250), 0)
            screen.blit(f4.image4, Y)
            pygame.display.update()
            pygame.time.wait(100)
            pygame.draw.rect(screen, work_color, (600, 0, 200, 250), 0)
            screen.blit(f4.image4, f4.rect4)
            pygame.display.update()

            # главный цикл
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        # отслеживается нажатие пользователем пробела
                        if event.key == pygame.K_SPACE:
                            # новое окно с добавлением новых элементов
                            self.screen.fill((238, 232, 170))
                            self.addImageOnSecondPage()
                            # чтобы слова во 2 окне было видно за картинкой:
                            pygame.draw.rect(screen, work_color,
                                             (500, 225, 800, 17), 0)
                            pygame.draw.rect(screen, work_color,
                                             (0, 230, 500, 16), 0)
                            pygame.draw.rect(screen, work_color,
                                             (0, 259, 800, 16), 0)
                            pygame.draw.rect(screen, work_color,
                                             (0, 289, 800, 15), 0)
                            pygame.draw.rect(screen, work_color,
                                             (0, 319, 400, 18), 0)
                            pygame.draw.rect(screen, work_color,
                                             (400, 319, 100, 15), 0)
                            pygame.draw.rect(screen, work_color,
                                             (500, 316, 100, 20), 0)
                            pygame.draw.rect(screen, work_color,
                                             (300, 349, 150, 15), 0)
                            pygame.draw.rect(screen, work_color,
                                             (450, 349, 50, 17), 0)
                            self.addText2()

                            # ПОДСВЕТКА
                            choice = [aqua, work_color]
                            pygame.time.wait(1000)
                            k = 0
                            for i in range(36):
                                pygame.draw.line(self.screen, choice[k],
                                                 (140, 555), (655, 555), 5)
                                pygame.draw.line(self.screen, choice[k],
                                                 (141, 555), (141, 423), 5)
                                pygame.draw.line(self.screen, choice[k],
                                                 (141, 424), (198, 424), 5)
                                pygame.draw.line(self.screen, choice[k],
                                                 (207, 424), (330, 424), 5)
                                pygame.draw.line(self.screen, choice[k],
                                                 (339, 424), (440, 424), 5)
                                pygame.draw.line(self.screen, choice[k],
                                                 (449, 424), (592, 424), 5)
                                pygame.draw.line(self.screen, choice[k],
                                                 (601, 424), (658, 424), 5)
                                pygame.draw.line(self.screen, choice[k],
                                                 (658, 424), (658, 555), 5)
                                pygame.display.update()
                                if k == 1:
                                    k = 0
                                elif k == 0:
                                    k = 1
                                if i % 6 == 0:
                                    pygame.time.wait(1000)
                                else:
                                    pygame.time.wait(500)


display = HELLO_PYGAME()
display.functionApp()

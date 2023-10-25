#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ModelWindow:
    def __init__(self, title, x, y, width, height, color, visibility=True, with_border=True):
        self.title = title
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.visibility = visibility
        self.with_border = with_border

    # перемещение окна по горизонтали
    def move_horizontal(self, distance):
        new_x = self.x + distance
        if new_x >= 0 and new_x + self.width <= screen_width:  # Проверка на границы экрана по горизонтали
            self.x = new_x

    # перемещение окна по вертикали
    def move_vertical(self, distance):
        new_y = self.y + distance
        if new_y >= 0 and new_y + self.height <= screen_height:  # Проверка на границы экрана по вертикали
            self.y = new_y
    
    # изменение размера окна
    def resize(self, new_width, new_height):
        if self.x + new_width <= screen_width and self.y + new_height <= screen_height:  
            self.width = new_width
            self.height = new_height

    # изменение цвета
    def change_color(self, new_color):
        self.color = new_color

    # именение видимости
    def change_visibility(self, new_visibility):
        self.visibility = new_visibility


    def toggle_border(self):
        self.with_border = not self.with_border

    def display(self):
        return {
            'title': self.title,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'color': self.color,
            'visibility': self.visibility,
            'with_border': self.with_border
        }

# Пример использования класса ModelWindow
if __name__ == "__main__":
    screen_width = 800
    screen_height = 600

    window1 = ModelWindow("Window 1", 100, 100, 200, 150, "blue", "visible", True)
    #првоверка работы создания объекта
    print(window1.display())
    window1.move_horizontal(50)
    window1.move_vertical(30)
    window1.resize(250, 200)
    window1.change_color("red")
    window1.change_visibility("hidden")
    window1.toggle_border()
    #проверка работы методов класса ModelWindow
    print(window1.display())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Pair:
    def __init__(self, first, second):
        if not isinstance(first, float) or not isinstance(second, float):
            raise ValueError("Both 'first' and 'second' numbers")
        self.first = first
        self.second = second

    # Возведение в степень
    def power(self):
        result = self.first**self.second
        return result

    # Вывод на экран
    def display(self):
        print(
            f"Pair: first = {self.first}, second = {self.second}, result = {self.power()}"
        )

    # Ввод значений с клавиатуры
    def read():
        try:
            first = float(input("Enter the first number: "))
            second = float(input("Enter the second number: "))
            return Pair(first, second)
        except ValueError:
            print("Invalid input")
            return None


# Создание объекта Pair
def make_pair(first, second):
    return Pair(first, second)


if __name__ == "__main__":
    pair = Pair.read()
    pair.display()
    make_pair(3.0, 4.0).display()

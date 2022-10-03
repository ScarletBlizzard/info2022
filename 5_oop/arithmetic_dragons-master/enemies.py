# coding: utf-8
# license: GPLv3 
from gameunit import *
from random import randint, choice 


class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_colors)
    enemy = RandomEnemyType()
    return enemy


def generate_enemy_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def factor(x):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0: factors.append(x)
    return factors


class Dragon(Enemy):
    _type = 'дракон' 

    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == str(self.__answer)


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest


class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'чёрный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + 'x' + str(y)
        self.set_answer(x * y)
        return self.__quest


class Troll(Enemy):
    _type = 'тролль' 

    def set_answer(self, answer):
        self._answer = answer

    def check_answer(self, answer):
        return str(answer).lower() == str(self._answer)


class GuessTroll(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'серый'

    def question(self):
        self.__quest = "Угадай число от 1 до 5"
        self.set_answer(randint(1,5))
        return self.__quest


class PrimeTroll(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'синий'

    def question(self):
        x = randint(1,100)
        self.__quest = f"Число {x} простое?"
        self.set_answer("да" if is_prime(x) else "нет")
        return self.__quest


class FactorTroll(Troll):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'жёлтый'

    def question(self):
        x = randint(1,100)
        self.__quest = f"Разложи {x} на множители"
        self.set_answer(factor(x).sort())
        return self.__quest

    def check_answer(self, answer):
        return self._answer == answer.split(",").sort()
    

enemy_colors = [
        GreenDragon,
        RedDragon,
        BlackDragon,
        GuessTroll,
        PrimeTroll,
        FactorTroll
]

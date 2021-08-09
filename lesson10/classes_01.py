"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы: переопределить магические методы сравнения (==, !=, >=, <=, <, >).
"""


class MyTime:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

        self.overall = hours * 60 * 60 + minutes * 60 + seconds

    def __eq__(self, other):
        self.overall == other.overall

    def __ne__(self, other):
        self.overall == other.overall

    def __lt__(self, other):
        self.overall == other.overall

    def __gt__(self, other):
        self.overall == other.overall
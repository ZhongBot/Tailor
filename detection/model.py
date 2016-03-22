from enum import Enum


class PatternType(Enum):
    Stripe = 1
    Dot = 2
    Solid = 3
    Check = 4


class Entry:
    def __init__(self, pattern_type, sobel, sums):
        self.pattern_type = pattern_type
        self.sobel = sobel
        self.sums = sums


class Sobel:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class SobelSum:
    def __init__(self, x, y):
        self.x = x
        self.y = y

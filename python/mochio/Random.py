from random import randint


def randoms(length: int, min: int = 0, max: int = 100):
    return [randint(min, max) for _ in range(length)]


def percentage(min: int = 0, max: int = 100) -> int:
    return randint(0, 100)

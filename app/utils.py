from random import random


def get_chance(probability: float) -> bool:
    return random() < probability

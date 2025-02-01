import random


def randomize_time(value: float) -> float:
    return value + random.choice([-0.005, 0.005])


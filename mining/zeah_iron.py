import random
import pyautogui as pag
import time
from utils.util import randomize_time


def move_and_click(coords):
    """
    Moves the mouse to each (x, y) coordinate row by row in a randomized order (left to right or right to left).

    :param coords: List of tuples containing (x, y) positions
    """
    rows = [coords[i:i + 4] for i in range(0, len(coords), 4)]  # Split into rows of 4 points

    for row in rows:
        if random.choice([True, False]):  # Randomly decide row order
            row = row[::-1]  # Reverse the row order

        for x, y in row:
            pag.moveTo(x, y, duration=0.002)
            pag.click()
            time.sleep(0.0001)  # Wait 0.2 seconds before moving to the next point

def three_iron_ores():
    delay = random.uniform(1.01, 1.2)

    # pag.moveTo(806, 388, randomize_time(0.1))
    pag.moveTo(1097, 617, randomize_time(0.1))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(delay)

    # pag.moveTo(1077, 584, randomize_time(0.1))
    pag.moveTo(832, 391, randomize_time(0.1))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(delay)

    # pag.moveTo(835, 828, randomize_time(0.1))
    pag.moveTo(601, 646, randomize_time(0.1))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(delay)

reps = 121

for i in range(1, reps + 1):
    print(i)
    coordinates = [
        # (1507, 650), (1575, 644),
        (1360, 631), (1430, 635), (1494, 634), (1550, 634),
        (1360, 671), (1430, 695), (1494, 674), (1550, 694),
        (1384, 745), (1448, 746), (1504, 745), (1575, 747),
        (1386, 803), (1448, 802), (1507, 801), (1575, 804),
        (1386, 851), (1448, 850), (1507, 852), (1575, 853),
        (1386, 901), (1448, 900), (1507, 903), (1575, 902),
        (1386, 950), (1448, 951), (1507, 953), (1575, 952),
    ]
    move_and_click(coordinates)

    for j in range(1, 9):
        three_iron_ores()
        time.sleep(random.uniform(1.02, 1.06))







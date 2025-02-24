import random
import pyautogui as pag
import time
from utils.util import randomize_time


# fish spot
# 828, 563

# 1507, 650
# 1575, 644

# 1386, 699
# 1448, 695
# 1507, 699
# 1575, 694

# 1386, 745
# 1448, 746
# 1507, 745
# 1575, 747


# def move_and_click(coords):
#     """
#     Moves the mouse to each (x, y) coordinate in the given list and clicks.
#
#     :param coords: List of tuples containing (x, y) positions
#     """
#     for x, y in coords:
#         pag.moveTo(x, y, duration=0.2)
#         pag.click()
#         time.sleep(0.05)  # Wait 0.2 seconds before moving to the next point


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
            pag.moveTo(x, y, duration=0.07)
            pag.click()
            time.sleep(0.07)  # Wait 0.2 seconds before moving to the next point

reps = 90

for i in range(1, reps + 1):
    print(i)
    # start
    pag.moveTo(828, 563, randomize_time(0.1))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(111)

    coordinates = [
        # (1507, 650), (1575, 644),
        (1386, 699), (1448, 695), (1507, 699), (1575, 694),
        (1386, 745), (1448, 746), (1507, 745), (1575, 747),
        (1386, 803), (1448, 802), (1507, 801), (1575, 804),
        (1386, 851), (1448, 850), (1507, 852), (1575, 853),
        (1386, 901), (1448, 900), (1507, 903), (1575, 902),
        (1386, 950), (1448, 951), (1507, 953), (1575, 952),
    ]
    move_and_click(coordinates)





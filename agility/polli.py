
import pyautogui as pag
import time
from utils.util import randomize_time


# minimap click 1507, 226
# start 710, 735
# 1 788, 360
# 2 959, 387
# 3 940, 532
# 4 893, 483
# 5 725, 510
# 6 600, 462
# 7 884, 391
# 8 965, 518

laps = 40

for i in range(1, laps + 1):
    print(i)
    # climb
    pag.moveTo(1507, 226, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(10.85)

    # start
    pag.moveTo(710, 735, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(5.15)

    # 1
    pag.moveTo(788, 360, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(4.95)

    # 2
    pag.moveTo(959, 387, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(5.05)

    # 3
    pag.moveTo(940, 532, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(3.8)

    # 4
    pag.moveTo(893, 483, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(5.55)

    # 5
    pag.moveTo(725, 510, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(3.95)

    # 6
    pag.moveTo(600, 462, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(8.15)

    # 7
    pag.moveTo(884, 391, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(4.91)

    # 8
    pag.moveTo(965, 518, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(4.85)
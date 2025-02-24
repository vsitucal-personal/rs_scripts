
import pyautogui as pag
import time
from utils.util import randomize_time


# start 1275, 514
# 1 905, 649
# 2 981, 448
# 3 856, 454
# 4 949, 496
# 5 979, 406
# 6 771, 618
# 7 832, 527
# 8 920, 471
# 9 873, 440
# 10 1052, 475
# 11 892, 361

laps = 19

inv1 = 1505, 698
inv2 = 1562, 700
inv_int = 0

for i in range(1, laps + 1):
    print(i)
    # start
    pag.moveTo(1275, 514, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(6)

    # 1
    pag.moveTo(905, 649, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(13.1)

    # 2
    pag.moveTo(856, 454, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(5)

    # 3
    pag.moveTo(828, 418, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(4.6)

    # 4
    pag.moveTo(828, 498, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(4.8)

    # 5
    pag.moveTo(854, 397, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(3.3)

    # 6
    pag.moveTo(656, 613, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(8.2)

    # 7
    pag.moveTo(717, 526, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(7)

    # 8
    pag.moveTo(794, 467, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(6.7)

    # 9
    pag.moveTo(756, 443, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(6.7)

    # 10
    pag.moveTo(933, 467, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(6.6)

    # 11
    pag.moveTo(764, 353, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(6.7)

    if i % 4 == 0:
        if i == 4:
            inv_int = 1

        time.sleep(0.25)
        move = inv1 if inv_int == 0 else inv1
        pag.moveTo(move, randomize_time(0.6))
        time.sleep(randomize_time(0.25))
        pag.click()
        time.sleep(0.5)

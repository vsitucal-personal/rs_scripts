
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

laps = 35

inv1 = 1505, 698
inv2 = 1562, 700
inv3 = 1449, 694
inv4 = 1394, 698
inv_int = 0
x, y = inv1

for i in range(1, laps + 1):
    print(i)
    # start
    pag.moveTo(985, 495, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(4.55)

    # 1
    pag.moveTo(804, 264, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(7.95)

    # 2
    pag.moveTo(703, 533, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(5.85)

    # 3
    pag.moveTo(729, 524, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(2.4)

    # 4
    pag.moveTo(823, 715, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(3.6)

    # 5
    pag.moveTo(943, 848, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(6.2)

    # 6
    pag.moveTo(845, 549, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(9.6)

    if i % 4 == 0:
        time.sleep(0.25)

        if i == 12:
            x, y = inv2

        if i == 20:
            x, y = inv3

        if i == 28:
            x, y = inv4

        pag.moveTo(x, y, randomize_time(0.6))
        time.sleep(randomize_time(0.25))
        pag.click()
        time.sleep(0.5)




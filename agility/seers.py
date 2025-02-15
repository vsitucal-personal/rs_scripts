import pyautogui as pag
import time
from utils.util import randomize_time


# climb 1335, 55
# jump gap 554, 446
# tight 718, 699
# jump gap 2 843, 653
# jump gap 3 544, 618
# finish 871, 588

for i in range(1, 2):
    print(i)
    # climb
    pag.moveTo(1335, 55, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(16)

    # jump gap
    pag.moveTo(554, 446, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(6)

    # tight
    pag.moveTo(718, 699, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(8.2)

    # gap 2
    pag.moveTo(843, 653, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(4.6)

    # gap 3
    pag.moveTo(544, 618, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(4.6)

    # fin
    pag.moveTo(871, 588, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    time.sleep(3.4)
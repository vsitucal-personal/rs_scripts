import pyautogui as pag
import time
from utils.util import randomize_time

# bow string 649, 197
# mage long 688, 195
# bank 737, 649
# deposit 898, 815
# inv 1 1484, 754
# inv 2 1562, 861

for i in range(1, 100):
    print(i)
    # bank
    pag.moveTo(737, 649, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    # deposit
    pag.moveTo(898, 815, randomize_time(0.6))
    time.sleep(randomize_time(0.5))
    pag.click()

    # bowstring
    pag.moveTo(649, 197, randomize_time(0.4))
    time.sleep(randomize_time(0.3))
    pag.click()

    # mage long
    pag.moveTo(688, 195, randomize_time(0.4))
    time.sleep(randomize_time(0.3))
    pag.click()

    time.sleep(randomize_time(0.4))
    pag.press('esc')

    # inv 1
    pag.moveTo(1484, 754, randomize_time(0.4))
    time.sleep(randomize_time(0.3))
    pag.click()

    # inv 2
    pag.moveTo(1562, 861, randomize_time(0.4))
    time.sleep(randomize_time(0.3))
    pag.click()

    time.sleep(randomize_time(0.9))
    pag.press('space')

    time.sleep(randomize_time(18))

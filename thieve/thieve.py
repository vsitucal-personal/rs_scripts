import threading
import pyautogui
import time
import keyboard
import sys
import winsound

clicking = False
start_time = None

def click_veil_and_pouch():
    original_pos = pyautogui.position()

    time.sleep(1.5)
    pyautogui.click(x=1364, y=619)
    time.sleep(0.75)
    pyautogui.press('1')
    pyautogui.click(x=1361, y=764)

    pyautogui.press('2')
    pyautogui.moveTo(original_pos)
    time.sleep(1.1)

def spam_left_click():
    global start_time
    last_special_click = 0

    while True:
        if clicking:
            if start_time is None:
                start_time = time.time()

            elapsed = time.time() - start_time
            if elapsed >= 60*16:  # 10 minutes
                print("x minutes elapsed. Exiting...")
                winsound.Beep(2500, 4000)
                sys.exit()

            current_time = time.time()
            if current_time - last_special_click >= 60:
                click_veil_and_pouch()
                last_special_click = current_time

            pyautogui.click(button='left')
            time.sleep(0.05)
        else:
            time.sleep(0.1)

def toggle_clicking():
    global clicking, start_time
    clicking = not clicking
    if clicking:
        start_time = time.time()
    print("Clicking mode:", "ON" if clicking else "OFF")

threading.Thread(target=spam_left_click, daemon=True).start()
keyboard.add_hotkey('`', toggle_clicking)

print("Press ` (tilde) to toggle. Press ESC to quit early.")
keyboard.wait('esc')

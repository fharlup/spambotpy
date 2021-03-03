import pyautogui
import time
bacot="ayo bangun sayang"
for _ in range (50):
    pyautogui.typewrite(bacot)
    pyautogui.press('enter')
    time.sleep(1)

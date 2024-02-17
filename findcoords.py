import pyautogui
import time

x, y = pyautogui.position()
while True:
    new_x, new_y = pyautogui.position()
    # if new_x != x or new_y != y:
    #     break
    print("Mauszeiger an Position: x={}, y={}".format(new_x, new_y))
    time.sleep(0.25)

